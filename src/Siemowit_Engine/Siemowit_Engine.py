import random
import numpy as np


#Siemowit Silnik stworzony do tworzenia gry typu Dungeon Crawler
#Author: Rafał Kondziela


######################################################################

#Classes essential to Dungeon Crawler



#Player Class

    # TODO - Klasa do tworzenia postaci gracza:
    # - HP
    # - base_ATT (na 1 LVLu ma byc 0 + 2 on lvl)
    # - LVL bazowo 1
    # - EXP  bazowo 0
    # - equipped_weapon (akutalnie używana broń)
    # - pos_x (pozycja x na mapie)
    # - pos_y (pozycja y na mapie) 
    # - Class (Aktualna klasa postaci)
    # - Equipment (słownik w formie (przedmiot : ile_przedmiotu))

class Player:
    pos_x = 3
    pos_y = 0
    def __init__(self,name,HP,base_ATT,lvl,exp,equipped_weapon,Class,equipment):
        self.name = name
        self.HP = HP
        self.base_ATT = base_ATT
        self.lvl = lvl
        self.exp = exp
        self.equipped_weapon = equipped_weapon
        self.Class = Class
        self.equipment = equipment

#Weapon Class

    # TODO - Klasa ogólna dla każdej broni. Po niej dziedziczyć będą poszczególne bronie
    # - name ( nazwa broni)
    # - ATT (Obrażenia zadawane przez broń

class Weapon:
    def __init__(self,name,ATT):
        self.name = name
        self.ATT = ATT


#Moster Class

    #TODO - Klasa ogólna dla każdego potwora. Po niej dziedziczyć będą poszczególne potwory
    # - name (nazwa potwora)
    # - HP(Ilość życia potwora)
    # - ATT (ilość ataku potwora)

class Monster:
    def __init__(self,name,HP,ATT):
        self.name = name
        self.HP = HP
        self.ATT = ATT


#Map Class

    #TODO - Klasa ogólna dla mapy nałożonej na kartezjański układ współrzędnych
    # - fields_x - szerokość mapy
    # - fields_y - wysokość mapy
    # - metoda generate_map(fields_x, fields_y) - przelatuje od lewej do prawej po całej mapie i jeżeli wylosje że na danej współrzędnej jest room to go wstawia a jak nie to wstawia "0"

class Map:
    def __init__(self, fields_x, fields_y):
        self.fields_x = fields_x
        self.fields_y = fields_y
        
        

    def generate_map(self,fields_x, fields_y):
        new_map = np.zeros(shape =(fields_x,fields_y))
        for x in range(0,fields_x):
            for y in range(0,fields_y):
                if(x == 0 and y == 3):
                    new_map[x][y] = 4
                elif(x == 4 and y == 3):
                    new_map[x][y] = 5
                elif(y == 3 and x > 0 and x < 4 ):
                    new_map[x][y] = 1
                else:
                    if(x == 0):
                        throw = throw_coin()
                        if(throw == 1):
                            new_map[x][y] = 1
                        else:
                            new_map[x][y] = 0
                    if(x > 0 and x < 3 and new_map[x - 1][y] == 1):
                        new_map[x][y] = 1
                    else:
                        throw = throw_coin()
                        if(throw == 1):
                            new_map[x][y] = 1
                        else:
                            new_map[x][y] = 0
                    if(x > 3 and (new_map[x - 1][y] == 1 or new_map[x - 1][y] == 4 or new_map[x - 1][y] == 5)):
                        throw = throw_coin()
                        if(throw == 1):
                            new_map[x][y] = 1
                        else:
                            new_map[x][y] = 0
                    
                        
   #Poprawić generowanie mapy jak już ustale dla czego sie nie generuje tak jak chce
   #Dodać podział na generowanie ze względu na level                         
                    
                    
                    
                   
                #print(new_map[x][y])
        print(new_map)
        return new_map

    
    
        

#Room Class

    #TODO - Klasa ogólna dla poszczególnych lokacji. Po niej dziedziczyć będą poszczególne lokacje
    # - description (docelowo jest plik .txt z opisami lokacji w którym to opisy oznaczone są regexami po których każy pokój ma swój opis


class Room:
    def __init__(self,description):
        self.description = description

    def show_description(description):
        print(descrption)

#Item Class

    #TODO Klas ogólna dla każdego przedmiotu. Po niej dziedziczyć będzą wszystie przedmioty

        # - name (nazwa przedmiotu)
        # - value (ilość punktów HP które przywraca)

class Item:
    def __init__(self,name,value):
        self.name = name
        self.value = value



#######################################################################

