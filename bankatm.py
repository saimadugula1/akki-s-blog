print 'python bank'
restart=('Y')
chances = 3
balance = 5000
while chances >= 0:
    pin = int(raw_input('Please Enter You 4 Digit Pin: '))
    if pin == (0000):
        print 'You entered you pin Correctly\n'
        while restart not in ('n','NO','no','N'):
            print ' 1 For Your Balance\n'
            print ' 2 To Make a Withdrawl\n'
            print ' 3 To Pay in\n'
            print ' 4 To Return Card\n'
            option = int(raw_input(''))
            if option == 1:
                print 'Your Balance is Rs',balance,'\n'
                restart = raw_input(' ')
                if restart in ('n','NO','no','N'):
                    print 'Thank You'
                    break
            elif option == 2:
                option2 = ('y')
                withdrawl = float(raw_input(' withdraw? : '))
                if withdrawl in [10, 20, 40, 60, 80, 100]:
                    balance = balance - withdrawl
                    print '\nYour Balance is now Rs',balance
                    restart = raw_input('Would You you like to go back? ')
                    if restart in ('n','NO','no','N'):
                        print 'Thank You'
                        break
                elif withdrawl != [10, 20, 40, 60, 80, 100]:
                    print 'Invalid Amount, Please Re-try\n'
                    restart = ('y')
                elif withdrawl == 1:
                    withdrawl = float(raw_input('Please Enter Desired amount:'))    

            elif option == 3:
                Pay_in = float(raw_input('to paying amount '))
                balance = balance + Pay_in
                print '\nYour Balance is now rs',balance
                restart = raw_input('Would You you like to go back? ')
                if restart in ('n','NO','no','N'):
                    print 'Thank You'
                    break
            elif option == 4:
                print 'Please wait whilst your card is Returned...\n'
                print 'Thank you for you service'
            else:
                print 'Please Enter a correct number. \n'
                restart = ('y')
    elif pin != ('0000'):
        print 'Incorrect Password'
        chances = chances - 1
        if chances == 0:
            print '\nNo more tries'
            break
