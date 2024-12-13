function solution(video_len, pos, op_start, op_end, commands) {
    // video_len: 총 비디오 길이
    // pos: 현재 비디오 위치
    // op_start, op_end: 오프닝
    // commands: 사용자 명령어
    let currentTime = changeSeconds(pos);
    currentTime = checkOpeningTime(currentTime, op_start, op_end);
    
    for (const command of commands) {
        if (command == "prev") {
            currentTime = prev(currentTime, op_start, op_end);
        } else if (command == "next") {
            currentTime = next(currentTime, video_len, op_start, op_end);
        }
    }
    let min = String(Math.floor(currentTime / 60));
    let sec = String(currentTime % 60);
    min = min.padStart(2, "0");
    sec = sec.padStart(2, "0");
    return `${min}:${sec}`;
}

// 문자열 pos(분:초)을 초로 변환하는 함수
function changeSeconds(pos) {
    let [min, sec] = pos.split(":");
    min = Number(min);
    sec = Number(sec);
    return min * 60 + sec;
}

// 명령어에 따른 현재 시간 조정
function prev(currentTime, op_start, op_end) {
    currentTime < 10 ? currentTime = 0 : currentTime -= 10;
    return checkOpeningTime(currentTime, op_start, op_end)
}

function next(currentTime, video_len, op_start, op_end) {
    const videoTime = changeSeconds(video_len);
    currentTime += 10;
    currentTime > videoTime ? currentTime = videoTime : currentTime;
    return checkOpeningTime(currentTime, op_start, op_end)
}

function checkOpeningTime(currentTime, op_start, op_end) {
    const startingTime = changeSeconds(op_start);
    const endingTime = changeSeconds(op_end);
    if (startingTime <= currentTime && currentTime <= endingTime){
        currentTime = endingTime;
    }
    
    return currentTime;
}