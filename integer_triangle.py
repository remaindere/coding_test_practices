def solution(triangle):
    answer = 0
    
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1 :
                triangle[i][j] += triangle[i-1][-1]
            else :
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    
    answer = max(triangle[len(triangle)-1])
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42576
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
