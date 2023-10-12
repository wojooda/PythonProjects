# name: Wojood Ahmad Alghamdi, E-mail: WALGHAMDI0200.stu@uj.edu.sa, Course number: CCCS 111, Section number: D3ِ
# Assignment Title: Taxation System in America and Australia, date: th  2019, "started 29th oct, 4:36 PM"
#                                                               TAXATION SYSTEM IN AMERICA AND AUSTRALIA
def main(): # defining the main function
    print("\n||******************************||\n    Welcome to Taxation System\n||******************************||")#i used \n to put each in newline    
    DisplayMenu() # calling the DisPlayMenu function, to display and take input from the user
    choice = input("please Enter your choice (A or B or C): ") # take input from the user
    while choice!='A' and choice!='a' and choice!='B' and choice!='b' and choice!='C' and choice!='c': # will stop only if choice doesn't equal abc
        print('-'*30, "\nwrong entry! \nyou should enter A for America, B for Australia, C for Exit \nTry again\n"  )
        DisplayMenu() # calling the DisPlayMenu function again, to display and take input from the user untill it follows the directions
        choice = input("please Enter your choice (A or B or C): ") # take input from the user again
    while choice=='A' or choice=='a' or choice=='B' or choice=='b':
        if choice=='A' or choice=='a':
            print('-'*30) # printing it 30 times
            itin = input("\nEnter your Individual Taxpayer Identification Number (ITIN): ") # take input from the user
            Itin = isValidITIN(itin) # calling the isValidITIN function, to test the entered value, Itin variable is to store the boolean value
            while Itin==False: # will stop only if Itin doesn't equal False
                print("Wrong entry, your ITIN doesn't follow the rules. \nplease try again\n")
                itin = input("Enter your Individual Taxpayer Identification Number (ITIN): ") #keep asking the user until they enter the right value
                Itin = isValidITIN(itin) # calling the function again to test the entered value
            if Itin==True: # will execute if the Itin equals true
                name = input("\nPlease enter your Full name: ") # take input from the user
                salary = float(input("\nEnter your salary: ")) # take input from the user and make it int
                while salary<0: # if the user entered a negative value will execute
                    print('-'*30, '\nIncorrect salary value\n   Please try again\n', '-'*30)
                    salary = float(input("\nEnter your salary: ")) #keep asking the user until they enter the right value
                if salary>=0:
                    tax = USTaxPaid(salary) # call the USTaxPaid function to determine the tax based on the entered salary value
                total = CalculateTax(salary, tax) # calling the CalculateTax function to make caculations
            print('-'*30,'\nThe entered data:','\nFull name:', name, '<3', '\nYour ITIN is:', itin, "\nyour annual salary is: ", salary\
                ,'\n', '-'*30, "\nThe citizen's Tax-payable amount is: ", format(total, ',.1f'), end = '$') #displaying the data entered by the user # i used \ to break the long statement
            WriteToFile(name, itin, salary, total) # writing data entered by user to the file
            DisplayMenu() # calling the DisPlayMenu function again, to display and take input from the user untill it follows the directions
            choice = input("please Enter your choice (A or B or C): ") # take input from the user again
            while choice!='A' and choice!='a' and choice!='B' and choice!='b' and choice!='C' and choice!='c': # will stop only if choice doesn't equal abc
                print('-'*30, "\nwrong entry! \nyou should enter A for America, B for Australia, C for Exit \nTry again\n"  )
                DisplayMenu() # calling the DisPlayMenu function again, to display and take input from the user untill it follows the directions
                choice = input("please Enter your choice (A or B or C): ") # take input from the user again
        elif choice=='B' or choice=='b':
            print('-'*30) # printing it 30 times
            tfn = input("Enter your Tax File Number (TFN): ") # take input from the user
            TfN = isValidTFN(tfn) # calling the isValidTFN function, to test the entered value, TfN variable is to store the boolean value
            while TfN==False: # will stop only if TfN doesn't equal False
                print("wrong entry, TFN must be 9 digits\npleases try again\n")
                tfn = input("Enter your Tax File Number (TFN): ") #keep asking the user until they enter the right value
                TfN = isValidTFN(tfn) # calling the function again to test the entered value
            if TfN==True: # will execute if the TfN equals true
                name = input("\nPlease enter your Full name: ") # take input from the user
                salary = float(input("\nEnter your salary: ")) # take input from the user
                while salary<0: # if the user entered a negative value will execute
                    print('\nIncorrect salary value\n   Please try again\n', '-'*30)
                    salary = float(input("\nEnter your salary: ")) # take input from the user
                if salary>=0:
                    tax = AUTaxPaid(salary)  # call the AUTaxPaid function to determine the tax based on the entered salary value
                total = CalculateTax(salary, tax) # calling the CalculateTax function to make caculations
                print('-'*30,'\nThe entered data:','\nFull name:', name, '<3', '\nYour ITIN is:', tfn, "\nyour annual salary is: ", salary\
                    ,'\n', '-'*30, "\nThe citizen's Tax-payable amount is: ", format(total, ',.1f'), end = '€') #displaying the data entered by the user, i used \ to break the long statement
            WriteToFile(name, tfn, salary, total) # writing data entered by user to the file
            DisplayMenu() # calling the DisPlayMenu function again, to display and take input from the user untill it follows the directions
            choice = input("please Enter your choice (A or B or C): ") # take input from the user again
            while choice!='A' and choice!='a' and choice!='B' and choice!='b' and choice!='C' and choice!='c': # will stop only if choice doesn't equal abc
                print('-'*30, "\nwrong entry! \nyou should enter A for America, B for Australia, C for Exit \nTry again\n"  )
                DisplayMenu() # calling the DisPlayMenu function again, to display and take input from the user untill it follows the directions
                choice = input("please Enter your choice (A or B or C): ") # take input from the user again
        elif choice=='C' or choice=='c':
            print('-'*30,"\nYou've choosen to end the program\n",'-'*30, "\nThank you for using our Taxation system <3") # ending the program
