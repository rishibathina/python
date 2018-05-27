import random                                                                 
'''
Program to game boggle
'''
'''
Aops list a list of all the words that are considered valid in this game. We need a base list in order to check what words they create are valid or not
'''
def isin_aops_list(word):
   infile = open ('wordlist.txt', 'r')
   content = infile.readlines()
   all_words = []
   #print (content)
   for line in content:
      words = line.strip()
      #print (words)
      all_words.append(words)
   if word in all_words:
      return (True)
   else:
      return(False) 
   infile.close() 

def find_all_coordinates(uppercase_letter):                      
   letterdict = {}                                               
   for x in enumerate(mylist):                                   
      row_number,row = x                                         
      for letter in enumerate(row):                                  
         column_number, col = letter                                 
         #print((row_number,column_number),col)                      
         if col in letterdict:                                       
               letterdict[col].append((row_number,column_number))    
         else:                                                       
               letterdict[col] = [(row_number,column_number)]  
   return (letterdict[uppercase_letter])     

def is_word_above_2_letters(word):
   len_of_word = len(word)  
   if len_of_word > 2:
      return (True) 
   else:
      return (False)                     

def score_boogle(int):
   if int == 3 or int == 4:
      return(1)
   elif int == 5:
      return (2)
   elif int == 6:
      return (3)
   elif int == 7:
      return (5)
   elif int >= 8:
      return (11)
   else:
      print ("Pls enter a valid integer!")

def boggle_body():                                                                    
   word_two = 'hi'   
   second_player_score = 0
   score_dict = {}                                                       
   while word_two != '':                                                      
      word_two = input("So " + str(name_two) + ", what is your word? (Leave blank to quit.) ")
      #if isin_aops_list(word_two) and is_word_above_2_letters(word_two) :
      if isin_aops_list(word_two) and is_word_above_2_letters(word_two) :
         starting_letter = []
         word_len_counter = 1
         stop_execution = False
         for letter in word_two:
            letter = letter.upper()
            if len(starting_letter) == 0:
               starting_letter = find_all_coordinates(letter)
            else:
               for tuple in starting_letter:
                  stop_execution = False
                  #print (starting_letter)
                  #print (letter)
                  #print (tuple)
                  coordinates = find_all_coordinates(letter)
                  for coordinate in coordinates:
                     #print (coordinates)
                     #print (coordinate)
                     x_axis_three, y_axis_three = tuple
                     x_axis_four, y_axis_four = coordinate
                     #x = abs(tuple - coordinate)
                     #x_axis, y_axis = x
                     if abs(x_axis_three - x_axis_four) <= 1 and abs(y_axis_three - y_axis_four) <= 1:
                        #print ('done')
                        word_len_counter = word_len_counter + 1
                        #print (word_len_counter)
                        if word_len_counter == len(word_two):
                           second_player_score = second_player_score + score_boogle(len(word_two))                           
                           print ("That is a valid word!")
                           score_dict[word_two] = score_boogle(len(word_two))
                           starting_letter = coordinates
                           stop_execution = False
                           break
                        else:
                           starting_letter = coordinates
                           stop_execution = False
                           #print ("Oh no!")      
                           break 
                     else:
                        #print ('screwed')
                        stop_execution = True
                        pass
                     #if stop_execution:
                        #break
                  if not stop_execution:
                     break
            if stop_execution:
               print ("This is not a valid word!")
               break
      elif word_two == '':
         print ("Thanks for playing!")
         for key in score_dict:
            value = score_dict.get(key)
            print (key,value)
         break
      else:
         print ("This is not a valid word!")
   print ("So " + str(name_two) + ", your final score is " + str(second_player_score) + ".")



string_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                                 
mylist = [[random.choice(string_letters) for x in range(4)] for y in range(4)]

for row in mylist:                                     
   print (row)                                        

name_two = input ("What is the player's name? ")          
second_player_score = 0

boggle_body()         
'''print ("So " + str(name_one) + ", your score is " + str(first_player_score) + ".")     
print ("So " + str(name_two) + ", your score is " + str(second_player_score) + ".")'''    



