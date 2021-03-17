def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x : x[2])
    cy_t = [x for x in range(n)]
    
    for st, dst, cost in costs :
        if cy_t[st] != cy_t[dst] :
            dest = cy_t[dst]
            for i in range(n):
                if cy_t[i] == dest :
                    cy_t[i] = cy_t[st]
            answer += cost
        if len(set(cy_t)) == 1:
            break
        
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42861
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
