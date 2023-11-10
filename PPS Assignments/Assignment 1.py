basic_salary=int(input("Enter your basic salary:"))
hra=0.1*basic_salary
TA=0.05*basic_salary
gross_salary=basic_salary+hra+TA
print("Gross Salary is:",gross_salary)
Proffesional_Tax=0.02*gross_salary
net_salary=gross_salary-Proffesional_Tax
print("Your Net Salary is:",net_salary)