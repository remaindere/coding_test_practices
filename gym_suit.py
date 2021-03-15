from collections import deque

def solution(n, lost, reserve):
    answer = 0
    
    '''
    answer = n-len(lost)
    
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if(lost[i] == reserve[j]) :
                lost[i]=0
                reserve[j]=-2
                answer+=1
                break
                
    for i in range(len(lost)) :
        for j in range(len(reserve)) :
            if(lost[i] == reserve[j]-1 or lost[i] == reserve[j] or lost[i] == reserve[j]+1) :
                lost[i]=0
                reserve[j]=-2
                answer+=1
                break
    print(lost)
    print(reserve)
    '''
    
    temp = 0
    has_clothes = []
    
    for i in range(n):
        has_clothes.append(1)
    
    for i in lost:
        has_clothes[i-1]-=1

    for i in reserve:
        has_clothes[i-1]+=1
    
    for i in range(len(has_clothes)):
        if(has_clothes[-i]>1) :
            if(has_clothes[-i-1]<1) :
                has_clothes[-i]-=1
                has_clothes[-i-1]+=1
    
    for i in range(len(has_clothes)-1):
        if(has_clothes[i]>1) :
            if(has_clothes[i+1]<1) :
                has_clothes[i]-=1
                has_clothes[i+1]+=1
    
    for i in range(len(has_clothes)):
        if(has_clothes[i]>=1):
            answer+=1
    
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42862
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
