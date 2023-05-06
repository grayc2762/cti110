# CTI-110
# P4HW1-Score List
# Calvin Gray
# April 6 2023

num = int(input("How many scores? "))
total = 0
for i in range(0,num):
    grade = float(input ("Grade: "))
    total = grade + total
     
average = total / num
print(average)
if average >= 90:
    print("grade is A")
elif average >=80:
    print("grade is B")
elif average >=70:
    print("grade is C")
elif average >=60:
    print("grade is D")
else:
    print("grade is F")
      

