infile = open ('wordlist.txt', 'r+')
values = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,
          'J':8,'K':5,'L':1,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,
          'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
list_of_sums = []
sum_dict = {}
for line in infile:
   words_in_line = line.split()
   for word in words_in_line:
      total_sum = 0
      word = word.upper()
      for letter in word:
         value = values[letter]
         total_sum += value
      sum_dict[word] = total_sum
print ((max(sum_dict, key=sum_dict.get)).lower())
infile.close()