def binary_pal(n):
    str_bin = "{0:b}".format(n)
    backward_bin = ''
    
    for i in range(1, len(str_bin) + 1):
        index = -i
        backward_bin += str_bin[index]
    
    if str_bin == backward_bin: return True
    else: return False
    

# TEST CASES 👇

binary_pal(0) # returns True

binary_pal(5) # returns True

binary_pal(7) # returns True

binary_pal(10) # returns False

binary_pal(15) # returns True

binary_pal(20) # returns False

binary_pal(21) # returns False