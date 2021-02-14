class Solution(object):
    def nextGreaterElements(self, A):
        stack, res = [], [-1] * len(A)
        list1 =[i for i in range(len(A))]
        list2 = list1 + list1
        for i in list2:
            while stack and (A[stack[-1]] < A[i]):
                res[stack.pop()] = A[i]
            stack.append(i)
        return res

