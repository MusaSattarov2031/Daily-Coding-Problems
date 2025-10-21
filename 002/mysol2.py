def solution(array):
    SIZE=len(array)
    res=[]
    if SIZE<=1:
        return res
    
    mult=1
    for i in array:
        mult=mult*i
    for i in array:
        res.append(int(mult/i))
    return res

print(solution([1, 2, 3, 4, 5]))
        