class Solution {
public:
    bool canJump(vector<int>& nums) {
        int maxIndex = 0; int final = nums.size()-1;

        for(int i=0; i<nums.size(); i++){
            if(i <= maxIndex){
                maxIndex = max(maxIndex, nums[i] + i);
                if(maxIndex >= final) return true;
            }

        }

        return false;
    }
};
