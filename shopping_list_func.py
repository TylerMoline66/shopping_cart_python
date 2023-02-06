import check_num

def make_a_shopping_list():
  user_input = input('what would you like to do? (Please use a number): ')
  user_input = check_num.check_num(user_input)

  if user_input == 1:
    with open('shopping_list.txt', 'r') as shopping_list:
      print(shopping_list.read())
  elif user_input == 2:
    while True:
      adding_to_the_list = input('What would you like to add? (R will return you to previous menu): ').title()
      if adding_to_the_list == 'R':
        break
      else:
        with open('shopping_list.txt', 'a') as shopping_list:
          shopping_list.write(f"\n{adding_to_the_list}")
          print(f"\n---> {adding_to_the_list} was added to your shopping list\n")
  elif user_input == 3:
    with open('shopping_list.txt', 'w') as shopping_list:
      print('\n---------- Your shopping list is cleared ----------')
  elif user_input == 4:
    print("\n---------- Goodbye! ----------\n")
    return False
