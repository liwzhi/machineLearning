package leetcodeJavaSolution;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class combinationSum {
	public List<List<Integer>> combinationSum(int[] candidates,int target){
		List<List<Integer>> result = new ArrayList<List<Integer>>();
		List<Integer> stk = new ArrayList<Integer>();
		int start = 0;
		Arrays.sort(candidates);
		helper(candidates,result,stk,target, start);
		return result;
	}

	private List<List<Integer>> helper(int[] candidates, List<List<Integer>> result, List<Integer> stk, int target, int start) {
		// TODO Auto-generated method stub
		if(sum(stk)==target){
			Collections.sort(stk);
			if (!result.contains(stk)){
			result.add(new ArrayList<Integer>(stk));}
			return result;
		}
		for(int i =start;i<candidates.length;i++){
		    int item = candidates[i];
		    if(item<=target && sum(stk)<target){
		        stk.add(item);
		        helper(candidates,result,stk,target,i);
		        stk.remove(stk.size()-1);
		        
		    }
		}

		
		return result;
		
	}
	
	public int sum(List<Integer> stk){
		int result = 0;
		for(Integer i:stk){
			result+=i;
		}
		return result;
	}	
}
