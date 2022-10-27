function solution(n) {
  var answer = 0;
  //    for(let vn =1; vn < n; vn++){
  //    if(n === (vn*vn)){
  //        return 1;
  //    }else
  //         answer = 2;
  // }
  //    return answer
  return Math.sqrt(n) === Math.floor(Math.sqrt(n)) ? 1 : 2;
}
