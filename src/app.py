def get_number_list():
  file = open("Data/1_1inputs.txt", "r")
  lines = file.readlines()
  return lines


numberlist = get_number_list()

print(numberlist)