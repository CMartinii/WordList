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
