# WAP to find greatest of two Numbers
print('Find Greatest of Two Numbers')
a = int(input('Enter First Number '))
b = int(input('Enter Second Number '))

if (a > b):
 print('First number is greatest')
elif (b > a):
 print('Second number is greatest')
else:
 print('Both numbers are equal')


# WAP to find greatest of three Numbers
print('Find Greatest of Three Numbers')
a = int(input('Enter First Number '))
b = int(input('Enter Second Number '))
c = int(input('Enter Third Number '))

if ((a > b) & (a > c)):
 print('First number is greatest')
elif ((b > a) & (b > c)):
 print('Second number is greatest')
elif ((a == b) & (a > c)):
 print('First and second number are equal and greater than third') 
elif ((b == c) & (b > a)):
 print('Second and third number are equal and greater than first')  
elif ((a == c) & (a > b)):
 print('First and third number are equal and greater than second')
elif (a == b == c):
 print('All three numbers are equal')
else:
 print('Third number is greatest')
