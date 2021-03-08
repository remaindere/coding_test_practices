def solution(phone_book):
    answer = True
        
    phone_book.sort()

    i = 0
    j = 0
    
    while i<len(phone_book) :
        while j<len(phone_book) :
            if(len(phone_book[i]) < len(phone_book[j])) :
                if(phone_book[j].find(phone_book[i]) != -1) :
                    answer = False;
                    return answer;
            j = j + 1    
        i = i + 1

    return answer

#https://programmers.co.kr/learn/courses/30/lessons/42577
#출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
