def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False

# Example 
str1 = "abcd"
str2 = "cdab"
result = is_rotation(str1, str2)
print(result)  