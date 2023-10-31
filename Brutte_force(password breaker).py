import random
import pyautogui

chars = "abcdefghijklmnopqrstuvwxyz"
num = "0123456789"
spl = "!@#$%^&*()_+`-=[]{;:}',.<>/?\\|"
full = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+`-=[]{;:}',.<>/?|"

final_chars = list(chars)
final_num = list(num)
final_full = list(full)

pwd = pyautogui.password("Enter a password: ")
sample_pwd = ""

if pwd.isalpha():
    final_set = final_chars
elif pwd.isnumeric():
    final_set = final_num
else:
    final_set = final_full

while sample_pwd != pwd:
    sample_pwd = ''.join(random.choices(final_set, k=len(pwd)))
    print("<------" + sample_pwd + "------>")
    if sample_pwd == pwd:
        print("The password is: " + sample_pwd)
        break
# for i in range(len(pwd)):
#     while sample_pwd != pwd[i]:
#         sample_pwd = ''.join(random.choices(final_set, k=i+1))
#         print("<------" + sample_pwd + "------>")
#     if sample_pwd == pwd:
#         print("The password is: " + sample_pwd)
#         break
