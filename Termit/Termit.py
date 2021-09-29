import pygame as pg
#import time
import random as rd
#from class_termit import Term_rab
pg.init()

def escape(): 
    for i in pg.event.get():
        if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
            return True
        else:
            return False

printid = True
tropage= 500
eattropage = 1000
inftrop = False
maxhp = 500
termitnikcordx = 33
termitnikcordy = 33
wherespawn = [[termitnikcordx+1,termitnikcordy-1], [termitnikcordx+1, termitnikcordy+3]]
width = 750
hight = 750
klet = 10
water_balance = 15 #% out of land
trees_balance = 15 #% out of land

direcs = ["up", "right", "down", "left"]
#eatfind = False

termitnikinf = [0, 0] #eda woda и

waterone = False #одно или много озёр (по умолчанию False)
eatmode = "new"   #new or old or one (по умолчанию new)




WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
WOOD = (202,164,114)
YELLOW = (255,255,0)
BROWN = (101,67,33)
GRASS = (5, 176, 5)
LIGHT_BLUE = (17, 190, 247)
ORANGE = (150,100,20)
YELLOW_GREEN = (159,205,7)


UP = (0)
DOWN = (-2)
LEFT = (-1)
RIGHT = (1)
#x = 5
#y = 4

"font"
idFont = pg.font.Font(None, 15) #klet*20,
#text1 = idFont.render('Hello Привет', 1, (180, 0, 0))


'''image'''
  #water########################
water1 = pg.image.load('waterCicle.png')#.convert_alpha()
water1 = pg.transform.scale(water1, (klet+1,klet+1))
water1 = pg.transform.rotate(water1, -90)
water2 = pg.transform.rotate(water1, 90)
water3 = pg.transform.rotate(water2, 90)
water4 = pg.transform.rotate(water3, 90)

waterend1 = pg.image.load('waterend.png')#.convert_alpha()
waterend1 = pg.transform.scale(waterend1, (klet+1,klet+1))
waterend1 = pg.transform.rotate(waterend1,0)
waterend2 = pg.transform.rotate(waterend1,90)
waterend3 = pg.transform.rotate(waterend2,90)
waterend4 = pg.transform.rotate(waterend3,90)

watermost1 = pg.image.load('watermost.png')#.convert_alpha()
watermost1 = pg.transform.scale(watermost1, (klet+1,klet+1))
watermost1 = pg.transform.rotate(watermost1,0)
watermost2 = pg.transform.rotate(watermost1,90)

watercicle = pg.image.load('waterciclesup.png')#.convert_alpha()
watercicle = pg.transform.scale(watercicle, (klet+1,klet+1))
############################################
termitn = pg.image.load('termitnik.png')#.convert_alpha()



termitnik = pg.transform.scale(termitn, (klet+1,klet+1))

termit1 = pg.image.load('termit1.png')
termit2 = pg.image.load('termit2.png')

trava = pg.image.load('trava.png')#.convert_alpha()
trava = pg.transform.scale(trava, (klet+1,klet+1))

eat = pg.image.load('apple.png')#.convert_alpha()
eat = pg.transform.scale(eat, (klet+1,klet+1))

tropa = pg.image.load('tropa.png')#.convert_alpha()
tropa = pg.transform.scale(tropa, (klet+1,klet+1))

'''window'''

#pg.display.set_icon(termitnik)
s = [[0] * int(width/klet) for i in range(int(hight/klet))]
#######################
#screen.fill(GRASS)

#рождение
#смерть
#состояние(еда,хп,вода)
#сост. влияет на активность
#режим(сон, работа, учёба, игра, гулянка и т.д)

def bub(x,y, direc): #возвращает x,y термита
    if direc == "up":
        if y-1 < 0:
            y = (hight/klet)-1
            x = x
        else:
            y -= 1
            x = x
    if direc == "down":
        if y+1 >= hight/klet:
            y = 0
            x = x
        else:
            y += 1
            x = x
    if direc == "right":
        if x+1 >= width/klet:
            y = y
            x = 0
        else:
            y = y
            x +=1
    if direc == "left":
        if x-1 < 0:
            y = y
            x = (width/klet)-1
        else:
            y = y
            x = x-1
    return int(x),int(y)


    #if x >= width/klet-1: #34
        #x = 0
    #if y >= hight/klet-1: #34
        #y = 0
    #if x <= 0: 
       # x = width/klet-1
    #if y <= 0:
    #    y = hight/klet-1
    #return x,y

