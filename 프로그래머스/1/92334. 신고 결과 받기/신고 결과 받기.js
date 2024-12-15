function solution(id_list, report, k) {
    // 신고 횟수를 다 합산
    // 신고 횟수가 k번 이상인 사람만 필터링
    // 해당 아이디가 신고한 사람이 있으면 email
    const warning_list = {}
    for (const id of id_list){
        warning_list[id] = {
            "count": 0,
            "warning": []
        }
        
    }
    for (const elem of report){
        const [a, b] = elem.split(' '); // a: 신고한 사람, b: 신고 당한 사람
        if (!(warning_list[a].warning.includes(b))){
            warning_list[a].warning.push(b)
        }
    }
    
    for (const id of id_list) {
        warning_list[id].warning.forEach((person)=>{
            warning_list[person].count +=1;
        })
    }
    const block_users = [];
    for (const id of id_list) {
        if (warning_list[id].count >= k)
            block_users.push(id);
    }
    
    var answer = [];
    
    for (const id of id_list) {
        let cnt = 0;
        block_users.forEach((user) => {
            if (warning_list[id].warning.includes(user)){
                cnt += 1;
            }
        })
        answer.push(cnt);
    }
    return answer;
}