import heapq
#import math
def solution(scoville, K):
    answer = 0
    count = 0
    heapq.heapify(scoville) # 힙 해짐 ㅋㅋ
    
    while scoville[0] < K:
        if len(scoville) < 2: 
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        count+=1
    answer = count
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42626
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
