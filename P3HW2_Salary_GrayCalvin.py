# CTI-110
# P3HW2-Salary
# Calvin Gray
# March 23,2023

payrate = float(input("Enter pay rate: "))
hours = float(input("Hours: "))
name = input("Enter Name: ")

if hours > 40:
    regpay = payrate * 40
    ovthrs = hours - 40
    ovtpay = payrate * ovthrs * 1.5
    grosspay = ovtpay + regpay
else:
    regpay = hours * payrate
    grosspay = ovtpay + regpay
print('----------------------------------------------')
print('Employee name:', name)

print()
print("Hours Worked" + " "*5 + "Pay Rate"+ " "*5 +"overtime"+" "*5 +"overtime Pay" + " "*5 + "reghour pay" + " "*5 + "gross pay")
print('----------------------------------------------------------------------------------------------------')

print(hours,'\t\t',payrate,'\t\t'+ '',ovthrs,'\t\t' + ' $' + str(format(ovtpay,',.2f')) + '\t' + ' $'+str(format(regpay,',.2f')) +'\t'+ ' $' + str(format(grosspay,',.2f')))


