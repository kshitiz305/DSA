def palindrome(string_a,index):
    if index > len(string_a)//2:
        return True
    if string_a[index]!= string_a[len(string_a) - index - 1]:
        return False
    return palindrome(string_a,index+1)


print(palindrome('ab',0))