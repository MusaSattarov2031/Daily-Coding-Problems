#right now can only think about aplying nested for loops but understand that this is insoficient

def solution(arr: list, k: int):
    seen=set()
    for i in arr:
        condidate=k-i
        if condidate in seen:
            return True
        seen.add(i)
            
    return False

arr=input("Enter the list separeted by spaces: ")

array=[int(x) for x in arr.split()]
k=int(input("Enter k: "))
print("True" if solution(array, k) else "False")