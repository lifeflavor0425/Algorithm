const solution = require("../프로그래머스/Lv0/캐릭터 좌표");
describe("캐릭터 좌표", () => {
  test(`테스트 케이스 1 `, () => {
    const answer = solution(
      ["left", "right", "up", "right", "right"],
      [11, 11]
    );
    expect(answer).toStrictEqual([2, 1]);
  });
  test(`테스트 케이스 2 `, () => {
    const answer = solution(["down", "down", "down", "down", "down"], [7, 9]);
    expect(answer).toStrictEqual([0, -4]);
  });
});
