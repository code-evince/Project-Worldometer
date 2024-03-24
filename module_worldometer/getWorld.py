import worldometer
import warnings
warnings.filterwarnings("ignore")
import sys
import os
sys.stderr = open(os.devnull,'w')

def main():

    world = worldometer.main()


    # Open the file in write mode
    with open(f"cache\world.txt", "w") as file:
        # Iterate over the zipped arrays
        for i in range(len(world)):
            file.write("\t".join(map(str, world[i])) + "\n")

if __name__ == '__main__':
    main()

sys.stderr = sys.__stderr__