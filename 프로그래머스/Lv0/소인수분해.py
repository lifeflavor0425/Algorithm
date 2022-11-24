# 소인수분해란 어떤 수를 소수들의 곱으로 표현하는 것입니다. 예를 들어 12를 소인수 분해하면 2 * 2 * 3 으로 나타낼 수 있습니다. 따라서 12의 소인수는 2와 3입니다. 자연수 n이 매개변수로 주어질 때 n의 소인수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

def solution(n):
    answer = []
    sosu = 2
    while n >= sosu :
        if n%sosu == 0 :
            n= n/sosu
            if  sosu not in answer :
                answer.append(sosu)
        else :
            sosu +=1

    return answer
#     answer = []
#     q=[]
#     for i in range(2,n+1):   #n의 약수 구하기
#         if n%i ==0:
#             q.append(i)    

#     for i in q:  #n의 약수 중에서 소수 구하기
#         for j in range(2,5000):
#             if i*j in q:
#                 q.remove(i*j)
#     q.sort()
#     return q
