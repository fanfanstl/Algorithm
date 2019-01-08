# 时间复杂度为O(n**2)


# 冒泡排序法
# def dubble_sort(lists):
#     for i in range(len(lists)):
#         for j in range(i+1,len(lists)):
#             if lists[i] > lists[j]:
#                 lists[i], lists[j] = lists[j], lists[i]
#     return lists
# lists = [1,8,5,4,6,6,3]
# print(dubble_sort(lists))

# 选择排序
# def select_sort(lists):
#     for i in range(len(lists)):
#         min = i
#         for j in range(i+1, len(lists)):
#             if lists[i] > lists[j]:
#                 min = j
#         if min != i:
#             lists[i], lists[min] = lists[min],lists[i]
#     return lists
# lists = [1,8,5,4,6,6,3]
# print(select_sort(lists))

# 桶排序
# def bucket_sort(lists):
#     new_lists = ['*'] * (max(lists) + 1)
#     for item in lists:
#         new_lists[item] = item
#     return [x for x in new_lists if x != '*']
#
# lists = [1,8,5,4,6,6,3]
# print(bucket_sort(lists))

# 插入排序
# def insert_sort(lists):
#     for i in range(len(lists)):
#         for j in range(i, 0, -1):
#             if lists[j] < lists[j-1]:
#                 lists[j],lists[j-1] = lists[j-1], lists[j]
#             else:
#                 break
#     return lists
# lists = [1,8,5,4,6,6,3]
# print(insert_sort(lists))


# 时间复杂度为O(nlogn)
# 快速排序法
# def quick_sort(lists):
#     if (len(lists) == 0) or (len(lists) == 1):
#         return lists
#     tem = lists.pop()
#     less = []
#     greater = []
#     for item in lists:
#         if item > tem:
#             greater.append(item)
#         else:
#             less.append(item)
#     return quick_sort(less) + [tem] + quick_sort(greater)
#
#
# lists = [1,8,5,4,6,6,3]
# print(quick_sort(lists))



