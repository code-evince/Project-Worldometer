import subprocess

def main():
    print("################################################################")
    print("                        PROJECT COVID-19                        ")
    print("----------------------------------------------------------------")
    print("    BY - Ayush Shakya | Bishnu Prasad Nayak | Chaitanya Kale    ")
    print("         (23CS60R26)  |     (23CS60R28)     |  (23CS60R29)      ")
    print("################################################################")
    exit = 0
    while(exit==0):
        print("\n\n++++++++++++++++++++++++++ MAIN MENU +++++++++++++++++++++++++++")
        print("1. Worldometer COVID-19")
        print("2. Wikipedia COVID-19")
        print("3. EXIT")
        user = int(input("\nEnter your choice: "))
        if(user == 3):
            exit = 1
        elif(user == 1):
            cmd = "python3 module_worldometer/menu.py"
            subprocess.run(cmd, shell=True)
            pass
        elif(user == 2):
            cmd = "python3 module_wikipedia/menu2.py"
            subprocess.run(cmd, shell=True)
            pass
        else:
            print('Try Again! Enter the valid choice.')


if __name__ == '__main__':
    main()