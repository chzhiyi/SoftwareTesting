import re


def get_urls():
    urls = set()
    line_number = 0
    with open('log.result', 'r') as f:
        for line in f.readlines():
            urls.add(line.split(' ')[2])
            line_number += 1
    for url in urls:
        print(url)
    print("url去重后的总数=",len(urls))
    print('文件总行数=', line_number)


def get_urls_with_exclude_productids():
    urls = set()
    with open('log.result', 'r') as f:
        for line in f.readlines():
            temp = line.split(' ')[2]
            value = re.sub(r'/github/reposity/issues/[\w]{32,}', '/github/reposity/issues/20190304000001', temp, re.IGNORECASE)
            if value is not None:
                urls.add(value)
            else:
                urls.add(temp)
    for url in urls:
        print(url)
    print("去重后的url总数: ", len(urls))



get_urls()
get_urls_with_exclude_productids()