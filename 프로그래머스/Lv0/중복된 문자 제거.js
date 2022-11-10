// 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

function solution(my_string) {
    var answer = '';
    let arr = []
    answer = my_string.split('').filter(cur=> {
         if(!arr.includes(cur)) return arr.push(cur)
     }).join('')
    return answer;
    // set 활용
   //  return [...new Set(my_string)].join('');
}
