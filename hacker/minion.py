
'''
Both players are given the same string,S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

THE MINION GAME
'''


def minion(my_str):
    consonant_name = 'stuart'
    vowel_name = 'kevin'
    consonant_words = 0
    vowel_words = 0
    letter_list = list(my_str)
    all_words = []
    l = len(my_str)
    vowel = ['A', 'E', 'I', 'O', 'U']
    consonant = ['Q', 'W', 'R', 'T', 'Y', 'P', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X' 'C', 'V', 'B', 'N', 'M']
    all_words = (letter_list[start:end+1] for start in xrange(l) for end in xrange(start, l))
    for array in all_words:
        if array[0] in vowel:
            vowel_words += 1
        else:
            consonant_words += 1
    if vowel_words > consonant_words:
        print vowel_name, vowel_words
    elif consonant_words > vowel_words:
        print consonant_name, consonant_words
    else:
        print 'draw'

def main():
    my_str = raw_input()
    minion(my_str.upper())

if __name__ == '__main__':
    main()

