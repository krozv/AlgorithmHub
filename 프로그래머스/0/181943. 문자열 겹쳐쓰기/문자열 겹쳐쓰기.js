function solution(my_string, overwrite_string, s) {
    var answer = '';
    const front_string = my_string.slice(0, s)
    const back_string = my_string.slice(s+overwrite_string.length)
    answer = front_string + overwrite_string + back_string
    return answer;
}