// 문제 설명
// 소수점 아래 숫자가 계속되지 않고 유한개인 소수를 유한소수라고 합니다.
// 분수를 소수로 고칠 때 유한소수로 나타낼 수 있는 분수인지 판별하려고 합니다.
//  유한소수가 되기 위한 분수의 조건은 다음과 같습니다.

// 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다.
// 두 정수 a와 b가 매개변수로 주어질 때, a/b가 유한소수이면 1을,
//  무한소수라면 2를 return하도록 solution 함수를 완성해주세요.

// 제한사항
// a, b는 정수
// 0 < a ≤ 1,000
// 0 < b ≤ 1,000

function solution(a, b) {
  // 내림차순
  let arr = [a, b].sort((a, b) => b - a);
  const remainder = gcd(arr[0], arr[1]);
  arr = arr.map((element) => element / remainder);
  if (a > b) {
    return sosu(arr[1]).length === 0 ? 1 : 2;
  } else {
    return sosu(arr[0]).length === 0 ? 1 : 2;
  }
  // 쉬운 답
  // return Number((a/b).toFixed(10)) == a/b ? 1 : 2
}
// 최대 공약수 구하기
function gcd(a, b) {
  const remainder = a % b; // 1번
  if (remainder === 0) return b; // 2번
  return gcd(b, remainder); // 3번
}
// 소인수 분해
function sosu(num) {
  let i = 2;
  let primes = [];
  while (true) {
    if (num % i === 0) {
      num = num / i;
      primes.push(i);
      i = 1;
    }
    i++;
    if (i > num) {
      break;
    }
  }
  primes = remove(primes);
  return primes;
}
// 2 or 5 제거
function remove(array) {
  if (array.includes(2)) array.splice(array.indexOf(2), 1);
  if (array.includes(5)) array.splice(array.indexOf(5), 1);
  if (array.includes(2) || array.includes(5)) return remove(array);
  else return array;
}
module.exports = solution;
