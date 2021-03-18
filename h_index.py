def solution(citations):
    answer = 0
    
    citations.sort()
    
    n = len(citations)
    b_idx = 0
    
    for i in range(n):
        if(n-i<=citations[i]):
            b_idx = i
            break
    
    #남은 논문 수 n-b_idx        
    #break된 idx지점의 값과 남은 논문값이 같은경우
    if(citations[b_idx]==n-b_idx):
        answer = citations[b_idx]
        return answer
    #break된 idx값에서 idx지점의 값까지, 남은 논문 수와 일치할때까지++
    for i in range(b_idx,citations[b_idx]):
        if(n-b_idx==i):
            answer = i
            break
    
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42747
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
