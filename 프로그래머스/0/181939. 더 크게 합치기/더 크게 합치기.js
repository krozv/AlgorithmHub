function solution(a, b) {
    var answer = 0;
    const firstResult = Number(String(a) + String(b));
    const secondResult = Number(String(b) + String(a));
    answer = firstResult >= secondResult ? firstResult : secondResult;
    return answer;
}