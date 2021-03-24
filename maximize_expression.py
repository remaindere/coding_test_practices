from itertools import permutations
from copy import deepcopy
from collections import deque
import math
import re
def solution(expression):
    answer = 0
    
    numbers=('0','1','2','3','4','5','6','7','8','9')
    #print(help(permutations))
    ops_set = []
    ops_set = set(ops_set)
    cases = []
    exp_cp = deepcopy(expression)
    exp_cp = deque(exp_cp)
    exp_temp = []
    calc_cur = 0
    
    num_idx1 = 0
    num_idx2 = 0
    num1 = 0
    num2 = 0
    calc_res = ''
    res_list = []
    while exp_cp :
        c = exp_cp.popleft()
        if(c=='*' or c=='-' or c=='+'):
            ops_set.add(c)
    
    cases = list(map(''.join,permutations(ops_set, len(ops_set))))
    #print(list(cases))
    
    for i in range(math.factorial(len(ops_set))):
        exp_temp = deepcopy(expression)
        for j in cases[i]:
            while exp_temp.find(j)!=-1 :
                calc_cur = exp_temp.find(j)
                num_idx1 = calc_cur-1
                num_idx2 = calc_cur+1
                while exp_temp[num_idx1] in numbers :
                    if(num_idx1==0):
                        break
                    num_idx1-=1
                if(num_idx1!=0): 
                    num_idx1+=1
                while exp_temp[num_idx2] in numbers :
                    if(num_idx2==len(exp_temp)-1):
                        break
                    num_idx2+=1
                num1 = int(exp_temp[num_idx1:calc_cur])
                num2 = int(exp_temp[calc_cur+1:num_idx2])
                calc_res = str(eval)
                exp_temp = exp_temp.replace(exp_temp[num_idx1:num_idx2],calc_res)
                
        res_list.append(int(calc_res))
    
    
    answer = max(res_list)
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/67257
#카카오 2020 인턴십 테스트 : https://tech.kakao.com/2020/07/01/2020-internship-test/
