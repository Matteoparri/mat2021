'''
--- Goal
Write a Python program that prints the relative frequence of each letter
of the alphabet (without distinguishing between lower and upper case) in the
book.


'''

import string
import time
import argparse
import numpy as np
import matplotlib.pyplot as plt



'''
Use argparse of assign --help for help of the program.
'''


parser=argparse.ArgumentParser(
    description='''This program returns the frequency of every letter of the alphabet inside a book.txt given in input. Please make sure the txt is in the same folder as this program and make sure you write 'name.txt'as input. ''',
    epilog="""All is well that ends well.""")

args=parser.parse_args()


#The user inserts the input
user_path = input('Insert input file:')

plato_file = open(user_path,'r')
plato =plato_file.read()


#Start the clock

start_time = time.time()

#Convert to lower for ascii reasons to count both maiusc and minusc.

low_plato=plato.lower()

#Create a list of ascii string lowercase.
alphabet_string = string.ascii_lowercase

#And this results in an alphabet
alpha_list = list(alphabet_string)


'''
alpha_manual=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''

##########COUNTING##########

'''
We use the .count function of strings to count number of occurrencies. It  outputs a number.
low_plato.count('a'))
'''
#print(len(alpha_manual))
#print(len(alpha_list))

#we create an empty list to store the number of each.
freq=[]

for item in alpha_list:
    freq.append(low_plato.count(item))


for i in range(len(alpha_list)):
    x=alpha_list[i]
    y=freq[i]
    print(f'Frequency of {x} is {y}' )

print("Runtime--- %s seconds ---" % (time.time() - start_time))



ans = input('Do you want to show the histograms? Input yes or no:')

if ans == 'yes':
    y = freq
    x = alpha_list
    plt.bar(x,y)
    g = user_path
    plt.title(f'Histogram of frequencies of letters for {g}')
    plt.show()

else:
    print('Alright, have a good day')


