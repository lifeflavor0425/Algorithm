// 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.

function solution(bin1, bin2) {
    // var answer = '';
    // let num1 =0;
    // let num2 =0;
    //  num1 = bin1.split('').reverse().reduce((sum,value,index)=>{ 
    //     return sum += value * Math.pow(2,index) 
    // },0)
    //  num2 = bin2.split('').reverse().reduce((sum,value,index)=>{
    //     return value === 1 ? sum += Math.pow(2,index) : sum +=  Math.pow(2,index)
    // },0)
    // let sum = num1 + num2
    // let arr = []
    // while(sum >= 1){
    //     arr.push(sum%2)
    //     sum = Math.floor(sum/2)
    // }
    // console.log(arr)
    // answer = arr.reverse().join('')
    // return answer;
    
    // 2진수 합
    return (parseInt(bin1, 2) + parseInt(bin2, 2)).toString(2);
}
