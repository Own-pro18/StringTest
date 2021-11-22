str = input("Enter the string ")
rev = str[::-1]
# for i in str:
#     rev = i+rev
def str_test():
    print(rev)
    if str.islower()==True or str.isupper()==True:
        return True
    elif str[0].isupper()==True and str[1:].islower()==True:
        return True
    else:
        return False

if __name__ == '__main__':
    print(str_test())
