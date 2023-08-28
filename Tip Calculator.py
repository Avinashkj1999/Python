total_amount=float(input("Enter total of bill \n =>"))
number_of_persons=int(input("Enter number of person to Share the bill \n =>"))
tip_percentage=int(input("Enter the tip percentage you want to give \n"))

total_amount_with_tip=total_amount*((100+tip_percentage)/100)
Shared_amount=total_amount_with_tip/number_of_persons
print(Shared_amount)