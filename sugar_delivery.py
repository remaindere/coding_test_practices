N = int(input())
sugar = 0
while N > 0 :
  if N % 5 == 0 :
    sugar += N / 5
    break
  else :
    N = N - 3
    sugar += 1
return sugar
# beakjoon, https://www.acmicpc.net/problem/2839
