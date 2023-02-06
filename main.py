import shopping_list_func
count = 0
list_of_options = ['Print', 'Add', 'Clear', 'Quit']


while True:
  if count == 0:
    print('\nWelcome to the shopping list program! below are your options')
    count += 1
  else:
    print('\n----------')
    for i, option in enumerate(list_of_options, 1):
      print(f"{i}. {option}")
    print('----------\n')

    if shopping_list_func.make_a_shopping_list() == False:
      break
  