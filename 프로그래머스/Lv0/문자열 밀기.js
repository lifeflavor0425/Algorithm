// 문제 설명
// 문자열 "hello"에서 각 문자를 오른쪽으로 한 칸씩 밀고 마지막 문자는 맨 앞으로 이동시키면
//  "ohell"이 됩니다. 이것을 문자열을 민다고 정의한다면 문자열 A와 B가 매개변수로 주어질 때,
//  A를 밀어서 B가 될 수 있다면 몇 번 밀어야 하는지 횟수를 return하고 밀어서 B가 될 수 없으면 -1을
//  return 하도록 solution 함수를 완성해보세요.

// 제한사항
// 0 < A의 길이 = B의 길이 < 100
// A, B는 알파벳 소문자로 이루어져 있습니다.
function solution(A, B) {
  var answer = 0;
  let queue = [...A];
  for (let index = 0; index < A.length; index += 1) {
    if (queue.join("") == B) return (answer = index);
    popAndUnshift(queue);
  }
  if (answer === 0) return -1;
  return answer;
}
function popAndUnshift(queue) {
  const popStr = queue.pop();
  queue.unshift(popStr);
  return queue;
}
// 미친 아이디어 : B의 문자를 이어 붙이면 A의 문자열이 나옴, 그 인덱스가 이동한 개수
// let solution=(a,b)=>(b+b).indexOf(a)
module.exports = solution;
