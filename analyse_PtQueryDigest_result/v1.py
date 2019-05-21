# _*_coding: utf-8_*_
# create_time: 2019-05-20 06:33
# author: qiaosong

import linecache
import re
import db_utils


def get_number(s):
    r = s.lower().replace('\n', '')
    if r[-2:] == 'ms':
        return float(r.replace('ms', ''))/1000
    elif r[-2:] == 'us':
        return float(r.replace('us', ''))/1000/1000
    elif r[-1] == 'k':
        return float(r.replace('k', '')) * 1000
    elif r[-1] == 'm':
        return float(r.replace('m', '')) * 1000 * 1000
    elif r[-1] == 'g':
        return float(r.replace('g', '')) * 1000 * 1000
    elif r[-1] == 's':
        return float(r.replace('s', ''))
    else:
        return r


def get_query(i, value, temp):
    rank = value.split(' ')[2].replace(':', '')
    id = value.split(' ')[8]
    flag = False
    for key in dist.keys():
        if id.startswith(key):
            if rank == dist[key]['Rank']:
                flag = True
                dist_detail[key] = {}
                break
    if flag:
        i = i + 7
        value = re.sub(' {2,}', ' ', temp[i]).split(' ')
        min_exec_time = value[5]
        max_exec_time = value[6]
        avg_exec_time = value[7]
        pt95_exec_time = value[8]
        median_exec_time = value[10]

        i = i + 1
        value = re.sub(' {2,}', ' ', temp[i]).split(' ')
        total_lock_time = value[4]

        i = i + 1
        value = re.sub(' {2,}', ' ', temp[i]).split(' ')
        total_rows_sent = value[4]

        i = i + 1
        value = re.sub(' {2,}', ' ', temp[i]).split(' ')
        total_rows_exmaine = value[4]

        i = i + 4
        value = re.sub(' {2,}', ' ', temp[i]).split(' ')
        hosts = value[2:]

        i = i + 1
        value = re.sub(' {2,}', ' ', temp[i]).split(' ')
        users = value[2:]

        print(min_exec_time, max_exec_time, avg_exec_time, pt95_exec_time, median_exec_time, total_lock_time,
              total_rows_sent, total_rows_exmaine, hosts, users)

        while temp[i].startswith('#'):
            i = i + 1

        str_sql = ''
        while not temp[i].startswith('#') and temp[i] != '\n':
            str_sql = str_sql + ' ' + temp[i]
            i = i + 1

        dist_detail[key] = {'min_exec_time': get_number(min_exec_time), 'max_exec_time': get_number(max_exec_time), 'avg_exec_time': get_number(avg_exec_time),
                      'pt95_exec_time': get_number(pt95_exec_time), 'median_exec_time': get_number(median_exec_time),
                      'total_lock_time': get_number(total_lock_time),
                      'total_rows_sent': get_number(total_rows_sent), 'total_rows_examine': get_number(total_rows_exmaine), 'hosts': ' '.join(hosts).replace('\n', ''),
                      'users': ' '.join(users).replace('\n', ''), 'sql': str_sql}
        dist_detail[key]['sql'] = re.sub(' {2,}', ' ', dist_detail[key]['sql'].replace('\t', ' ').replace('\n', ' ').replace('\G', ''))
    return i


file = './pt_dir/slow_slave_0517.log'
dist = {}
dist_detail = {}
period_dist = {}