def kletki(): #рисует клетки
    for i in range(0,hight,klet):
       pg.draw.line(screen,BLACK,(0,i),(width,i))
    for i in range(0,width,klet):
        pg.draw.line(screen,BLACK,(i,0),(i,hight))

def paint(): #рисует
    for i in range(int(hight/klet)):
        for j in range(int(width/klet)):
            if s[i][j] == "t":
                screen.blit(termitnik, (j*klet, i*klet))

            elif s[i][j]==0:
                #pg.draw.rect(screen,GREEN,(((j)*klet,(i)*klet),(klet,klet)))
                screen.blit(trava, (j*klet, i*klet))

            elif s[i][j] == "w":
                screen.blit(trava, (j * klet, i * klet))
                #pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))
                rad = radar(j,i)
                u = False
                d = False
                l= False
                r = False
                for h in rad:
                    if rad.get(h) == "w":
                        if h=="up":
                            u = True
                        elif h=="down":
                            d = True
                        elif h=="right":
                            r = True
                        else:
                            l = True

                    #полу-круги
                if (d and r) and (not u) and (not l):
                    screen.blit(water1, (j*klet, i*klet))
                elif (u and r) and (not l) and (not d):
                    screen.blit(water2, (j*klet, i*klet))
                elif (u and l) and (not r) and (not d):
                    screen.blit(water3, (j*klet, i*klet))
                elif (l and d) and (not r) and (not u):
                    screen.blit(water4, (j*klet, i*klet))
                    #концы
                elif (d) and (not r) and (not u) and (not l):
                    screen.blit(waterend1, (j*klet, i*klet))
                elif (r) and (not l) and (not u) and (not d):
                    screen.blit(waterend2, (j*klet, i*klet))
                elif (u) and (not r) and (not d) and (not l):
                    screen.blit(waterend3, (j*klet, i*klet))
                elif (l) and (not d) and (not u) and (not r):
                    screen.blit(waterend4, (j*klet, i*klet))
                    #мосты
                elif ((l and r) and (not d) and (not u)):
                    pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))#screen.blit(watermost1, (j*klet, i*klet))
                elif ((u and d) and (not r) and (not l)):
                    pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))#screen.blit(watermost2, (j*klet, i*klet))
                    #круг
                elif (not u) and (not d) and (not l) and (not r):
                    screen.blit(watercicle, (j*klet, i*klet))
                else:
                   pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))  

                '''try:
                    if s[i+1][j]=="w" and s[i][j+1]=="w" and s[i-1][j]!="w" and s[i][j-1]!="w":
                        screen.blit(water1, (j*klet, i*klet))
                    elif s[i+1][j]!="w" and s[i][j+1]=="w" and s[i-1][j]=="w" and s[i][j-1]!="w":
                        screen.blit(water2, (j*klet, i*klet))
                    elif s[i+1][j]!="w" and s[i][j+1]!="w" and s[i-1][j]=="w" and s[i][j-1]=="w":
                        screen.blit(water3, (j*klet, i*klet))
                    elif s[i+1][j]=="w" and s[i][j+1]!="w" and s[i-1][j]!="w" and s[i][j-1]=="w":
                        screen.blit(water4, (j*klet, i*klet))
                    else:
                        pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))
                except:
                    try:
                        if s[i+1][j]!="w" and s[i][j+1]=="w" and s[i-1][j]=="w" and s[i][j-1]!="w":
                            screen.blit(water2, (j*klet, i*klet))
                        elif s[i+1][j]!="w" and s[i][j+1]!="w" and s[i-1][j]=="w" and s[i][j-1]=="w":
                            screen.blit(water3, (j*klet, i*klet))
                        elif s[i+1][j]=="w" and s[i][j+1]!="w" and s[i-1][j]!="w" and s[i][j-1]=="w":
                            screen.blit(water4, (j*klet, i*klet))
                        else:
                            pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))
                    except:
                        try:
                            if s[i+1][j]!="w" and s[i][j+1]!="w" and s[i-1][j]=="w" and s[i][j-1]=="w":
                                screen.blit(water3, (j*klet, i*klet))
                            elif s[i+1][j]=="w" and s[i][j+1]!="w" and s[i-1][j]!="w" and s[i][j-1]=="w":
                                screen.blit(water4, (j*klet, i*klet))
                            else:
                                pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))
                        except:
                            try:
                                if s[i+1][j]=="w" and s[i][j+1]!="w" and s[i-1][j]!="w" and s[i][j-1]=="w":
                                    screen.blit(water4, (j*klet, i*klet))
                                else:
                                    pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))
                            except:
                                pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))                       
        
        
                if s[i-(hight-1)][j] == "w" and s[i][j-(wight-1)]=="w" and s[i-(hight+1)][j] != "w" and s[i][j-(wight+1)]!="w":
                    screen.blit(water1, (j*klet, i*klet))
                elif s[i-(hight-1)][j] != "w" and s[i][j-(wight-1)] =="w" and s[i-(hight+1)][j] == "w" and s[i][j-(wight+1)]!="w":
                    screen.blit(water2, (j*klet, i*klet))
                elif s[i-(hight-1)][j] != "w" and s[i][j-(wight-1)] !="w" and s[i-(hight+1)][j] == "w" and s[i][j-(wight+1)]=="w":
                    screen.blit(water3, (j*klet, i*klet))
                elif s[i-(hight-1)][j] == "w" and s[i][j-(wight-1)] !="w" and s[i-(hight+1)][j] != "w" and s[i][j-(wight+1)]=="w":
                    screen.blit(water4, (j*klet, i*klet))
                else:
                    pg.draw.rect(screen,LIGHT_BLUE,(((j)*klet,(i)*klet),(klet,klet)))
                    '''
                
            elif s[i][j] == "e":
                screen.blit(trava, (j * klet, i * klet))
                screen.blit(eat, (j*klet, i*klet))

            else:
                #pg.draw.rect(screen,YELLOW_GREEN,(((j)*klet,(i)*klet),(klet,klet)))
                screen.blit(trava, (j * klet, i * klet))
                screen.blit(tropa, (j * klet, i * klet))
                if inftrop == False:
                    s[i][j][1]-=1
                if s[i][j][1] <= 0:
                    s[i][j] = 0


    for t in termits:
        i = termits.get(t)
        if termits.get(t)[3] != "none":
            pg.draw.rect(screen, RED, (((i[0]) * klet, (i[1]) * klet), (klet, klet)))
        elif termits.get(t)[7] <= 50:
            pg.draw.rect(screen, BLACK, (((i[0]) * klet, (i[1]) * klet), (klet, klet)))
        else:
            pg.draw.rect(screen, ORANGE, (((i[0]) * klet, (i[1]) * klet), (klet, klet)))
        if printid:
            idPrint = idFont.render(str(t), 1, WHITE)
            screen.blit(idPrint, ((i[0]) * klet, (i[1]) * klet))


    #kletki()
    pg.display.update()

