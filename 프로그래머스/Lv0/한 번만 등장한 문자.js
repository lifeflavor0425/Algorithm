// 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

function solution(s) {
    // var answer = '';
    // let arr = []
    // for(let i=0; i<s.length;i+=1){
    //     let count = 0;
    //     count = [...s].reduce((acc,index)=>{
    //     return index === s[i] ? acc+=1 : acc
    // },0)
    //     if(count === 1) arr.push(s[i])
    // }
    // answer = arr.sort().join('')
    // return answer;
    
    // for ~ of ~ 사용 -> index를 앞과 뒤에서 구했을 때 같은 것 = 유일한 1개 
    let res = [];
    for (let c of s) if (s.indexOf(c) === s.lastIndexOf(c)) res.push(c);
    return res.sort().join('');
}
