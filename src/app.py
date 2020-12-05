def get_number_list():
  file = open("Data/1_1inputs.txt", "r")
  lines = file.readlines()

  numberlist = []
  for line in lines:
    numberlist.append(int(line))
    
  return numberlist


numberlist = get_number_list()

print(numberlist)