class Solution {
public:
    int maxArea(vector<int>& heights) {
      int start =0;
      int end = heights.size()-1;
      int mx=0, area=0;
      while(start<end){
        int h = min(heights[start], heights[end]);
        area= (end-start) * h;
        mx = max(mx, area);
        if(heights[start] < heights[end]) start++;
        else end--;
      }
      return mx;
    }
};
