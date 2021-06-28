'''
메모리 초과 ... 해결중
'''

import sys
X = int(input())

samples = [[X, 0]]
answer = set([])
for sample in samples :
    if sample[0] == 1 :
        answer.add(sample[1])
    if sample[0] < 1 :
        continue
    if sample[0] % 3 == 0 :
        samples.append([sample[0] / 3, sample[0] + 1])
    if sample[0] % 2 == 0 :
        samples.append([sample[0] / 3, sample[0] + 1])
    samples.append([sample[0] - 1, sample[0] + 1])

print(min(answer))

# baekjoon, https://www.acmicpc.net/problem/1463
