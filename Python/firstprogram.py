pin_num=1234
balance=10000
print("Wel come to SBI ATM")
pin=int(input("Enter your pin number"))
if pin==pin_num:
  print("Wel come Ranjit kumar rout")
  print("Select the options")
  print("1 : Withdral money and 2 : Check balance")
options=int(input("chose your option"))
if options==1:
 withdrawl=int(input("Enter the mokney to withdral"))
 if withdrawl<=balance:
  print("withdrawl sucessfully")
 else:
   print("insufficient balance")
else:
 print("ok")
else:
print("invalid otp")

    






