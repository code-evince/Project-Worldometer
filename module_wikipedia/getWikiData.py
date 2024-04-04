import time
import sys
import os
import subprocess
import warnings
warnings.filterwarnings("ignore")
sys.stderr = open(os.devnull,'w')

months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

def main(ctrl):
    if ctrl == 1:   #get timelines data
        #call wikiparser.runner(name, url)
        # name = with directory path of webpage
        pass
    elif ctrl == 2:     #get reponses data
        pass
    elif ctrl == 3:     #get countries data
        pass
    
    return


if __name__ == '__main__':
    main()
