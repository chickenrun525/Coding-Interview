class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        int length = s.length();
        boolean[] f = new boolean[length+1];
        f[0] = true;
        for (int i = 1; i < length+1; i++) {
            for (int j = 0; j < i; j++) {
                if (f[j] && wordDict.contains(s.substring(j,i))) {
                    f[i] = true;
                    break;
                }
            }
        }
        return f[length];
    }
}