def move(x,y,direc, ostovtrop, id, eatFind): #двигает термита. Принимает текущии координаты и направление движенияния
    if ostovtrop:
        if eatFind == True:
            s[y][x] = [-id, eattropage]
        else:
            s[y][x] = [-id, tropage]
    else:
        s[y][x] = [-id, 20]
    x,y = bub(x,y,direc)
    #s[y][x] = -id
    #time.slleep(0.1)
    return x,y  # Возвращает координ

def print_masive(): #
    for row in s:
        for elem in row:
            print(elem, end=' ')
        print()

'''world'''
def world_generate():
    
    ''' water '''                
    water_s = int(((width/klet) * (hight/klet)) * (water_balance/100))
    if waterone != True:
        while water_s != 0:
            i = rd.randint(0,width/klet-1) 
            j = rd.randint(0,hight/klet-1)
            size = rd.randint(1,water_s)
            s[i][j] = "w"
            #paint(j,i, LIGHT_BLUE)
            water_s -= size
            for q in range(size):
                if i ==0:
                    i += rd.randint(0,1)
                if i == width/klet-1:
                    i += rd.randint(-1,0)
                else:
                    i += rd.randint(-1,1)

                if j ==0:
                    j = rd.randint(0,1)
                if j == hight/klet-1:
                    j += rd.randint(-1,0)
                else:
                    j += rd.randint(-1,1)
                #i += rd.randint(-1,1)     
                #j += rd.randint(-1,1)
                s[i][j] = "w"
                #paint(j,i,LIGHT_BLUE)
    else:
        i = rd.randint(0,width/klet-1) 
        j = rd.randint(0,hight/klet-1)
        for q in range(water_s):
            chance = rd.randint(1,2)
            if chance == 1: 
                if i ==0:
                    i += rd.randint(0,1)
                if i == width/klet-1:
                    i += rd.randint(-1,0)
                else:
                    i += rd.randint(-1,1)
                    
            else:     
                if j ==0:
                       j = rd.randint(0,1)
                if j == hight/klet-1:
                    j += rd.randint(-1,0)
                else:
                    j += rd.randint(-1,1)
                #i += rd.randint(-1,1)     
                #j += rd.randint(-1,1)
            s[i][j] = "w"
                #paint(j,i,LIGHT_BLUE)
        
            
    '''trees'''
    trees_s = int(((width/klet) * (hight/klet)) * (trees_balance/100))
    if eatmode == "old":  
        for q in range(trees_s):
            i = rd.randint(0,width/klet-1) 
            j = rd.randint(0,hight/klet-1)
            if s[i][j] == 0:
                s[i][j] = "e"
                #screen.blit(apple_tree, (j*klet, i*klet))
        pg.display.update()
    elif eatmode == "one":
        i = rd.randint(0,width/klet-1) 
        j = rd.randint(0,hight/klet-1)
        for q in range(trees_s):
            chance = rd.randint(1, 2)
            if chance == 1:
                if i == 0:
                    i += rd.randint(0, 1)
                if i == width / klet - 1:
                    i += rd.randint(-1, 0)
                else:
                    i += rd.randint(-1, 1)

            else:
                if j == 0:
                    j = rd.randint(0, 1)
                if j == hight / klet - 1:
                    j += rd.randint(-1, 0)
                else:
                    j += rd.randint(-1, 1)
                #i += rd.randint(-1,1)     
                #j += rd.randint(-1,1)
            s[i][j] = "e"
                #paint(j,i,LIGHT_BLUE)
    else:
        while trees_s != 0:
            i = rd.randint(0,width/klet-1) 
            j = rd.randint(0,hight/klet-1)
            size = rd.randint(1,trees_s)
            s[i][j] = "e"
            #paint(j,i, LIGHT_BLUE)
            trees_s -= size
            for q in range(size):
                chance = rd.randint(1, 2)
                if chance == 1:
                    if i == 0:
                        i += rd.randint(0, 1)
                    if i == width / klet - 1:
                        i += rd.randint(-1, 0)
                    else:
                        i += rd.randint(-1, 1)

                else:
                    if j == 0:
                        j = rd.randint(0, 1)
                    if j == hight / klet - 1:
                        j += rd.randint(-1, 0)
                    else:
                        j += rd.randint(-1, 1)
                #i += rd.randint(-1,1)     
                #j += rd.randint(-1,1)
                s[i][j] = "e"
                #paint(j,i,LIGHT_BLUE)
        '''termitnik'''
    for i in range(termitnikcordy, termitnikcordy + 3):
        for j in range(termitnikcordx, termitnikcordx + 3):
            s[i][j] = "t"
    paint()

