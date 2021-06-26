N = int(input())

sugar = 0

while N >= 0 : # while sugar bags are exist
  if N % 5 == 0 :
    sugar += N // 5
    break
    
  N -= 3
  sugar += 1
  
if N < 0 : # it can't be divided by zero
  print(-1)
else : # div process ended successful
  print(sugar)

# baekjoon, https://www.acmicpc.net/problem/2839
