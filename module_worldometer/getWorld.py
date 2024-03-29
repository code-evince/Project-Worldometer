import worldometer
import warnings
import time
warnings.filterwarnings("ignore")
import sys
import os
sys.stderr = open(os.devnull,'w')

def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def write_last_updated_time(file_name):
    try:
        with open(file_name, 'w') as f:
            current_time = get_current_time()
            f.write(current_time)
    except Exception as e:
        print(f"An error occurred while writing last updated time: {str(e)}")



def main():

    world = worldometer.main()


    # Open the file in write mode
    with open(f"cache/world.txt", "w") as file:
        for i in range(len(world)):
            file.write("\t".join(map(str, world[i])) + "\n")
    
    file_name = "lastUpdated.txt"
    write_last_updated_time(file_name)


if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__






