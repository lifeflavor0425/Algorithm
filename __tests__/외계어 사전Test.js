const solution = require("../프로그래머스/Lv0/외계어 사전");
describe("외계어 사전", () => {
  test(`테스트 케이스 1 : ["p", "o", "s"],  ["sod", "eocd", "qixm", "adio", "soo"]`, () => {
    const answer = solution(
      ["p", "o", "s"],
      ["sod", "eocd", "qixm", "adio", "soo"]
    );
    expect(answer).toStrictEqual(2);
  });
  test(`테스트 케이스 2 : ["z", "d", "x"],   ["def", "dww", "dzx", "loveaw"]`, () => {
    const answer = solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]);
    expect(answer).toStrictEqual(1);
  });
  test(`테스트 케이스 3 : ["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]`, () => {
    const answer = solution(
      ["s", "o", "m", "d"],
      ["moos", "dzx", "smm", "sunmmo", "som"]
    );
    expect(answer).toStrictEqual(2);
  });
});