def food_generate(much):
    global s
    if much:
        need = True
        while need:
            x = rd.randint(0, int(width/klet)-1)
            y = rd.randint(0, int(hight/klet)-1)
            if s[y][x] != "t" and s[y][x] != "w" and s[y][x] != "e":
                need = False
                rad = radar(x,y)
                for i in rad:
                    if rad.get(i) == "w":
                        s[y][x] = "w"
                        break
                    elif rad.get(i) == "e":
                        s[y][x] = "e"
                        break
    else:
        x = rd.randint(0, int(width / klet) - 1)
        y = rd.randint(0, int(hight / klet) - 1)
        if s[y][x] != "t":
            need = False
            rad = radar(x, y)
            for i in rad:
                if rad.get(i) == "w":
                    s[y][x] = "w"
                    break
                elif rad.get(i) == "e":
                    s[y][x] = "e"
                    break


def napr(direc, angle):
    di = ["up",'right','down',"left"]
    g = di.index(direc)
    f = di[g+angle]
    #print(f)
    return f

def radar(x,y):
    voz_dir = ["up","right", "down", "left"]
    if y == 0:
        voz_dir.remove("up")
    if x == 0:
        voz_dir.remove("left")
    if y == hight/klet-1:
        voz_dir.remove("down")
    if x == width/klet-1:
        voz_dir.remove("right")
    #voz_dir.remove(napr(direc,-2))
    rad = dict()
    for i in voz_dir:
        if i =="up":
            rad[i] = s[y-1][x]
        if i =="right":
            rad[i] = s[y][x+1]
        if i =="down":
            rad[i] = s[y+1][x]
        if i =="left":
            rad[i] = s[y][x-1]
    return rad

