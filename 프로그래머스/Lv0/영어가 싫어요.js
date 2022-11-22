// 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.
const numberObject = {
    "zero" : 0, "one" : 1, "two" : 2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9 
}
function solution(numbers) {
    var answer = 0;
    answer = split_tree(numbers)
    // 정규식 사용
    //  let d = ['zero', 'one','two','three','four','five','six','seven','eight','nine'];
    // for (let i in d) numbers = numbers.replace(new RegExp(d[i], 'g'), +i);
    // return +numbers;
    return answer;
}
function split_tree(numbers) {
    let newArr = []
    let numStr = ''
    let index = 0
    numbers.split("").some(e=> {
        index +=1
        numStr += e
        if(numberObject[numStr] !== undefined) { 
            newArr.push(numberObject[numStr])
            numStr = ''
            index = 0
        }
    })
    return Number(newArr.join(''))
}
