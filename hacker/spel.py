"""
print correct words with given characters, must include the control charater in the word.
letter_list = ['r', 'o', 'x', 'i']

control_letter = 'f'
output:
for
fix
fox
.......
"""

import itertools

from multiprocessing import Process, Manager

dictionary_file = '/usr/share/dict/words'

letter_list = ['r', 'o', 'x', 'i']

control_letter = 'f'

manager = Manager()

word_list = manager.list()

def new_combination(i, dictionary):
    global new_combination
    comb_list = itertools.permutations(letter_list, i)
    for item in comb_list:
        item = ''.join(item)
        if item in dictionary:
            word_list.append(item)

def read_dictionary():
    my_list = []
    for word in open(dictionary_file):
        if control_letter in word:
            if(len(word) >2 and len(word)<6):
                my_list.append(word)
    return my_list


def main():
    dictionary = read_dictionary()
    all_processes = []
    for j in range(9,10):
        new_combo = Process(target = new_combination, args = (j,dictionary))
        new_combo.start()
        all_processes.append(new_combo)
    while all_processes:
        for process in all_processes:
            process.join()

    print list(set(word_list))

if __name__ == '__main__':
    main()

    
