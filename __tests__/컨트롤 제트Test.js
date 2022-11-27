const solution = require("../프로그래머스/Lv0/컨트롤 제트");

describe("컨트롤 제트", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution("1 2 Z 3");
    expect(answer).toStrictEqual(4);
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution("10 20 30 40");
    expect(answer).toStrictEqual(100);
  });
  test(`테스트 케이스 3 `, () => {
    const answer = solution("10 Z 20 Z 1");
    expect(answer).toStrictEqual(1);
  });
  test("테스트 케이스 4", () => {
    const answer = solution("1 1 1 1 Z Z 1 1 Z Z Z Z Z Z 1");
    expect(answer).toStrictEqual(1);
  });
});
