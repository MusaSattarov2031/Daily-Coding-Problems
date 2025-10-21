def solution(array):
    left=[1]
    right=[1]

    for i in range(1, len(array)):
        left.append(left[i-1]*array[i-1])
        right.append(right[i-1]*array[-i])

    prod=[]
    for i in range(len(array)):
        prod.append(left[i]*right[-i-1])
    return prod

print(solution([1, 2, 3, 4, 5]))
        