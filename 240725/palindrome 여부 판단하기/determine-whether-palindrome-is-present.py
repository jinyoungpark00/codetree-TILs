a = input()

def is_palindrome(a):
    for i in range(len(a) // 2):
        left = a[i]
        right = a[-i]
        if left != right:
            return False
    return True

if is_palindrome(a):
    print("Yes")
else:
    print("No")