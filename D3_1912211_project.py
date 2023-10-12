# name: Wojood Ahmad Alghamdi, E-mail: WALGHAMDI0200.stu@uj.edu.sa, Course number: CCCS 111, Section number: D3
# Assignment Title: Taxation System in America and Australia, date: 18th october 2019, "started 6th oct, 10:21"
#                                                               TAXATION SYSTEM IN AMERICA AND AUSTRALIA
#   this program calculates the taxation depending on the country the user chooses
# greating for the user, these will be printed always
print("\n||******************************||\n    Welcome to Taxation System\n||******************************||")#i used \n to put each in newline
print("The countries in our Taxation system are:\n  1. Australia\n  2. America")
# input from the user, int to make the value an integer
country = int(input("please select your country (choose 1 or 2): "))
#Australia tax paid, i made them constants because the values aren't goint to change
AUSTRALIA_TAX1 = "None"
AUSTRALIA_TAX2 = 0.15
AUSTRALIA_TAX3 = 0.30
AUSTRALIA_TAX4 = 0.37
AUSTRALIA_TAX5 = 0.45
#America tax paid, i made them constants because the values aren't goint to change
AMERICA_TAX1 = 0.10
AMERICA_TAX2 = 0.15
AMERICA_TAX3 = 0.25
AMERICA_TAX4 = 0.28
AMERICA_TAX5 = 0.33
AMERICA_TAX6 = 0.35
# used if-elif-else, to make the program works only if the condtion entered by the users are true
if country == 1: #should only execute if the user choose 1
    print("----------------------------------------\n")
    print("{Welcome to the Taxation System of Australia}\n")
    #inputs from the user
    taxID = input("Please enter your Taxpayer Identfication Number (ITIN): ")
    name = input("\nPlease enter your Full name: ")
    salary = int(input("\nEnter your salary: ")) 
    # nested if
    if salary>=0 and salary<=6000: #interval, could be done in many other ways
        annual= AUSTRALIA_TAX1 # no calculations because the tax here is a str "none"
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '€') #displaying the data entered by the user, i used \ to break the long statement
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", annual)
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >6000 and salary<=37000:
        annual= (salary*AUSTRALIA_TAX2) # calculating the tax-payable by multiplying the salary by the tax
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '€')# end is used to put € at the end of the argument
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="€")#formating data
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >37000 and salary<=80000:
        annual= (salary*AUSTRALIA_TAX3)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '€')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="€")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >80000 and salary<=180000:
        annual= (salary*AUSTRALIA_TAX4)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '€')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="€")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >180000:
        annual= (salary*AUSTRALIA_TAX5)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '€')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="€")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    else: # if the user entered a negative value will execute
        print("\nIncorrect salary value\n   Please try again")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
elif country == 2: #should only execute if the user choose 2, related to the first if
    print("----------------------------------------\n")
    print("{Welcome to the Taxation System of America}\n")
    #inputs from the user
    taxID = input("Please enter your Taxpayer Identfication Number (ITIN): ")
    name = input("\nPlease enter your Full name: ")
    salary = int(input("\nEnter your salary: "))
    if salary>=0 and salary <=8700:
        annual = (salary*AMERICA_TAX1)# calculating the tax-payable by multiplying the salary by the tax
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '$') #displaying the data entered by the user, i used \ to break the long statement
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="$")#formating data
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >8700 and salary<=35350:
        annual = (salary*AMERICA_TAX2)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '$')# end is used to put $ at the end of the argument
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="$")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >35350 and salary<=85650:
        annual = (salary*AMERICA_TAX3)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '$')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="$")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >85650 and salary<=178650:
        annual = (salary*AMERICA_TAX4)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '$')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="$")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >178650 and salary<=388350:
        annual = (salary*AMERICA_TAX5)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '$')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="$")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    elif salary >388350:
        annual = (salary*AMERICA_TAX6)
        print("----------------------------------------","\nwelcome", name, "<3", "\nYour ITIN is:", taxID, "\nYour annual salary is:", \
        salary, end = '$')
        print("\n----------------------------------------\nDear citizen :) Your tax-payable is:", format(annual, ',.2f'), end="$")
        print("\n----------------------------------------","\nThank you for using our Taxation system\n")
    else: # if the user entered a negative value will execute
        print("\nIncorrect salary value\n   Please try again")
else: # if the user entered anything rather than 1 or 2
    print("\nYou should either choose 1 or 2\n\tPlease try again") # executes only if the user intered value doesn't equal 1 or 2 
    print("----------------------------------------\nThank you for using our Taxation stystem")
print("________________________________\n")# will always be printed at the end of the program