# put your code here.


def word_count(file_name):
    """Program that takes a text file, counts how many 
    occurances of each individual word, and the print
    the word and it's word count."""
    
    # open a file
    the_file = open(file_name)
    word_count_dictionary = {}

    # iterate over the file
    for line in the_file:
        # iterate over each line
        for word in line.split():
            # count repeats
            if word in word_count_dictionary:
                word_count_dictionary[word] = word_count_dictionary[word] + 1
            else:
                 # add a new word to the dictionary
                word_count_dictionary[word] =  1

    for tup in word_count_dictionary.iteritems():
        print "%s: %d" %(tup[0], tup[1])        

    # print word_count_dictionary
            

    
    
   
    
    # print dictionary

word_count("test.txt")