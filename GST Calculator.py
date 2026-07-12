name=input('Enter your Name: ')
print(f"Hello, Welcome {name} ! , Here's the program to calculate GST and total price")
price=float(input ("Enter the Price of item: "))
quantity=float(input ("Enter the Quantity of item bought: "))
gst=float(input("Enter the GST percentage"))
subtotal=price*quantity
gstamt=(subtotal*gst)/100
total=subtotal+gstamt
print(f'The Subtotal is : {subtotal}')
print(f'The GST is: Rs. {gstamt:.2f}')
print(f'The total cost is: Rs. {total:.2f}')
d=input('Do you have a discount coupon? (y/n)')
if d=='y':
    s=int(input("Enter the discount percentage: "))
    dis=(total*s)/100
    print(f"The Final cost after discount is :{total-dis:.2f}")
else:
    print(f'Okay,Your Final cost is :{total:.2f}')



print(f'THANK YOU {name} for using our software and have a good day ahead!')
