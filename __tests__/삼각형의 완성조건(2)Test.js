const solution = require("../프로그래머스/Lv0/삼각형의 완성조건(2)");
describe("삼각형의 완성조건(2)", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution([1, 2]);
    expect(answer).toStrictEqual(1);
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution([3, 6]);
    expect(answer).toStrictEqual(5);
  });
  test(`테스트 케이스 3 `, () => {
    const answer = solution([11, 7]);
    expect(answer).toStrictEqual(13);
  });
});
