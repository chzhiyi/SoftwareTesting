import re

def re_extract_numbers():
    tmp = 'qs23hs24bj25bl45jc123ys234zl0'
    pat = r'[0-9]{1,}'
    nums = re.findall(pat, tmp)
    print(nums)


def re_match_hello_world(str_value):
    pattern = 'hello world'
    matchs = re.match(pattern, str_value)
    print(matchs)
    if matchs is not None :
        print(matchs.group(0))
        print(matchs.span())


def print_matchs(matchs):
    print(matchs)
    print(matchs.group(0))
    print(matchs.span())


def re_match_simple_regular_expression(str_value):
    pattern = r'T[moi]+'
    matchs = re.match(pattern, str_value)
    print_matchs(matchs)


def re_match_sample(pattern, str_value):
    matchs = re.match(pattern, str_value)
    print_matchs(matchs)




if __name__ == '__main__':
    # re_extract_numbers()

    # ## 'hello world'也是正则表达式,只能匹配字符串'hello world'或以'hello world'开头的字符串
    # re_match_hello_world('hello world')
    # re_match_hello_world('hello world, hello china')
    # ## 下面匹配失败。NoneType 没有属性或方法group(0)、span()
    # re_match_hello_world('hello')
    # re_match_hello_world('today, hello , hello world, Hello World')

    re_match_simple_regular_expression('Tim')
    re_match_simple_regular_expression('Tom')
    re_match_simple_regular_expression('Toooooom')
    re_match_simple_regular_expression('Tuple')

    # re_match_sample(r'T[io]+m', 'Tiiiiiiiiiim')
    # re_match_sample(r'T[io]+m', 'Tiooioooooim')

    # re_match_sample(r'^[0-9]+$', '31421341234')
    # # re_match_sample(r'^[0-9]+$', '214saf12312')
    # re_match_sample(r'[0-9]+', '214saf12312')


