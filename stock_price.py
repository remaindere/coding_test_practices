from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)

    while prices :
        c = prices.popleft()
        count = 0
        for i in prices :
            count = 1 + count
            if(c > i) :
                break
        answer.append(count)
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42584
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