def decision(x,y,direc,mode, id, eatfind):

    rad = radar(x,y)

    none = []
    trop = []
    tropinf = []
    eda = False
    termik = False

    #print(rad)

    for i in rad:
        if rad.get(i) == 0:
            none.append(i)
        if (type(rad.get(i)) == list) or (type(rad.get(i)) == int and rad.get(i) < 0):  #(str(rad.get(i))!= rad.get(i) and ((0<rad.get(i)<=tropage) or (rad.get(i) <= -1))):
            tropinf.append(rad.get(i))
            trop.append(i)
        if rad.get(i) == "e" or rad.get(i) == "w":
            eda = i
        if rad.get(i) == "t":
            termik = i

    ln = len(none)
    lt = len(trop)

    def fromTo():
        i = False
        age = False
        dir1 = False
        age2 = False
        dir2 = False
        can = True
        while can:
            for dir in rad:
                if type(rad.get(dir)) == list or (type(rad.get(dir)) == int and rad.get(dir) < 0):
                    dob = rad.get(dir)
                    if type(dob) == int:
                        inf = termits.get(id)
                        #print("inf = ", inf)
                        if inf[-1] ==  True:    #eatfind, ostovtrop
                            if inf[-2] == True:
                                dob = [dob, 2000]
                            else:
                                dob = [dob, 1000]
                        else:
                            dob = [dob, 10]

                    if (type(i)!=int) and (dob[1]>1000): #and dob[0] != -id): ########################### 1 не найден
                        i = dob[0]
                        age = dob[1]
                        dir1 = dir
                    elif (type(i)!=bool) and (dob[1]==age+2 or dob[1]==age-2): ############################ 2 не найден
                        age2 = dob[1]
                        can = False
                        dir2 = dir
                        break
            can = False
        if i != False:
            if age>age2:
                #print("dir1 =",dir1)
                return dir1
            else:
                #print("dir2 =",dir2)
                return dir2
        else:
            return False


    #print(id, "-",tropinf)

    def notrop():
        if ln == 1:
            return none[0]

        elif ln > 1 and (direc in none) and (napr(direc,-1) or napr(direc,-3)):
            if napr(direc,-2) in none:
                none.remove(napr(direc, -2))
            chance = rd.randint(1,100)
            if chance >= 20:
                return "none" , direc
            else:
                none.remove(direc)
                if ln != 1:
                    return "none", none[rd.randint(0,1)]
                else:
                    return "none", none[0]

        elif ln > 0 and (direc in none) and ((napr(direc, -2) not in none)):
            print("lol")





    if mode == "search":
        ''' search '''
        if eda != False:
            if rad.get(eda) == "w":
                return "w", eda
            else:
                return "e", eda


        if lt == 0:
            return "none", none[rd.randint(0,ln-1)]


        elif lt == 1:
            chance = rd.randint(1, 100)
            if chance > 50:
                return "none", trop[0]
            else:
                if ln > 1:
                    chance = rd.randint(1,100)
                    if direc in none and chance > 5:
                        return "none", direc
                    else:
                        return "none", none[rd.randint(0, ln-1)]
                else:
                    return "none", none[0]


        else:
            """есть шанс что не будет деалть новую дорогу"""
            if rd.randint(1,100) > 10 or ln == 0:
                '''lt > 1'''
                if napr(direc, -2) in trop:
                    trop.remove(napr(direc, -2))
                    lt = len(trop)
                if direc in trop and rd.randint(1, 100) > 20:
                    return "none", direc
                elif lt == 1:
                    return "none", trop[0]
                else:
                    #if direc in trop:
                    #    trop.remove(direc)
                    #    lt = len(trop)
                    return "none", trop[rd.randint(0, lt-1)]
            else:
                return "none", none[rd.randint(0,ln-1)]


    if mode == "return":
        if termik != False:
            return "term",direc
        else:
            if lt == 0:
                if ln == 1:
                    return "none", none[0]
                else:
                    return "none", none[rd.randint(0, ln - 1)]


            elif lt == 1:
                if direc not in trop:
                    if ln > 1:
                        chance = rd.randint(1, 100)
                        if direc in none and chance > 5:
                            return "none", direc
                        else:
                            return "none", none[rd.randint(0, ln - 1)]
                    else:
                        if ln >= 1:
                            return "none", none[0]
                        else:
                            return "none", trop[0]

                else:
                    return "none", trop[0]


            else:
                """есть шанс что будет деалть новую дорогу"""
                if rd.randint(1, 600) > 1 or ln == 0:
                    '''lt > 1'''
                    if napr(direc, -2) in trop:
                        trop.remove(napr(direc, -2))
                        lt = len(trop)

                    if direc in trop and rd.randint(1,100)> 20:
                        return "none", direc
                    elif lt == 1:
                        return "none", trop[0]
                    else:
                        return "none", trop[rd.randint(0, 1)]
                else:
                    return "none", none[rd.randint(0, ln - 1)]

        '''
        else:
            if direc in trop and napr(direc, -1) in trop and napr(direc, -3) in trop:
                if napr(direc, -2) in trop:
                    trop.remove(napr(direc, -2))
                #return "none", trop[rd.randint(0, len(trop) - 1)]
                return "none", direc
            elif direc in trop and napr(direc, -1) in trop or napr(direc, -3) in trop:
                if napr(direc, -2) in trop:
                    trop.remove(napr(direc, -2))
                return "none", trop[rd.randint(0, len(trop) - 1)]
                #return "none", direc
            elif direc in trop:
                return "none", direc
            elif direc not in trop:
                if napr(direc, -1) in trop and napr(direc, -3) in trop:
                    trop.remove(napr(direc, -2))
                    rand = rd.randint(0, len(trop) - 1)
                    return "none", trop[rand]
                elif len(trop) == 2:
                    trop.remove(napr(direc, -2))
                    return "none", trop[0]
                else:
                    return "none", trop[0]
                    '''




        '''
                else:
                    #ln = len(trop)
                    if napr(direc,-1) in trop:
                        return "none", napr(direc,-1)
                    elif direc in trop:
                        return "none", direc
                    elif napr(direc,-3) in trop:
                        return "none", napr(direc,-3)
                    else:
                        return "none", napr(direc, -2)
                        '''
                #elif ln == 2:
                    #if trop[0] != napr(direc,-2):
                    #    return "none",trop[0]
                    #else:
               #         return "none",trop[1]
               # elif ln == 1:
                #    return "none",trop[0]
                #else:
                  #  trop.remove(napr(direc,-2))
                   # return "none",trop[rd.randint(0,ln-2)]
    '''if trop[0] != napr(direc,-2):
                        return "none",trop[0]
                    else:
                        return "none",trop[rd.randint(1,ln-1)] '''
    #if mode == "harvest":       
    #if ranar = none
    #    90% dire
    #     5 - left
    #      5 - right
    #if radar != none
    #    take fooood or wateer
    #return direc,dob
