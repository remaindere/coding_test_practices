def solution(gems):
    gems_dict = {}
    
    l_cur = 0
    r_cur = 0
    l_opt = 0
    r_opt = len(gems)-1
    
    yet = 0 # 탈출조건
    for gem in gems:
        gems_dict[gem] = gems_dict.get(gem,0)
    
    while l_cur < len(gems) and r_cur < len(gems) and l_cur<=r_cur:
        gems_dict[gems[r_cur]]+=1
        yet = 0
        
        for i in gems_dict.values():
            if(i==0):
                yet=1
        
        if(yet):
            r_cur+=1 #오른쪽 커서 이동 (탐색범위 증가)
        else:
            if(r_opt-l_opt>r_cur-l_cur):
                l_opt = l_cur   
                r_opt = r_cur
            gems_dict[gems[l_cur]]-=1
            l_cur+=1 #왼쪽 커서 이동 (탐색범위 감소)
    
    answer = [l_opt+1, r_opt+1]
    return answer

#https://programmers.co.kr/learn/courses/30/lessons/67258
#카카오 2020 인턴십 테스트 : https://tech.kakao.com/2020/07/01/2020-internship-test/
