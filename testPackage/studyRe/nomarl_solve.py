## 找出以bai开头的花名
l = ['qiaosong', 'huasheng', 'baijing', 'bailian', 'jingchu', 'yinshuang', 'zilu']


def search_start_with_bai(lt):
    for tmpl in lt:
        if tmpl[0:3] == 'bai':
            print(tmpl)


def senior_search_start_with_bai(lt):
    tmp = [tmpl for tmpl in lt if tmpl[:3] == 'bai']
    print(tmp)


## 提取连续的数字
def extract_str():
    tmp = "qs23hs24bj25bl45jc123ys234zl0"
    for i in range(len(tmp)):
        if tmp[i] >= 'a' and tmp[i] <= 'z':
            tmp = tmp.replace(tmp[i], ' ')
    print([ s for s in tmp.split(' ') if len(s)>0 and int(s)>=0 ])


def search(lt):
    search_start_with_bai(lt)
    senior_search_start_with_bai(lt)


if __name__ == '__main__':
    search(l)
    extract_str()