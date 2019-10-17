# def is_palindrome(any_string):
#    char_list = []
#    for word in any_string:
#        for char in word: 
#            char_list.append(char)
#         print(char_list)
#     return


char_list = []
any_string = input()
any_string = any_string.replace(" ","")
any_string = any_string.lower()
for word in any_string: 
    for char in word: 
        char_list.append(char)

print(char_list)
reverse_list = char_list[::-1]
print(reverse_list)
if char_list == reverse_list: 
    print(any_string + " is a palindrome")
else:
    print(any_string + " is not a palindrome")

# is_palindrome("Caroline")


def is_palindrome(any_string):
    char_list = []
    any_string = any_string.replace(" ", "")
    any_string = any_string.lower()
    for word in any_string:
        for char in word:
            char_list.append(char)
            
