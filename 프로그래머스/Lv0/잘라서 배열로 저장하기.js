// 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

function solution(my_str, n) {
    var answer = [];
    const count = Math.ceil(my_str.length/n)
    for(let i=0; i< count; i+=1){
        answer.push(my_str.slice(0,n))
        my_str = my_str.slice(n)
    }

    return answer;
    // 정규식
    // return my_str.match(new RegExp(`.{1,${n}}`, "g"));
}
