def solution(people, limit):
    answer = 0
    if(len(people) == 1) :
        answer = 1
        return answer
    
    people.sort()
    
    l_idx = 0
    r_idx = len(people)-1
    
    while l_idx<=r_idx :
        if people[r_idx] + people[l_idx] <= limit :
            answer += 1
            l_idx +=1
            r_idx -=1
        else :
            answer += 1
            r_idx -=1
        
    if(len(people) == 1) :
        answer += 1
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42885
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
