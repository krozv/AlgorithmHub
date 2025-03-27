const fs = require('fs');
// const input = require("fs").readFileSync("./input.txt").toString().trim();
const input = fs.readFileSync("/dev/stdin").toString().trim();

function solution() {
    const id = input;
    console.log(id + "??!");
}

solution();
module.exports = solution;