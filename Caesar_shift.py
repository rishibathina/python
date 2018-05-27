def caesar_shift(starting_word,key_number):
    key_number = int(key_number)
    starting_word_list = list(starting_word)
    print (starting_word_list)
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    final_word_list = []
    final_word = ''
    for letter in starting_word_list:
        #print (letter)
        for element in alphabet_list:
            #print (element)
            if element is letter:
                x = alphabet_list.index(element)
                print (x)
                y = x + (key_number)
                #print (x)
                #print (y)
                final_word_list.append(alphabet_list[y])
                break
            else:
                pass
    final_word = ''.join(final_word_list)
    return final_word

caesar_shift('python',2)