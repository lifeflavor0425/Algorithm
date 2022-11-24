// my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

function solution(my_string) {
    // let newArr = my_string.split(' ')
    // console.log(newArr)
    // return newArr.includes('+') ? Number(newArr[0]) + Number(newArr[2]) :Number(newArr[0]) - Number(newArr[2])
    
    //eval 은 안쓰는 것이 좋다
    return eval(my_string)
}
