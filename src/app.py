def get_number_list():
  file = open("Data/1_1inputs.txt", "r")
  lines = file.readlines()

  new_numberlist = []
  for line in lines:
    new_numberlist.append(int(line))

  return new_numberlist
# block ends

def filter_number_list(the_numberlist, criteria_def):
  filtered_number_list = []
  for first_pos in range(0,len(the_numberlist)):
    for second_pos in range(0,len(the_numberlist)):
      if first_pos == second_pos:
        continue

      if the_numberlist[first_pos] + the_numberlist[second_pos] > 2020:
        continue

      for third_pos in range(0,len(the_numberlist)):
        if second_pos == third_pos:
          continue

        if first_pos == third_pos:
          continue
        

        first_number = the_numberlist[first_pos]
        second_number = the_numberlist[second_pos]
        third_number = the_numberlist[third_pos]
        is_true = criteria_def(first_number, second_number, third_number)

        print(first_number, second_number, third_number, is_true)

        if is_true: 
          filtered_number_list.append(first_number)
          filtered_number_list.append(second_number)
          filtered_number_list.append(third_number)
          break
        # end of 3rd for loop 
        if len(filtered_number_list) > 0:
          break
      # end of 2nd for Loop
    if len(filtered_number_list) > 0:
      break
    # end of 1st for loop 


  return(filtered_number_list)
# block ends

def is_sum_2020(the_first_number, the_second_number, the_third_number):
  the_sum = the_first_number + the_second_number + the_third_number
  if the_sum == 2020:
    return True
  return False
# block ends

# main
numberlist = get_number_list()

print(numberlist)

results = filter_number_list(numberlist, is_sum_2020)

print(results)

answer = results[0] * results[1] * results[2]
print('the answer is', answer)