# def fun(parameter), fun(argument) incorrect
def DisplayMenu():
    print("\n||********** MENU **************||\nThe countries in our Taxation system are:\n  A. America\n  B. Australia\n  C. Exit" \
        ,"||******************************||") # ABC not 123, \n to put each in newline

def isValidITIN(itin):
    if len(itin)!=9 or itin[0]!='9' or int(itin[3:5])<70 or int(itin[3:5])>99 or int(itin[3:5])==93 or int(itin[3:5])==89:
        return False # boolean value
    elif len(itin)==9 or itin[0]=='9'or int(itin[3:5])>=70  or int(itin[3:5])<=99  or int(itin[3:5])!=93 or int(itin[3:5])!=89:
        return True # boolean value

def isValidTFN(tfn):
    if len(tfn)!=9:
        return False # boolean value
    elif len(tfn)==9:
        return True # boolean value

def USTaxPaid(salary):
    if salary>=0 and salary <=8700:
        return 0.10
    elif salary >8700 and salary<=35350:
        return 0.15
    elif salary >35350 and salary<=85650:
        return 0.25
    elif salary >85650 and salary<=178650:
        return 0.28
    elif salary >178650 and salary<=388350:
        return 0.33
    elif salary >388350:
        return 0.35

def AUTaxPaid(salary):
    if salary>=0 and salary<=6000:
        return 0
    elif salary >6000 and salary<=37000:
        return 0.15
    elif salary >37000 and salary<=80000:
        return 0.30
    elif salary >80000 and salary<=180000:
        return 0.37
    elif salary >180000:
        return 0.45

def CalculateTax(salary, tax):
    result = salary*tax # calculating 
    return result

def WriteToFile(FullName, Id, salary, tax):
    taxfile = open('TaxPayableReport.txt', 'a') # opening a file in append mode
    taxfile.write(FullName +'\n')
    taxfile.write( Id +'\n')
    taxfile.write(str(salary) +'\n') # write only acceptet str
    taxfile.write(str(tax) +'\n') # write only acceptet str
    taxfile.close() # closing the file
    print("\nthe citizen's records has been inserted\n", '-'*30)

main() #calling the main function