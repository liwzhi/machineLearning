package leetcodeJavaSolution;

public class JumpGameTwo {
	public int jump(int[] nums){
		int step = 0;
		if(nums==null){
			return 0;
		}
		int pre = nums[0];
		for(int i=0;i<nums.length;i++){
			int curr = nums[i];
			if(curr<=pre-1 || i == nums.length-1){
				curr = pre;
			}else{
				step+=1;
				System.out.println(nums[i]);
			}
			pre = curr;
			
		}
		return step;
		
	}

}
