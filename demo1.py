
total =10000
balance= 0
Pin=1234
name =input('''Hello User!!!
enter your name please : ''')

if(name =='preeti'):
  print(f"welcome to SBI bank {name}" )
  print('enter your pin please:')
  if(pin==pin):
     amount=int(input('enter the amount to withdraw : '))
    if(amount>10000):
        print('Transaction failed! Insufficient balance')
        print('Enter a correct amount ')
    elif(amount<=10000):
        balance =total-amount
        print("transaction successful")
        print(f'collect your cash :{amount}')
        print(f'your Bank balance is : {balance}/-')
        print('Thank you')
  else:
        print('Invalid Pin')
        print('enter valid Pin')

else:
    print('invalid user')
    print('please enter the valid user name')