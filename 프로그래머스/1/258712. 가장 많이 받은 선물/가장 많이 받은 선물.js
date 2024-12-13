function solution(friends, gifts) {
    // 더 많은 선물을 준 사람이 다음 달에 선물을 받음
    // 선물 기록이 없을 경우 선물 지수가 기준임
    // 선물을 가장 많이 받을 친구가 받을 선물의 수?
    arr = {}
    friends.forEach((person) => {
        arr[person] = {};
        friends.forEach((friend) => {
            if (friend !== person)
                arr[person][friend] = 0;
        })
        arr[person]["giftIndex"] = 0;
        arr[person]["gift"] = 0;
    })
    
    gifts.forEach((gift) => {
        [a, b] = gift.split(' ');
        // a: 선물 준 친구, b: 선물 받은 친구
        arr[a][b] += 1;
        arr[a]["giftIndex"] += 1;
        arr[b]["giftIndex"] -= 1;
    })
    
    // 누가 가장 선물을 많이 받을지?
    friends.forEach((person) => {
        // console.log(arr[person])
        friends.forEach((friend) => {
            if (person !== friend && arr[person][friend] >= 0 && arr[friend][person] >= 0) {
                if (arr[person][friend] > arr[friend][person]) {
                    arr[person].gift += 1;
                } else if (arr[person][friend] == arr[friend][person]) {
                    if (arr[person].giftIndex > arr[friend].giftIndex) {
                        arr[person].gift += 1;
                    } else if (arr[person].giftIndex < arr[friend].giftIndex) {
                        arr[friend].gift += 1;
                    }
                } else {
                    arr[friend].gift += 1;
                }
                arr[person][friend] = -1;
                arr[friend][person] = -1;
            }
        })
        
    })
    
    var answer = 0;
    friends.forEach((friend) => {
        answer = Math.max(answer, arr[friend].gift);
    })
    
    return answer;
}