# Конец карты, вода, еда

'''
class Term_rab():
    def __init__(self, x, y):
        #self.speed = speed
        #self.healt = health
        #self.water = water
        #self.eat = eat
        self.x = x
        self.y = y
        print("termit create")
    def life(self):
        y,x = self.y ,self.x
        #s[y][x] = -1
        eatfind = False
        inventory = "none"
        paint()
        direc = "up"
        mode = "search"
        ostovtrop = True
        steps = 0
        while not escape():
            #dob = добыча
            dob,direc = decision(x, y, direc, mode, eatfind)
            #print(dob)
            if dob == "e" or dob == "w":
                inventory = dob
                sters = 0
                x,y = move(x,y,direc,ostovtrop)
                mode = "return"
                eatfind = True
                print(inventory)
                rad = radar(x, y, direc)
                ostovtrop = False
                for i in (rad):
                    if rad.get(i) == "w" or rad.get(i) == "e":
                        ostovtrop = True

            elif dob == "term":
                if inventory == "w":
                    termitnikinf[1] = termitnikinf[1] + 1
                elif inventory == "e":
                    termitnikinf[0] = termitnikinf[0] + 1
                inventory = "none"
                mode = "search"
                direc = napr(direc,-2)
                print(termitnikinf)
                sters = 0
                if ostovtrop == False:
                    ostovtrop = True
                    eatfind = False
           # elif int(tropage/3) <= steps:
                #mode = "return"
                #x, y = move(x, y, direc, ostovtrop)
                #ostovtrop = False
            else:
                x,y = move(x,y,direc,ostovtrop)
                steps+=1
            paint()
        #pg.quit()
'''
def terRabLife(f, id):


    x = int(f[0])
    y = int(f[1])
    direc = f[2]
    inventory = f[3]
    mode = f[4]
    eatfind = f[5]
    ostovtrop = f[6]
    hp = f[7]

    #x, y, direc, inventoty, mode
    #s[y][x] = -1
    #paint()
    #steps = 0
    # dob = добыча

    dob, direc = decision(x, y, direc, mode, id, eatfind)

    #rad = radar(x, y, direc)
    #rada = []
    #for i in rad:
    #    rada.append(rad.get(i))

    if dob == "w" or dob == "e":
        inventory = dob
        x, y = move(x, y, direc, ostovtrop, id, eatfind)
        mode = "return"
        eatfind = True
        rad = radar(x, y)
        direc = napr(direc, -2)
        ostovtrop = False

        for i in (rad):
            if rad.get(i) == "w" or rad.get(i) == "e":
                ostovtrop = True

    elif dob == "term":
        hp = 1000
        if inventory == "w":
            termitnikinf[1] = termitnikinf[1] + 1
        elif inventory == "e":
            termitnikinf[0] = termitnikinf[0] + 1
        inventory = "none"
        mode = "search"
        #print(termitnikinf)
        #sters = 0
        if ostovtrop == False:
            ostovtrop = True
            eatfind = False
        direc = napr(direc, -2)

    else:
        x, y = move(x, y, direc, ostovtrop, id, eatfind)
        hp -=1

    if hp <= 5:
        if inventory != "none":
            inventory = "none"
            hp = maxhp
            mode = "search"
            direc = napr(direc, -2)

    rad = radar(x,y)
    for i in (rad):
        if rad.get(i) == "t":
            hp = maxhp


    #x,y, direc, inventoty, mode, eatfind
    return x, y, direc, inventory, mode, eatfind, ostovtrop, hp


