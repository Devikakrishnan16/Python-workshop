#for i in range(5):
   # for j in range(i,5):
     #  print("*",end ="")
   # print()
   # first program
import time
nums =[2,5,6,9]
target = 7
start = time.perf_counter()
def sol(nums,target):
    dictionary ={}
    solutions =[]
    for i in range(len(nums)):
        dictionary[nums[i]]=i

    for i in range(len(nums)):
        currentnumber = nums[i]
        remaining = target - currentnumber
        if remaining in dictionary:
            solutions.append((i,dictionary[remaining]))
    return solutions
print(sol(nums,target))
end = time.perf_counter()
print(end-start)
