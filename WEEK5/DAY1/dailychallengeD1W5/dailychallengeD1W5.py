class Python:
    def f1(self, s1):
        return self.f2([], sorted(s1))
    def f2(self, curr, s1):
        if s1:
            return self.f2(curr, s1[1:]) + self.f2(curr + [s1[0]], s1[1:])
        return [curr]


a = []
n = int(input("How many element you want ? "))
for i in range(0, n):
    b = int(input("Enter your number: "))
    a.append(b)
print("Result: ")
print(Python().f1(a))

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result
print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))