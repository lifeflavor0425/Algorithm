const solution = require("../프로그래머스/Lv0/2차원으로 만들기");
describe("2차원으로 만들기", () => {
  test("[1, 2, 3, 4, 5, 6, 7, 8], 2 ", () => {
    const answer = solution([1, 2, 3, 4, 5, 6, 7, 8], 2);
    expect(answer).toStrictEqual([
      [1, 2],
      [3, 4],
      [5, 6],
      [7, 8],
    ]);
  });
  test("[100,95,2,4,5,6,18,33,948],3", () => {
    const answer = solution([100, 95, 2, 4, 5, 6, 18, 33, 948], 3);
    expect(answer).toStrictEqual([
      [100, 95, 2],
      [4, 5, 6],
      [18, 33, 948],
    ]);
  });
});
