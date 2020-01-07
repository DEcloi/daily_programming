def Palindrome(num):
    if num % 10 == 0 or num < 0:
        return False

    remain = 0
    while num > remain:
        remain = remain * 10 + num % 10
        num //= 10

    return num == remain or num == remain//10


num = 123210
print(Palindrome(num))
