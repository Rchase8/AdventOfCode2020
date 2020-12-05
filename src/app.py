def get_number_list():
  file = open("Data/1_1inputs.txt", "r")
  lines = file.readlines()

  new_numberlist = []
  for line in lines:
    new_numberlist.append(int(line))

  return new_numberlist
# block ends

def filter_number_list(the_numberlist, criteria_def):
  for first_pos in range(0,len(the_numberlist)):
    for second_pos in range(0,len(the_numberlist)):
      if first_pos == second_pos:
        continue

      first_number = the_numberlist[first_pos]
      second_number = the_numberlist[second_pos]




      print(first_number, second_number)
      pass
  pass
# block ends

def is_sum_2020(the_first_number, the_second_number):
  pass
# block ends

# main
numberlist = get_number_list()

print(numberlist)

filter_number_list(numberlist, is_sum_2020)

