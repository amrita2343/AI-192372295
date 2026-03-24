colors = ['Red','Green','Blue']
states = ['A','B','C']

for a in colors:
    for b in colors:
        for c in colors:
            if a!=b and b!=c and a!=c:
                print(a,b,c)
                break
