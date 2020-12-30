# a loop of 3Sum and 2Sum
class Solution:
    def fourSum(nums,target=0):
        nums = sorted(nums)
        ans = []
        for i in range(len(nums)):
            target1 = target - nums[i]
            # print(target1)
            for j in range(i+1,len(nums)):
                target2 = target1 - nums[j]
                hashmap = {}
                for k in range(j+1,len(nums)):
                    if nums[k] in hashmap:
                        solut = [nums[i],nums[j],nums[hashmap[nums[k]]],nums[k]]
              #          print(solut)
                        if solut not in ans:
                            ans.append(solut)
                        print(ans)
                #it is also fine to write [hashmap[nums[i]],i] here, I don't know the reason
                    else:
                        hashmap[target2 - nums[k]] = k
        return ans

a = Solution.fourSum([1,0,-1,0,-2,2])
print(a)
