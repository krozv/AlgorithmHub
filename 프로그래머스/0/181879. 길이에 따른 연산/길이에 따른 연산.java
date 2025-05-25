class Solution {
    public int solution(int[] num_list) {
        int answer = num_list[0];
        if (num_list.length >= 11){
            for (int i=0; i<num_list.length; i++){
                if (i != 0)
                    answer += num_list[i];
            }
        } else {
            for (int i=0; i<num_list.length; i++){
                if (i != 0)
                    answer *= num_list[i];
            }
        }

        return answer;
    }
}