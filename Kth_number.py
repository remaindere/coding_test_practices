def solution(array, commands):
    answer = []
    
    sli = []
    a = 0
    for i in range(len(commands)):
        sli = array[commands[i][0]-1:commands[i][1]]
        sli.sort()
        a = sli[commands[i][2]-1]
        answer.append(a)
    
    return answer
#https://programmers.co.kr/learn/courses/30/lessons/42748
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
