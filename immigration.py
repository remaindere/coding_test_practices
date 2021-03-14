def solution(n, times):
    answer = -1
    
    times.sort()
    
    a = 0
    b = n*times[-1]
    
    while a <= b :
        half = (a+b)//2
        
        #print("a, b, half : ", a,b,half)
        summation = 0
        for time in times :
            summation += half//time
            
        if summation >= n: 
            if answer == -1: ## init 
                answer = half
            else:
                answer = min(answer,half)
            b = half - 1
        elif summation < n: 
            a = half + 1
        
    return answer
#https://programmers.co.kr/learn/courses/30/lessons/43238
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
