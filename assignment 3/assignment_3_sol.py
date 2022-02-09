# This is an empty python file
# where you have to add your code to
# implement a basic countdown timer!
# The ______ library need to be used!
# 
# Good Luck!!!

import time

def timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(f'\r{timer}', end=' ')
        time.sleep(1)
        t -= 1

    print('\rTimer done!!!')

seconds = int(input("Enter number of seconds for timer: "))
timer(seconds) 