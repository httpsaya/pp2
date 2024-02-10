def polindrome(st):
    length = len(st)
    for i in range(0, len(st)//2):
        if st[i] == st[length - i - 1]:
            return True
    return False    

st = str(input())
print(polindrome(st))