#search - harvest - return - drop \
#| - - - - - - - - - - - - - - -  /
#ter1.life()
#print_masive()
#main
#ter1 = Term_rab(5,4)
#ter2 = Term_rab(4,5)
#if ter1.life() and ter2.life():
    #print(1)
#ter1.life()
#print_masive()
#screen.blit(waterend1, (0, 0))
#screen.blit(waterend2, (40, 40))
#screen.blit(waterend3, (80, 80))
#screen.blit(waterend4, (120, 120))'''


#x,y, direc, inventoty, mode, ,die
#termits.append([5, 4,"up","none", "search"])


termits = dict()
#x,y, direc, inventoty, mode, ,eatfound, ostovtrop, hp
spawn = wherespawn[rd.randint(0, len(wherespawn)-1)]
termits[1] = [spawn[0], spawn[1], direcs[rd.randint(0,3)],"none", "search", False, True, maxhp]
#termits[1] = [0, 1, ,"none", "search", False, True]
'''termits[2] = [5, 1,"up","none", "search", False, True]
termits[3] = [5, 2,"left","none", "search", False, True]
termits[4] = [5, 3,"up","none", "search", False, True]
termits[5] = [5, 4,"up","none", "search", False, True]
termits[6] = [0, 5,"left","none", "search", False, True]
termits[7] = [1, 5,"left","none", "search", False, True]
termits[8] = [2, 5,"left","none", "search", False, True]
termits[9] = [3, 5,"left","none", "search", False, True]
termits[10] = [4, 5,"left","none", "search", False, True]'''


