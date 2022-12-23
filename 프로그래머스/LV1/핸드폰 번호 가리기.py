# 문제 설명
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때,
# 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수,
# solution을 완성해주세요.

# 제한 조건
# phone_number는 길이 4 이상, 20이하인 문자열입니다.
# 입출력 예
# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"
def solution(phone_number):

    # answer = ""
    # number_text = phone_number[-4:]
    # text = phone_number.replace(number_text, "")
    # for i in text:
    #     answer += "*"
    # answer += number_text
    # print(answer)
    # return answer
    # --> 머가 문젠지 모름

    ## 한줄
    # print("*" * (len(phone_number) - 4) + phone_number[-4:])
    # return "*" * (len(phone_number) - 4) + phone_number[-4:]

    text_line = len(phone_number) - 4
    answer = "".join(["*" for i in range(text_line)])
    answer += phone_number[-4:]
    print(answer)
    return answer


solution("01033334444")
solution("027778888")
solution("1234567890123456789")
solution("00000")
