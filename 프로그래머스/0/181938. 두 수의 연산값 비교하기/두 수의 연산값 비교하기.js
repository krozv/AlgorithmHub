function solution(a, b) {
    var answer = 0;
    
    return Number(`${a}${b}`) >= 2*a*b ? Number(`${a}${b}`) : 2*a*b ;
}