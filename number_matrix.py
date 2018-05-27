inFile = open('number_matrix', 'r')                                                                                                                                         
#list of products for me to maxamize 
list_of_products = []                                                                                                                  
column = []                               #column's list for products                                                                                                       
number_of_iterations = 0
for line in inFile:                       #iterate throught file line by line                                                                                               
   mystring = line                       #convertingline into string                                                                                                       
   mylist = mystring.split()             #splitting the string into individual list indexes                                                                                
   #print (len(mylist))                                                                                                                                                    
   #print (x)                                                                                                                                                              
   row_counter = 0                       #value of indexing                                                                                                                
   while row_counter < 17:               #to index and not over index and to loop through the values over and over again
      #find all possible products
      product_of_numbers = int(mylist[row_counter])*int(mylist[row_counter+1])*int(mylist[row_counter+2])*int(mylist[row_counter+3])                                                 
      list_of_products.append( (product_of_numbers,"row",int(mylist[row_counter]),int(mylist[row_counter+1]),int(mylist[row_counter+2]),int(mylist[row_counter+3])))
      #increase index to allow for all products and so that we don't have a infinite loop                                                                                                                                                                                
      row_counter = row_counter + 1
   number_of_iterations += 1                                                    
#print (max(list_of_products))                                                                                                                                              
inFile.seek(0)                            #bring cursor back to the first line
column_counter = 0 
                                    #indexing for columns    
for number in range(0,number_of_iterations):
    #print (number)
    for line in inFile:                       #iterate through the file line by line
        newstring = line                      #convert line to string
        #print (newstring)
        newlist = newstring.split()           #convert string to list
        #print(newlist[int(number)])
        #print ()                                                                                              
        column.append(newlist[int(number)])             #add first index to the column list to find all possible products
        #print (len(column))                                                                             
        #print (y)                             #debug                                                     
        #print (len(column))                    #debug   
    #print (column)                                                                                                                          
    column_counter = 0 
    while column_counter < 17: #to index and not over index and to loop through the values over and over again  
        #find all possible products                                  
        #print (column_counter)
        product_of_numbers = int(column[column_counter])*int(column[column_counter+1])*int(column[column_counter+2])*int(column[column_counter+3])
        list_of_products.append((product_of_numbers, "col", int(column[column_counter]), int(column[column_counter+1]), int(column[column_counter+2]), int(column[column_counter+3]) ))               
        #increment by one to keep a finite loop 
        column_counter = column_counter + 1    
    column = []
    inFile.seek(0)                             
#print ((column))                          #debug      
print (list_of_products)
print (max(list_of_products))             #max product