def bubble(mylist):
  n = len(mylist)

  for i in range(n):
    for j in range(n- 1):
      if mylist[j] > mylist[j+1] :
        temp = mylist[j]
        mylist[j] = mylist[j+1]
        mylist[j+1] = temp

  return mylist


print('Input any letter to end the list\nEnter elements:')

try:
  new_list = []

  while True:
    new_list.append(int(input()))

except:
  print(f'Given List is : {new_list}\n')
  
final = bubble(new_list)

print(f'Sorted List is : {final} ')
