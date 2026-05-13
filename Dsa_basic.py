# DSA BASICS
# Date: May 2025

 #starting dsa basics
 
# 1. FIND MAXIMUM VALUE
# Time Complexity: O(n) linear search
def max_num(lst):
    max_value = float("-inf")
    for i in lst:
        if i > max_value:
            max_value = i
    return max_value
 
print("--- Find Max ---")
print(max_num([3, 7, 1, 9, 4, 6]))  #output-->9 
 
 
# ---------------------------------------------
 
# 2. FIND SECOND MAXIMUM VALUE
# Time Complexity: O(n)
def sec_max_value(lst):
    first = float("-inf")
    sec = float("-inf")
    if len(lst) <= 1:
        return None
    for i in lst:
        if i >= first:
            sec = first
            first = i
        elif i < first and i > sec:
            sec = i
        else:
            continue
    return sec
 
print("--- Find 2nd Max ---")
print(sec_max_value([3, 7, 1, 9, 4, 6]))  # output-->7
print(sec_max_value([9, 9, 3, 4]))         # output-->9
print(sec_max_value([5]))                  # output-->None
 
 
# -------------------------------------------------
 
# 3. REVERSE A LIST (Two Pointer)
# Time Complexity: O(n)
def lst_reverse(lst):
    for i in range(len(lst) // 2):
        lst[0 + i], lst[len(lst) - (i + 1)] = lst[len(lst) - (i + 1)], lst[0 + i]  # tough part
    return lst
 
print("--- Reverse List ---")
print(lst_reverse([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # output-->[10, 9, 8, ... 1]
 
 
# --------------------------------------------------------
 
# 4. PALINDROME CHECK (Two Pointer)
# Time Complexity: O(n)
def palindrome(str):
    if len(str) < 2:
        return None
    for i in range(len(str) // 2):
        if str[0 + i] != str[len(str) - (i + 1)]:  # become pretty easy after reverse list logic
            return False
    return True
 
print("\n--- Palindrome Check ---")
print(palindrome("racecar"))  # True
print(palindrome("hello"))    # False
print(palindrome("madam"))    # True
 
 
# ------------------------------------------------------
 
# 5. BINARY SEARCH
# Time Complexity: O(log n)
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
 # first time learning binary search challanged my problem solving and intresting way of searching
def binary_search(lst, target):
    lt = 0
    rt = len(lst) - 1
    mid = (lt + rt) // 2
    f = False
    while lt <= rt:
        if target == lst[mid]:
            f = True
            return mid
        elif target > lst[mid]:
            lt = mid + 1
            mid = (lt + rt) // 2
        elif target < lst[mid]:
            rt = mid - 1
            mid = (lt + rt) // 2
    if f == False:
        return -1
 
print("\n--- Binary Search ---")
print(binary_search(lst, 15))  # output-->14 (index)
print(binary_search(lst, 1))   # output-->0  (index)
print(binary_search(lst, 22))  # output-->-1 (not found)
 
 
# ============================================
 
# 6. BUBBLE SORT
# Time Complexity: O(n²)
#swapping the numbers to sort the number in ascending order
def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst
 
print("\n--- Bubble Sort ---")
print(bubble_sort([64, 25, 12, 22, 11]))  # [11, 12, 22, 25, 64]