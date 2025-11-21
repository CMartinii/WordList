import numpy as np

def num_letters(num_rows, num_columns):
    if(num_rows > 2 and num_columns > 2):
        return (num_rows*num_columns - ((num_rows-2)*(num_columns-2)))
    else: return num_rows*num_columns

assert(num_letters(3, 4) == 10)

#loop 1
assert(num_letters(13, 4) == 30)

#loop 2
assert(num_letters(4, 4) == 12)

#loop 3
assert(num_letters(6, 4) == 16)

#loop 4
assert(num_letters(6, 7) == 22)

print("Checking assertions.")


data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')

words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file


words.append((data[0,:]))
words.append((data[1:,columns-1]))
words.append((data[rows-1, columns-2:0:-1]))
words.append((data[rows-1:0:-1, 0]))

words = np.concatenate(words).tolist()

#collect all letters - fill in your code here

print(words) #check that you collected all the letters in your data file
print(len(words))
print(num_letters(rows, columns))
#assert len(words) == num_letters(rows, columns)


words2 = [] #
for element in words:
    if (words.index(element) == len(words) - 1):
        words2.append(element + words[0])
        break 
    element_new = element + words[(words.index(element) + 1)]
    words2.append(element_new)

print(words2)    
