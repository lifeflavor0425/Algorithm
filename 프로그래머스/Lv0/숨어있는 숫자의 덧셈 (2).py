# 문자열 my_string이 매개변수로 주어집니다. my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

def solution(my_string):
    answer = 0
    num = 0
    my_string += "A"
    for index in my_string : 
        if index.lower() == index.upper() :        
            num = num*10 + int(index)
        else :
            answer += num
            num = 0
    return answer
