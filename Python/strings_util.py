
def reverse_string(s):
    s[::-1]
    print("0")
    return s[::-1]

def palindrome(strn):
    return strn == strn[::-1]
    # for i in range(len(strn)//2):
    #     if(strn[i] != strn[len(strn)-i]):
    #         print(f"{strn[i]}  -  {strn[len(strn) - i-1]} ")
    #         return "Not a Palindrome"
        
    # return "Palindrome"

def concatenate(str1, str2):
    return str1 + " " + str2

def str_len(str1):
    return len(str1)


print(palindrome("Rohit"))

