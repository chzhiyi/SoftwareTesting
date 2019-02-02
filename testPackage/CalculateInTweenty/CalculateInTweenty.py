#encoding=utf=8

import random
import const

# 定义加减法运算的数字范围[0,20]、出题数
const.MAX = 20
const.MIN = 0
const.NUMS = 10

nums = const.NUMS


def generateMathExam():
    sysbol = random.choice('+-')
    max = random.randint(0, const.MAX)
    if sysbol == '+':
        min = random.randint(0, const.MAX)
        result = max + min
    else:
        min = random.randint(0, max)
        result = max - min
    return [max.__str__() + ' ' + sysbol + ' ' + min.__str__() + ' = ', result]


while nums >= 1:
    exam = generateMathExam()
    expected = exam[1].__str__()

    actual = input(exam[0])
    while True:
        if expected == actual.strip():
            print("Congratulations!")
            break
        else:
            print("Error!\n")
            actual = input(exam[0])

    nums = nums -1