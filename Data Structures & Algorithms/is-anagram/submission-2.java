class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) { 
            return false;
        }

        HashMap<Character, Integer> ana1 = new HashMap<>(); 
        HashMap<Character, Integer> ana2 = new HashMap<>(); 

        for (char i: s.toCharArray()) { 
            ana1.merge(i, 1, Integer::sum);
        }
        for (char j: t.toCharArray()) { 
            ana2.merge(j, 1, Integer::sum);
        }

        return ana1.equals(ana2);



    }
}
