def encryption(str1, str2):
    enc_dict = {}
    for i in range(len(str1)):
        if str1[i] not in enc_dict:
            enc_dict[str1[i]] = str2[i]
        elif enc_dict[str1[i]] != str2[i]:
            return False

    return True


str1 = "AAB"
str2 = "FOO"

result = encryption(str1, str2)
print(f"Input: {str1}, {str2}")
print(f"Output: {result}")
