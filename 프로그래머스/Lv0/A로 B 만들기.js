// 문자열 before와 after가 매개변수로 주어질 때, before의 순서를 바꾸어 after를 만들 수 있으면 1을, 만들 수 없으면 0을 return 하도록 solution 함수를 완성해보세요.

function solution(before, after) {
    var answer = [];
    let afterArr = after.split('')
    before.split('').forEach(e=> {
       if(afterArr.includes(e))  afterArr.splice(afterArr.indexOf(e), 1)
    })
    return afterArr.length === 0 ? 1 : 0

    // 정렬해서 비교
    // return before.split('').sort().join('') === after.split('').sort().join('') ? 1 : 0;
}
