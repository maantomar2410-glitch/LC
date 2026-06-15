def hh(nums,k):
        limit = k + 1
        if len(nums) < limit:
            limit = len(nums)
        check={}
        for i in range(limit):
                if(nums[i] in check):
                    return True
                else:
                    check[nums[i]]=1
        for i in range(len(nums)-k-1):
                del check[nums[i]]
                if(nums[k+i+1] in check):
                    return True
                else:
                    check[nums[k+i+1]]=1
        return False
