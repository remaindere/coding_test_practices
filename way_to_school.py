def solution(m, n, puddles):
    answer = 0
    
    route_map = [[0 for x in range(m+1)] for y in range(n+1)]
            
    for puddle in puddles :
        route_map[puddle[1]][puddle[0]] = -1 
    
    route_map[1][1] = 1
    
    #print(route_map) 
    
    for y in range(1, n+1) :
        for x in range(1, m+1) :
            if route_map[y][x] == -1 :
                continue
            if y == 1 and x == 1 :
                continue 
            if route_map[y][x-1] == -1 :
                route_map[y][x] = route_map[y-1][x]
            elif route_map[y-1][x] == -1 :
                route_map[y][x] = route_map[y][x-1]
            else :
                route_map[y][x] = route_map[y][x-1] + route_map[y-1][x]
            #print(route_map[y][x], route_map[y][x-1], route_map[y-1][x])
            
    #print(route_map)
    
    answer = route_map[n][m] % 1000000007        
    return answer
  
#https://programmers.co.kr/learn/courses/30/lessons/42898
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
