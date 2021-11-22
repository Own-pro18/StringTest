str = input("Enter the string ")
rev = str[::-1]
# for i in str:
#     rev = i+rev
print(rev)
if str.islower()==True or str.isupper()==True:
    print(True)
elif str[0].isupper()==True and str[1:].islower()==True:
    print(True)
else:
    print(False)
