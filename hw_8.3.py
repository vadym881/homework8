'hw_8.3'
def find_unique_value(some_list: list):
    frequency = {}
    for num in some_list:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    for num, count in frequency.items():
        if count == 1:
            return num

assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1' 
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2' 
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3' 
print("ОК - Task3")