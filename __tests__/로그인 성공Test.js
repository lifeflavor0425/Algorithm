const solution = require("../프로그래머스/Lv0/로그인 성공");

describe("로그인 성공", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution(
      ["meosseugi", "1234"],
      [
        ["rardss", "123"],
        ["yyoom", "1234"],
        ["meosseugi", "1234"],
      ]
    );
    expect(answer).toStrictEqual("login");
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution(
      ["programmer01", "15789"],
      [
        ["programmer02", "111111"],
        ["programmer00", "134"],
        ["programmer01", "1145"],
      ]
    );
    expect(answer).toStrictEqual("wrong pw");
  });
  test(`테스트 케이스 3 `, () => {
    const answer = solution(
      ["rabbit04", "98761"],
      [
        ["jaja11", "98761"],
        ["krong0313", "29440"],
        ["rabbit00", "111333"],
      ]
    );
    expect(answer).toStrictEqual("fail");
  });
  //   test("테스트 케이스 4", () => {
  //     const answer = solution("1 1 1 1 Z Z 1 1 Z Z Z Z Z Z 1");
  //     expect(answer).toStrictEqual(1);
  //   });
});
