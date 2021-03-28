changes = [500, 100, 50, 10, 5, 1]
count = 0
a = int(input())
c_val = 1000-a
#1000-380 = 620
    
for i in changes:
    count += c_val//i
    c_val %= i
    
print(count)

#https://www.acmicpc.net/source/24437184
#Baekjoon, https://www.acmicpc.net/
