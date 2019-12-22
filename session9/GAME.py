import random
game = {
    "player" : "P",
    'key' : 'k',
    'exit' : 'e',
    'map' :[["-","-","-","-"],["-","-","-","-"],["-","-","-","-"],["-","-","-","-"]]
}
game['map'][0][3] = 'P'
game['map'][1][1] = 'E'
game['map'][2][0] = 'K'
a = 0
b = 0
haskey = False
random.shuffle(game['map'])
for i in range(4):
    print(game['map'][i])
for i in range(4):
    for j in range(4):
        if game['map'][i][j] == "P":
            a = i
            b = j
while True:
    e = input("nhap cach di cua ban :")
    if e == 'w':
        if a > 0:
            game['map'][a][b] = '-'            
            a = a - 1
            if game['map'][a][b] == 'K':
                haskey = True
            if game['map'][a][b] == 'E' and haskey == True :
                print(" Mày Thắng")
                break
            elif game['map'][a][b] == 'E' and haskey == False :
                a =a+1
            game['map'][a][b] = "P"
            for i in range(4):
                print(game['map'][i])

    elif e == 'd':
        if b < 3:
            game['map'][a][b] = '-'
            b = b + 1
            if game['map'][a][b] == 'K':
                haskey = True
            if game['map'][a][b] == 'E' and haskey == True :
                print(" Mày Thắng")
                break
            elif game['map'][a][b] == 'E' and haskey == False :
                b= b -1
            game['map'][a][b] = 'P'
            for i in range(4):
                print(game['map'][i])
    elif e == 's':
        if a <3:
            game['map'][a][b] = '-'
            a = a + 1
            if game['map'][a][b] =='K':
                haskey = True
            if game['map'][a][b] == 'E' and haskey == True :
                print(" Mày Thắng")
                break
            elif game['map'][a][b] == 'E' and haskey == False:
                a = a - 1
            game['map'][a][b] = 'P'
            for i in range(4):
                print(game['map'][i])
    elif e ==  'a':
        if(b > 0):
            game['map'][a][b] = "-"
            b = b - 1
            if game['map'][a][b] == 'K':
                haskey = True
            if game['map'][a][b] == 'E' and haskey == True :
                print(" Mày Thắng")
                break
            elif game['map'][a][b] == 'E' and haskey == False :
                b = b+ 1
            game['map'][a][b] = 'P'
            for i in range(4):
                print(game['map'][i])

