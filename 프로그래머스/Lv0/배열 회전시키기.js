// 정수가 담긴 배열 numbers와 문자열 direction가 매개변수로 주어집니다. 배열 numbers의 원소를 direction방향으로 한 칸씩 회전시킨 배열을 return하도록 solution 함수를 완성해주세요.

function solution(numbers, direction) {
    var answer = [];
    let element = 0;
    if(direction === 'right'){
        element = numbers.pop()
         numbers.unshift(element)
    } else {
        element = numbers.shift()
         numbers.push(element)
    }
    return answer = numbers
}
