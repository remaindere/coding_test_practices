from collections import deque

def solution(progresses, speeds):
    answer = []
    
    est_res = []
    
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses :
        cur_p = progresses.popleft()
        cur_s = speeds.popleft()
        est_t = 100-cur_p
        est_rem = est_t / cur_s
        
        if(est_rem%1!=0):
            est_rem = int(est_rem) + 1

        est_res.append(est_rem)

    print(est_res)
    est_res = deque(est_res)
    
    while est_res : 
        cur = est_res.popleft()
        pop_c = 1
        for est in est_res :
            if cur >= est :
                pop_c+=1
            elif cur < est :
                break
        print(est_res)
        answer.append(pop_c)
        print(answer)
        while pop_c > 1 :
            est_res.popleft()
            pop_c -= 1
        for est in range(len(est_res)) :
            est_res[est] -= cur
            
            
    return answer
    
#https://programmers.co.kr/learn/courses/30/lessons/42586
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
