

nums1 = []
nums2 = [3,5]
nums3 = list()
index = 0

for i in range(len(nums1)+len(nums2)):
    if i < len(nums1):
        nums3.append(nums1[i])
    else:
        nums3.append(nums2[index])
        index  +=1

nums3.sort()
print(nums3)
ortanca = float(len(nums3)/2.0)
medyan = 0.0
print(ortanca)
if ortanca%2 != 0.5:
    medyan = (float(nums3[int(ortanca)]) + float(nums3[int(ortanca) - 1])) / 2.0
else:
    medyan = float(nums3[int(ortanca)])


print(medyan)