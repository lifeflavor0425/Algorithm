// 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

function solution(array, n) {
    var answer = 0;
    array.push(n)
    let index = array.sort((a,b)=>a-b).indexOf(n)
    return array[index]-array[index-1] > array[index+1] -array[index] ? array[index+1] : array[index-1]
    // map 
    // let solution=(r,n)=>r.map(e=>[e,Math.abs(e-n)]).sort((a,b)=>a[1]-b[1]||a[0]-b[0])[0][0]
}
