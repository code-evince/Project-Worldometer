import worldometer
import warnings
# warnings.filterwarnings("ignore")
import sys
import os
import getWorld
# sys.stderr = open(os.devnull,'w')

def main():
    print("-----------------------")
    print("Welcome to Worldometer")
    print("-----------------------")
    exit = 0
    while(exit==0):
        print("1. World Data and queries")
        print("2. Country Data and queries")
        print("3. EXIT")
        user = int(input("Your input : "))
        if(user == 3):
            exit = 1
            continue
        if(user == 1):
            print("MENU")
            print()
            print("1.  Total Cases")
            print("2.  Active Cases")
            print("3.  Total Deaths")
            print("4.  Total Recovered")
            print("5.  Total Tests")
            print("6.  Death/million")
            print("7.  Tests/million")
            print("8.  New Case")
            print("9.  New Death")
            print("10. New Recovered")
            print("11. Main Menu")
            print("12. EXIT")
            country = input("Enter name of the Country")
            ip = int(input("Your input : "))
            if(ip==12):
                exit=1
                continue
            if(ip==11):
                continue
            if(ip >0 and ip<11):
                getWorld.main()


            
        # if(user==2):



    




if __name__ == '__main__':
    main()

# sys.stderr = sys.__stderr__