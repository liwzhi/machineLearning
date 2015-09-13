class Solution(object):
    def isValid(self,s):
        if len(s) ==0:
            return True
        if len(s)==1:
            return False
        stack = []
        element = set(['(','[','{'])
        sign = 0
        for i in range(len(s)):
            curr = s[i]
            if curr in element:
                stack.append(curr)
            else:
                sign =1
                if len(stack) ==0:
                    sign = 0
                    break
                else:
                    match = stack.pop()
                    if curr==')':
                        if match !='(':
                            sign = 0
                            break
                    if curr =='[':
                        if match!=']':
                            sign = 0
                            break
                    if curr =='}':
                        if match!='{':
                            sign = 0
                            break
        if sign ==1 and len(stack)==0:
            return True
        else:
            return False
        