def console():
    def inputval(whattoinput, possiblevalue):
        need = True
        while need:
            print(str(whattoinput) + ":" + "possible values" + ":" + str(possiblevalue) + "." + "'ENTER' if you want default")
            value = input(">>> ")
            print(value)
            if value == "":
                return "def"
            elif type(possiblevalue) == list and value in possiblevalue:
                return value
            elif type(int(value)) == type(possiblevalue):
                return int(value)
            else:
                print("Incorrect value")

#    value = inputval("tropage", 1)
#    if value != "def":
#        global tropage
#        tropage = value
#
#    value = inputval("eattropage", 1)
#    if value != "def":
#        global eattropage
#        eattropage = value
#
#    value = inputval("maxhp", 1)
#    if value != "def":
#        global maxhp
#        maxhp = value
#
#    value = inputval("termitnikcordx", 1)
#    if value != "def":
#        global termitnikcordx
#        termitnikcordx = value
#
#    value = inputval("termitnikcordx", 1)
#    if value != "def":
#        global termitnikcordx
#        termitnikcordx = value
#
#    value = inputval("termitnikcordy", 1)
#    if value != "def":
#        global termitnikcordy
#        termitnikcordy = value

#eattropage = 1000
#maxhp = 500
#
#termitnikcordx = 33
#termitnikcordy = 33
#
#wherespawn = [[termitnikcordx+1,termitnikcordy-1], [termitnikcordx+1, termitnikcordy+3]]
#
#
#klet = 10
#width = 700
#hight = 700
#
#water_balance = 20 #% out of land
#
#trees_balance = 20 #% out of land
#
#direcs = ["up", "right", "down", "left"]
##eatfind = False
#
#termitnikinf = [0, 0] #eda woda
#
#waterone = False #одно или много озёр (по умолчанию False)
#eatmode = "new"   #new or old or one (по умолчанию new)

#if input("Print '1' if you wand to input values ") == "1":
#    console()

screen = pg.display.set_mode((width, hight))
pg.display.set_caption("10 BIT TERMIT")
pg.display.set_icon(termitn)
timer_event = pg.USEREVENT + 0
pg.time.set_timer(timer_event, 15)
paint()
world_generate()
pg.display.update()

running = True
while (running):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                running = False
            elif event.type == timer_event:
                #for l in range(1, len(termits)+1):
                for l in termits:
                    if termits.get(l)[7] > 0:
                        #print("fun", termits[l][0], termits[l][1])
                        termits[l] = terRabLife(termits.get(l), l)


                if termitnikinf[1] >= 2:
                    spawn = wherespawn[rd.randint(0, len(wherespawn)-1)]
                    termits[len(termits)+1] = [spawn[0], spawn[1], direcs[rd.randint(0,3)], "none", "search", False, True, maxhp]
                    termitnikinf[1] -= 2
                    print(len(termits))

                elif termitnikinf[0] >= 5:
                    spawn = wherespawn[rd.randint(0, len(wherespawn)-1)]
                    termits[len(termits)+1] = [spawn[0], spawn[1], direcs[rd.randint(0,3)], "none", "search", False, True, maxhp]
                    termitnikinf[0] -= 5
                    print(len(termits))

                food_generate(False)
                paint()



'''test mode
      if eda != False:
            if rad.get(eda) == "w":
                return "w", eda
            else:
                return "e", eda
        else:
            if lt == 0 or (lt == 1): #and tropinf[0][0] == -id): ################ своя или нету тропинки
                if direc in none:
                    return "none", direc
                else:
                    if ln > 1:
                        return "none", none[rd.randint(0, ln-1)]
                    else:
                        return "none", none[0]
            elif lt > 1: ################################################### from to
                ret = fromTo()
                #print(ret)
                if ret != False:
                    return "none", ret
                else:
                    if len(trop) >= 2:
                        #print("lt =", len(trop))
                        if direc in trop:
                            return "none", direc
                        else:
                            return "none", trop[rd.randint(0, lt-1)]
                    else:
                        return "none", trop[0]
            else: ########################################################## :(
            

'''