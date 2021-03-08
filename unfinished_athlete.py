def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    i = 0
    while participant[i]==completion[i]:
        i = i + 1
        if(i==len(completion)):
            break
    answer = participant[i]
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42576
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
