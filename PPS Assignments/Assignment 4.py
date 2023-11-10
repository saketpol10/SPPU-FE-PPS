print("Enter maths marks: ")
maths=int(input())

print("Enter science marks: ")
science=int(input())

print("Enter marathi marks: ")
marathi=int(input())

print("Enter social science marks: ")
social_science=int(input())

print("Enter computer marks: ")
computer=int(input())


total=maths+science+marathi+social_science+computer
print("Total is:",total)

average=(total/5)
print("The average of 5 subjects is:",average)
if average>75:
    print("Distinction and Passed")
elif average<75 and average>60:
    print("First Class and Passed")
elif average<60 and average>50:
    print("Second Class and Passed")
elif average<50 and average>40:
    print("Third Class and Passed")
else:
    print("Fail")