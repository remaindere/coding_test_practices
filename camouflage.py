def solution(clothes):
    answer = 0
    
    clo_dict = {}
    
    for cloth in clothes :
        clo_dict[cloth[1]] = clo_dict.get(cloth[1], 0) + 1

    clo_vals = list(clo_dict.values())
    
    mul_v = 1
    for cv in clo_vals :
            mul_v *= cv+1
    
    answer = mul_v -1
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42578
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
