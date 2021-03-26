#include <string>
#include <vector>
#include <map>

using namespace std;

vector<int> solution(vector<string> gems) {
    vector<int> answer;
    map<string, int> search, kindofgem;
    int range = 100000;

    kindofgem.insert({gems[0], 1});
    bool exist = false;
    for (int gi = 1; gi < gems.size(); gi++) 
        kindofgem[gems[gi]]++;

    int start = 0;
    for (int end = 0; end < gems.size(); end++) {
        search[gems[end]]++;

        if (search.size() == kindofgem.size()) {
            while (search.size() == kindofgem.size()) {
                search[gems[start]]--;
                if (search[gems[start]] == 0) search.erase(gems[start]);
                start++;
            }
            if (end - (start-1) < range) {
                range = end - (start-1);
                answer = { start,end+1 };
            }
        }
    }

    return answer;
}

#https://programmers.co.kr/learn/courses/30/lessons/67258
#카카오 2020 인턴십 테스트 : https://tech.kakao.com/2020/07/01/2020-internship-test/
#ref:오영헌
