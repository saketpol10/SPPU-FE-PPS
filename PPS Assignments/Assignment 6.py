def str_len(str):
    len=0
    for i in str:
        len=len+1
    return len

def str_rev(str):
    return str[::-1]

def str_cmp(str1,str2):
    if(str1==str2):
        return True
    else:
        return False

def is_pallindrome(str):
    rev=str_rev(str)

    if(str==rev):
        return True
    return False

def is_substr(str1,str2):
    if(str1.find(str2)==-1):
        return -1
    else:
        position=str1.find(str2)
        return position

while(True):

     print("Main Menu")
     print("1.Calculate length of string")
     print("2.String Reversal")
     print("3.Equality check of two strings")
     print("4.Check for Pallindrome")
     print("5.Check Substring")
     print("6.Exit")
     print("Enter your choice")
     choice=int(input())

     if choice==1:
         print("Enter some string:")
         str=input()
         print("Length of String ",str,"is",str_len(str))
     elif choice==2:
         print("Enter some string:")
         str = input()
         print("Reversal of string ",str,"is",str_rev(str))
     elif choice == 3:
         print("Enter first string:")
         str1 = input()
         print("Enter second string:")
         str2 = input()
         if(str_cmp(str1,str2)):
             print("Two strings are equal")
         else:
             print("Two strings are not equal")
     elif choice == 4:
         print("Enter some string:")
         str = input()
         if(is_pallindrome(str)):
             print("String ",str,"is pallindrome")
         else:
             print("String ", str, "is not pallindrome")
     elif choice == 5:
         print("Enter some string:")
         str1 = input()
         print("Enter some substring")
         str2 = input()
         if((is_substr(str1,str2))<0):
             print("String ",str2,"is not a substring of:",str1)
         else:
             print("The Substring is found at position:",is_substr(str1,str2))

     else:
         print("Exiting")
         break;







