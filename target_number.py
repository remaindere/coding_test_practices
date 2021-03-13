# BFS
from collections import deque
def solution(numbers, target):
    answer = 0
    
    storage = deque([(0, 0)])
    
    while storage :
        print(storage)
        sumval, stage = storage.popleft()
        
        if stage == len(numbers) :
            if sumval == target :
                answer+=1
        
        else :
            num = numbers[stage]
            storage.append((sumval+num, stage +1))
            storage.append((sumval-num, stage +1))
    
    return answer
#dfs below
'''

answer = 0
def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer

def dfs(numbers, target, sumval, idx):
    global answer
    print(target,sumval,idx)
    if sumval == target and idx == len(numbers) :
        answer+=1
        return
    if idx == len(numbers) :
        return
    
    dfs(numbers, target, sumval+numbers[idx], idx+1)
    dfs(numbers, target, sumval-numbers[idx], idx+1)
'''

#https://programmers.co.kr/learn/courses/30/lessons/43165
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
