const solution = require("../프로그래머스/Lv0/문자열 밀기");

describe("문자열 밀기", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution("hello", "ohell");
    expect(answer).toStrictEqual(1);
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution("apple", "elppa");
    expect(answer).toStrictEqual(-1);
  });
  test(`테스트 케이스 3 `, () => {
    const answer = solution("apple", "apple");
    expect(answer).toStrictEqual(0);
  });
  //   test("테스트 케이스 4", () => {
  //     const answer = solution("1 1 1 1 Z Z 1 1 Z Z Z Z Z Z 1");
  //     expect(answer).toStrictEqual(1);
  //   });
});
