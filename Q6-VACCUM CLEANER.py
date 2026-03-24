rooms = {'A':'Dirty', 'B':'Dirty'}
pos = 'A'

while True:
    if rooms[pos] == 'Dirty':
        rooms[pos] = 'Clean'
        print("Cleaning", pos)
    if pos == 'A':
        pos = 'B'
    else:
        pos = 'A'
    if rooms['A']=='Clean' and rooms['B']=='Clean':
        break

print("All clean")
