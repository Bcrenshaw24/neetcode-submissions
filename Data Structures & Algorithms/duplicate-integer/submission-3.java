
class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> mem = new HashMap<>(); 

        for (int i = 0; i < nums.length; i++) { 
            if (mem.containsKey(nums[i])) { 
                return true;
            }
            else { 
                mem.put(nums[i], 1);
            }


        }
        return false;

        
    }
}