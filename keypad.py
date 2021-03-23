from collections import deque
def solution(numbers, hand):
    answer = ''   
    ans_list = []
    lh_cur = 10
    rh_cur = 12
    num = 0
    numbers = deque(numbers)
    
    while numbers:
        num = numbers.popleft()
        
        if(num%3==1): #1,4,7
            lh_cur = num
            ans_list.append('L')
        elif(num%3==0 and num!=0): #3,6,9
            rh_cur = num
            ans_list.append('R')
        else: #2,5,8,0        
            if(calc_distance(rh_cur,num)>calc_distance(lh_cur,num)):
                lh_cur = num
                ans_list.append('L')
            elif(calc_distance(rh_cur,num)<calc_distance(lh_cur,num)):
                rh_cur = num
                ans_list.append('R')
            else:#same distance cost
                if(hand=="left"):
                    lh_cur = num
                    ans_list.append('L')
                else :
                    rh_cur = num
                    ans_list.append('R')
    
    
    answer = ''.join(ans_list)
    return answer

def calc_distance(cur, target):
    count = 0
    calc_val = 0
    
    if(cur==0):
        cur=11
    if(target==0):
        target=11

    if(cur >= target):
        calc_val = cur - target
    else :
        calc_val = target - cur
        
    while calc_val%3!=0:
        count+=1
        calc_val-=1
    
    count+=calc_val//3

    return count

#https://programmers.co.kr/learn/courses/30/lessons/67256
#카카오 2020 인턴십 테스트 : https://tech.kakao.com/2020/07/01/2020-internship-test/