temp = linecache.getlines(file)
global i
for i in range(len(temp)):
    value = re.sub(' {2,}', ' ', temp[i])
    if value == '\n':
        continue

    if not value.startswith('# Profile') and i <= 30:
        if value.startswith('# Hostname:'):
            period_dist['hostname'] = value.split(' ')[2]
        elif value.startswith('# Files:'):
            period_dist['files'] = value.split(' ')[2]
        elif value.startswith('# Overall:'):
            period_dist['total'] = get_number(value.split(' ')[2])
            period_dist['unique'] = get_number(value.split(' ')[4])
        elif value.startswith('# Time range:'):
            period_dist['time_range'] = ' '.join(value.split(' ')[3:]).replace('T', ' ').replace('to', ' - ')
        elif value.startswith('# Exec time'):
            period_dist['total_exec_time'] = get_number(value.split(' ')[3])
        elif value.startswith('# Lock time'):
            period_dist['total_lock_time'] = get_number(value.split(' ')[3])
        i = i + 1

    if value.startswith('# Profile'):
        i = i + 3
        value = re.sub(' {2,}', ' ', temp[i])
        while re.search('^# [\d]+ 0x', value) or re.search('^# MISC 0xMISC', value):
            v = value.split(' ')
            key = v[2].replace('.', '')
            num = v[1]
            response_time = v[3]
            percent = v[4]
            calls = v[5]
            r_call = v[6]
            v_m = v[7]

            dist[key] = {'Rank': num, 'Response time': response_time, 'percent':percent, 'Calls': calls, 'R/Call': r_call, 'V/M': v_m}
            i = i + 1
            value = re.sub(' {2,}', ' ', temp[i])

    if re.search('^# Query [\d]{1,}: .*', value):
        i = get_query(i, value, temp)



conn = db_utils.get_connection()
period_sql = """INSERT INTO slow_period(PERIOD, TOTAL, `UNIQUE`, TOTAL_EXEC_TIME, TOTAL_LOCK_TIME, FILES, HOSTNAME)
                VALUES('{total_range}', {total}, {unique}, {total_exec_time}, {total_lock_time}, '{files}', '{hostname}')"""\
    .format(total_range=period_dist['time_range'], total=period_dist['total'], unique=period_dist['unique'],
            total_exec_time=period_dist['total_exec_time'], total_lock_time=period_dist['total_lock_time'],
            files=period_dist['files'], hostname=period_dist['hostname']).replace('\n', '')
cursor = conn.cursor()
cursor.execute(period_sql)
conn.commit()
period_id = cursor.lastrowid

print(len(dist), '---' ,len(dist_detail))

for key in dist_detail.keys():
    sql = dist_detail[key]['sql'].replace('\'', '\\\'').replace('"', '\"')
    insert_sql = """INSERT INTO slow_sql(`sql`) VALUES('{sql}')""".format(sql=sql)
    print(insert_sql)
    cursor.execute(insert_sql)
    conn.commit()
    sql_id = cursor.lastrowid
    insert_result = """INSERT INTO slow_results(PERIOD_ID, RANK, QUERY_ID, SQL_ID, RESPONSE_TIME, TOTAL_NUM, PERCENT, R_CALL, V_M, MIN_EXEC_TIME, MAX_EXEC_TIME, AVG_EXEC_TIME, PT95_EXEC_TIME, 
                        MEDIAN_EXEC_TIME, TOTAL_LOCK_TIME, TOTAL_ROWS_SENT, TOTAL_ROWS_EXAMINE, HOSTS, USERS)
                        VALUES({period_id}, {rank}, '{query_id}', {sql_id}, {response_time}, {total_num}, '{percent}', {r_call}, {v_m}, {min_exec_time}, {max_exec_time}, {avg_exec_time},
                        {pt95_exec_time}, {median_exec_time}, {total_lock_time}, {total_rows_sent}, {total_rows_examine}, '{hosts}', '{users}')""".format(period_id=period_id, rank=dist[key]['Rank'], query_id=key,
                            sql_id=sql_id,response_time=dist[key]['Response time'], total_num=dist[key]['Calls'], percent=dist[key]['percent'], r_call=dist[key]['R/Call'], v_m=dist[key]['V/M'], min_exec_time=dist_detail[key]['min_exec_time'],
                            max_exec_time=dist_detail[key]['max_exec_time'], avg_exec_time=dist_detail[key]['avg_exec_time'],pt95_exec_time=dist_detail[key]['pt95_exec_time'], median_exec_time=dist_detail[key]['median_exec_time'],
                            total_lock_time=dist_detail[key]['total_lock_time'], total_rows_sent=dist_detail[key]['total_rows_sent'], total_rows_examine=dist_detail[key]['total_rows_examine'],
                            hosts=dist_detail[key]['hosts'], users=dist_detail[key]['users'])
    print(insert_result)
    cursor.execute(insert_result)
    conn.commit
cursor.close()
conn.close()


