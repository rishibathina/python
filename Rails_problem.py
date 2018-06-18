def skip(string, index, number):
    list_of_string = list(string)
    #print (len(list_of_string))
    final_list_of_string = []
    final_list_of_string.append(list_of_string[index])
    number_of_times_skip = (len(list_of_string) - (index + 1)) // number
    if type(number_of_times_skip) is float:
        #print (number_of_times_skip)
        for index_number in range(1,number_of_times_skip+1):
            #print (number_of_times_skip)
            final_list_of_string.append(list_of_string[(index_number * number) + index])
        final_string = ''.join(final_list_of_string)
        return (final_string)
    else:
        #print (number_of_times_skip)
        #print ("I am here")
        for index_number in range(1,number_of_times_skip+1):
            #print (number_of_times_skip)
            final_list_of_string.append(list_of_string[(index_number * number) + index])
        final_string = ''.join(final_list_of_string)
        return (final_string)
def encipher_fence(plaintext,numRails):
    list_of_strings = []
    for number in range(0,numRails):
        #print (skip(plaintext,number,numRails))
        list_of_strings.append(skip(plaintext,number,numRails))
        print (list_of_strings)
    final_list_of_strings = list(reversed(list_of_strings))
    print(final_list_of_strings)
    final_scramble = ''.join(final_list_of_strings)
    print (final_scramble)
print(encipher_fence("This is a test.", 2))
# should print: hsi  etTi sats.
print(encipher_fence("This is a test.", 3))
# should print: iiae.h  ttTss s
print(encipher_fence("Happy birthday to you!", 4))
# should print: pidtopbh ya ty !Hyraou
import math
def decipher_fence(scrambled_text,numRails):
    new_scrambled_text = scrambled_text[::-1]
    #print (new_scrambled_text)
    len_of_scrambled_text = len(scrambled_text)
    len_of_scrambled_text = len(scrambled_text)
    #print (len_of_scrambled_text)           
    orig_longest_length_of_rail = math.ceil(len_of_scrambled_text / numRails)
    #print (orig_longest_length_of_rail)
    longest_length_of_rail = orig_longest_length_of_rail
    first_string = ''            
    x = 0                                                                    
    #print (longest_length_of_rail)    
    while x < len_of_scrambled_text - 1:                
        if longest_length_of_rail > len_of_scrambled_text - 1:
            sub_string = new_scrambled_text[x:len_of_scrambled_text]                              
        else:                                                                                   
            sub_string = new_scrambled_text[x:longest_length_of_rail]
        first_string = first_string + sub_string[::-1]               
        x = x + orig_longest_length_of_rail                                                      
        longest_length_of_rail = longest_length_of_rail + orig_longest_length_of_rail
        #print (first_string)            
    final_string = ''  
    for i in range(0,orig_longest_length_of_rail):    
        index = i                          
        while index < len(first_string):
            final_string = final_string + first_string[index]
            index = index + orig_longest_length_of_rail
    #print (final_string)
    return final_string
def decode_text(scrambled_text,wordfilename):
    inputFile = open('wordlist.txt','r')
    wordlist = inputFile.readlines()
    all_words = []
    #print (content)
    for line in wordlist:
        words = line.strip()
        #print (words)
        all_words.append(words)
    inputFile.close()
    len_of_scrambled_text = len(scrambled_text)
    for numRails in range(1,len_of_scrambled_text):
        first_string = decipher_fence(scrambled_text,numRails)
        first_list = first_string.split()
        for word in first_list:
            if word in all_words:
                stop_execution = True
                pass
            else:
                stop_execution = False
                break
        if stop_execution == True:
            break
        else:
            pass
    final_string = ' '.join(first_list)
    return (final_string)
print(decode_text(" cr  pvtl eibnxmo  yghu wou rezotqkofjsehad", 'wordlist.txt'))
# should print: the quick brown fox jumps over the lazy dog
		
        
        