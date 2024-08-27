# https://school.programmers.co.kr/learn/courses/30/lessons/42842

import cmath

def solution(brown, yellow):	
    sum = brown / 2 + 2
    prod = brown + yellow
    diff = cmath.sqrt(sum ** 2  - prod * 4).real

    a = int((sum + diff) / 2)
    b = int(sum - a)

    return [a, b]
