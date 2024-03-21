const solution = require("../프로그래머스/Lv0/직사각형 넓이 구하기");
describe("삼각형의 완성조건(2)", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution([
      [1, 1],
      [2, 1],
      [2, 2],
      [1, 2],
    ]);
    expect(answer).toStrictEqual(1);
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution([
      [-1, -1],
      [1, 1],
      [1, -1],
      [-1, 1],
    ]);
    expect(answer).toStrictEqual(4);
  });
  //   test(`테스트 케이스 3 `, () => {
  //     const answer = solution([11, 7]);
  //     expect(answer).toStrictEqual(13);
  //   });
});
