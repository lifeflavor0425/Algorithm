const solution = require("../프로그래머스/Lv0/유한소수 판별하기");

describe("유한소수 판별하기", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution(7, 20);
    expect(answer).toStrictEqual(1);
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution(11, 22);
    expect(answer).toStrictEqual(1);
  });
  test(`테스트 케이스 3 `, () => {
    const answer = solution(12, 21);
    expect(answer).toStrictEqual(2);
  });
  test("테스트 케이스 4", () => {
    const answer = solution(21, 12);
    expect(answer).toStrictEqual(1);
  });
  test("테스트 케이스 5", () => {
    const answer = solution(30, 30);
    expect(answer).toStrictEqual(1);
  });
  test("테스트 케이스 6", () => {
    const answer = solution(10, 30);
    expect(answer).toStrictEqual(2);
  });
  test("테스트 케이스 7", () => {
    const answer = solution(70, 10);
    expect(answer).toStrictEqual(1);
  });
  test("테스트 케이스 8", () => {
    const answer = solution(10, 60);
    expect(answer).toStrictEqual(2);
  });
});
