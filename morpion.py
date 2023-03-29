import random
row1=None
column1=None
row2 = None
column2 = None

# Je créee des liste vide pour stocker les données des joueurs
data1=[]
data2=[]
data3=[]
data4=[]

# Je créee des variables pour compter le nombre de fois que les joueurs ont gagné
count=0
count2=0

print("Welcome to TIC-TAC-TOE!!")
tic=input("Enter O or X as your choice --> ")

# Cette fonction permet de vérifier si le tableau de jeu est plein ou non
def full_board_check(board):
    return len ([i for i in board if i == '#']) == 1
pass
# Je créee une condition pour que le joueur 2 ne puisse pas choisir la même lettre que le joueur 1
if tic=='O':
    tac='X'
else:
    tac='O'
block=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

# Je créee une condition pour que le joueur qui commence soit choisi au hasard
i=0
choice=int(input("Enter 1 for Head and 0 for Tail --> "))
x=random.randint(0,1)

# Je créee une condition pour que le joueur qui entre la valeur 'x' soit invité à commencer à entrer les coordonnées de la case qu'il souhaite remplir
if choice==x:
    print("## Saisissez la ligne et la colonne dans lesquelles vous souhaitez placer votre choix ##")
    row1=int(input("Ligne --> "))
    data1.append(row1)
    column1=int(input("Colonne --> "))
    data2.append(column1)
    block[row1-1][column1-1]=tic
    print(block[0][0],"|",block[0][1],"|",block[0][2])
    print(block[1][0],"|",block[1][1],"|",block[1][2])
    print(block[2][0],"|",block[2][1],"|",block[2][2])


    # Je créee une boucle infinie pour que le jeu continue jusqu'à ce qu'un des joueurs gagne ou qu'il y ait un match nul. Par ailleurs, selon les coordonnées entrées par le joueur, le méssage d'avertissement adéquat est affiché
    while True:
        i+=1
        if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
            if block[1][0]==tic:
                print("You Win!!")
            else:
                print('you Lose!!')
            break
        elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
            if block[2][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
            if block[0][1]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break

        # Je créee une condition pour que le joueur 2 qui est l'ordinateur puisse choisir les coordonnées de la case qu'il souhaite remplir
        elif i%2!=0:
            print("## A.I ##")
            if row2!=None and column2!=None:
                row2=random.randint(1,3)
                data3.append(row2)
                index1+=1
                length1=len(data3)

                # Je créee une condition "for" pour  parcourir les éléments de "data1". Si un élément correspond à "row2", une variable "count" est incrémentée de 1.
                for j in data1:
                    if row2==j:
                        count+=1
                for k in range(0,index1):
                    if row2==data3[k]:
                        count2+=1

                # La deuxième partie commence par la création d'une boucle "while" qui vérifie si la variable "count" est supérieure à 0. Si c'est le cas, une nouvelle valeur est générée pour "row2" et la boucle "for" est répétée.
                while count>0 or count2>0:
                    row2=random.randint(1,3)
                
            
                data3[index1]=row2
                column2=random.randint(1,3)
                data4.append(column2)
                index2+=1
                length2=len(data4)

                count=0
                count2=0
                for j in data2:
                    if row2==j:
                        count+=1
                for k in range(0,index2):
                    if column2==data4[k]:
                        count2+=1
                while count>0 or count2>0:
                    column2=random.randint(1,3)
                    for j in data2:
                        if row2 == j:
                            count += 1
                    for k in range(0, index2):
                        if column2 == data4[k]:
                            count2 += 1
                data4[index2]=column2
                block[row2-1][column2-1] = tac
            else:
                row2=random.randint(1,3)
                data3.append(row2)
                index1=0
                for j in data1:
                    if row2==j:
                        count+=1
                while count>0:
                    count=0
                    row2=random.randint(1,3)
                    data3[0]=row2
                    for j in data1:
                        if row2 == j:
                            count += 1
                column2=random.randint(1,3)
                data4.append(column2)
                index2=0
                count = 0
                for j in data2:
                    if row2 == j:
                        count += 1
                while count>0:
                    count=0
                    column2=random.randint(1,3)
                    data4[0]=column2
                    for j in data2:
                        if row2 == j:
                            count += 1
                block[row2 - 1][column2 - 1] = tac
            #block[row2-1][column2-1]=tac
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        elif i%2==0:
            print('## Your Turn ##')
            row1=int(input("Row --> "))
            data1.append(row1)
            column1=int(input("Column --> "))
            data2.append(column2)
            block[row1-1][column1-1]=tic
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        else:
            print("Draw!!")
            break
else:
    print("## A.I won the toss ##")
    print("## A.I ##")
    row2=random.randint(1,3)
    data3.append(row2)
    index1=0
    column2=random.randint(1,3)
    data4.append(column2)
    index2=0
    block[row2-1][column2-1]=tac
    print(block[0][0],"|",block[0][1],"|",block[0][2])
    print(block[1][0],"|",block[1][1],"|",block[1][2])
    print(block[2][0],"|",block[2][1],"|",block[2][2])
    while True:
        i+=1
        if block[0][0]==block[0][1] and block[0][1]==block[0][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[1][0]==block[1][1] and block[1][1]==block[1][2] and block[1][0]!=' ':
            if block[1][0]==tic:
                print("You Win!!")
            else:
                print('you Lose!!')
            break
        elif block[2][0]==block[2][1] and block[2][1]==block[2][2] and block[2][0]!=' ':
            if block[2][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][0] and block[1][0]==block[2][0] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][1]==block[1][1] and block[1][1]==block[2][1] and block[0][1]!=' ':
            if block[0][1]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][2] and block[1][2]==block[2][2] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][0]==block[1][1] and block[1][1]==block[2][2] and block[0][0]!=' ':
            if block[0][0]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif block[0][2]==block[1][1] and block[1][1]==block[2][0] and block[0][2]!=' ':
            if block[0][2]==tic:
                print("You Win!!")
            else:
                print("You Lose!!")
            break
        elif i%2==0:
            print("## A.I ##")
            row2=random.randint(1,3)
            data3.append(row2)
            index1+=1
            length1 = len(data3)
            for j in data1:
                if row2==j:
                    count+=1
            for k in range(0,index1):
                if row2==data3[k]:
                    count2+=1
            while count>0 or count2>0:
                count=0
                count2=0
                row2=random.randint(1,3)
                for j in data1:
                    if row2 == j:
                        count += 1
                for k in range(0,index1):
                    if row2==data3[k]:
                        count2+=1
            data3[index1]=row2
            count=0
            count2=0
            column2=random.randint(1,3)
            data4.append(column2)
            index2+=1
            length2 = len(data4)
            for j in data2:
                if column2==j:
                    count+=1
            for k in range(0,index2):
                if column2==data4[k]:
                    count2+=1
            while count>0 or count2>0:
                count=0
                count2=0
                column2=random.randint(1,3)
                for j in data2:
                    if column2 == j:
                        count += 1
                for k in range(0,index2):
                    if column2==data4[k]:
                        count2+=1
            data4[index2]=column2
            block[row2-1][column2-1]=tac
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        elif i%2!=0:
            print("## Your Turn ##")
            row1=int(input("Row --> "))
            data1.append(row1)
            column1=int(input("Column --> "))
            data2.append(column2)
            block[row1-1][column1-1]=tic
            print(block[0][0],"|",block[0][1],"|",block[0][2])
            print(block[1][0],"|",block[1][1],"|",block[1][2])
            print(block[2][0],"|",block[2][1],"|",block[2][2])
        else:
            print("Draw!!")
            break
print("Thanks for playing!!")

# En résumé, ce code génère une grille de 3 colonnes et un nombre de lignes défini par l'utilisateur, 
# en veillant à ce qu'il n'y est pas de doublons dans les lignes et les colonnes.