import subprocess

def main():
    requirements = "pip install nltk; pip install datetime; pip install PLY"
    subprocess.run(requirements, shell=True)
    print("____________________________________________________________________________________________________________________________")
    print("____________________________________________________________________________________________________________________________")
    print('\n\n\n')

    print("################################################################")
    print("                        PROJECT COVID-19                        ")
    print("----------------------------------------------------------------")
    print("    BY - Ayush Shakya | Bishnu Prasad Nayak | Chaitanya Kale    ")
    print("         (23CS60R26)  |     (23CS60R28)     |  (23CS60R29)      ")
    print("################################################################")
    exit = 0
    while(exit==0):
        print("\n\n################################################################")
        print("++++++++++++++++++++++++++ MAIN MENU +++++++++++++++++++++++++++")
        print("1. Worldometer COVID-19")
        print("2. Wikipedia COVID-19")
        print("3. EXIT")
        try:
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
        except Exception as er:
            print(er)


if __name__ == '__main__':
    main()