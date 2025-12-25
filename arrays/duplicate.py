#Given an array of integers, find if the array contains any duplicates.
#Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

def brute_force_duplicate_search(array):
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True
            
    return False

array = [0, 4, 65, 2, 5, 42, 42]
print(brute_force_duplicate_search(array))

