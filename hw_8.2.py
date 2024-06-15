'hw_8.2'
def is_palindrome(init_string: str) -> bool:
    string_lower = init_string.lower()
    cleared_string = ''.join(char for char in string_lower if char.isalnum())
    return cleared_string == cleared_string[::-1]
    # for char in string_lower:
    #     if char in string.punctuation:
    #         ''.join(char)
    # if string_lower == string_lower[::-1]:
    #     return True
    # else:
    #     return False
    
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4' 
print("ОК - Task2")