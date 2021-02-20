# random.sample displays data in a list (square brackets and commas).
# Also takes a counts=[x,x] argument which tells Python how many times to print each item.
import random
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50], k=6))

print(random.sample(range(1,51), k=6))


nums = []
for i in range(1,51):
    nums.append(i)
print(random.sample(nums, k=6))