# Methods ( Tu znajdują się metody wykorzystywane przez silnik podczas przebeigu gry)



#create_rooms() - tworzy instancje wszystkich lokacji dostępnych w grze


#move_f(player) - przesuwa gracza o 1 pole do przodu

def move_f(player):
    player.pos_x = player.pos_x
    player.pos_y = player.pos_y + 1


#move_b(player) - przesuwa gracza o 1 pole do tyłu

def move_b(player):
    player.pos_x = player.pos_x
    player.pos_y = player.pos_y - 1

#move_l(player) - przesuwa gracza o 1 pole w lewo

def move_l(player):
    player.pos_x = player.pos_x + 1
    player.pos_y = player.pos_y 

#move_r(player) - przesuwa gracza o 1 pole w prawo

def move_r(player):
    player.pos_x = player.pos_x - 1
    player.pos_y = player.pos_y 


#Dice 

    #TODO Metody w których będą rzuty kostką
    # - metoda : throw_K(x) (x to wielkość rzucanej kostki)
    # - metoda : throw_coin ( wypada 0 lub 1)


def throw_K(x):
    throw = random.randint(1,x)
    return throw

def throw_coin():
    throw = random.randint(0,1)
    return throw


########################################################################

#Main Game Loop Methods :


#Metoda sprawdzająca pozycję gracza na mapie losująca lokacje z dostępnej listy
#dodająca wylosowanego potwora do lokacji i zarządzająca co dalej
def into_room(player,game_map):
    if(game_map[player.pos_y][player.pos_x] == 4):
        print("Jestę na statcie")
        check_roads(player,game_map)
        travel(Stefan)
    elif(new_map[player.pos_y][player.pos_x] == 1):
        print("Poszedłem do przodu")
        check_roads(player,game_map)
        travel(Stefan)
        



#Metoda sprawdzająca możliwe ścierzki i wyświetlająca opcje podróży na ekranie
def check_roads(player,game_map):
    if(game_map[player.pos_y + 1][player.pos_x] == 1 or game_map[player.pos_y + 1][player.pos_x] == 5 or game_map[player.pos_y + 1][player.pos_x] == 6):
        print("Naciśnij 'f' aby iść naprzód")
    if(game_map[player.pos_y - 1][player.pos_x] == 1 or game_map[player.pos_y + 1][player.pos_x] == 5 or game_map[player.pos_y + 1][player.pos_x] == 4 or game_map[player.pos_y + 1][player.pos_x] == 6):
        print("Naciśnij 'b' aby iść do tylu")
    if(game_map[player.pos_y][player.pos_x + 1] == 1 or game_map[player.pos_y + 1][player.pos_x] == 5 or game_map[player.pos_y + 1][player.pos_x] == 4 or game_map[player.pos_y + 1][player.pos_x] == 6):
        print("Naciśnij 'l' aby iść w lewo")
    if(game_map[player.pos_y][player.pos_x - 1] == 1 or game_map[player.pos_y + 1][player.pos_x] == 5 or game_map[player.pos_y + 1][player.pos_x] == 4 or game_map[player.pos_y + 1][player.pos_x] == 6):
        print("Naciśnij 'r' aby iść w prawo")
    


#Metoda do podróżowania po mapie
def travel(player):
    chosen_path = input('Wybierz ścierzkę: ')
    if(chosen_path.lower() == 'f'):
        move_f(player)
    if(chosen_path.lower() == 'b'):
        move_b(player)
    if(chosen_path.lower() == 'l'):
        move_l(player)
    if(chosen_path.lower() == 'r'):
        move_r(player)


#Metoda służąca do walki między graczem a potworem
def fight(player,monster):
    while(player.HP > 0 or monster.HP > 0):
        print(player.name  , '**************' , player.HP)
        print(monster.name , '**************' , monster.HP)
        action = input("wciśnij 'a' aby zaatakować: ")
        if(action.lower() == 'a'):
            att = throw_K(6) + player.base_ATT #tu testowo 6 docelowo bedzie zależne od broni
            print(att)
            monster.HP -= att
            if(monster.HP > 0):
                att = throw_K(monster.ATT)
                print(att)
                player.HP -= att
                if(player.HP <= 0):
                    print("porażka")
                    break
            else:
                print("zwycięstwo")
                break

#######################################################################
#Temporary test area :

game_map = Map(5,7)

new_map = game_map.generate_map(5,7)


Stefan = Player('Stefan',30,0,1,0,'fist','Stefan',[])
Rat = Monster('Rat',15,5)


#for x in range(5):
   # into_room(Stefan,new_map)

fight(Stefan,Rat)






