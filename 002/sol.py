def productExceptSelf(nums):
    leftProducts = [1]
    rightProducts = [1]
    for i in range(1, len(nums)):#for [1, 2, 3, 4, 5]
        leftProducts.append(nums[i-1]*leftProducts[i-1])#left will be [1, 1, 2, 6, 24, 120]
        rightProducts.append(nums[-i]*rightProducts[i-1])#right will be [1, 5, 20, 60, 120, 120]
    prods = []
    for i in range(len(nums)):
        prods.append(leftProducts[i]*rightProducts[-1-i])# will be [120, 60, 40, 30, 24]
    return prods

print(productExceptSelf([1, 2, 3, 4, 5])==[120, 60, 40, 30, 24])