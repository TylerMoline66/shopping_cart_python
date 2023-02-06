def check_num(thingy):

  if thingy.isnumeric() == True:
    thingy = int(thingy)
    return thingy
    
  else:
    print('\n-------> USE A NUMBER <--------')