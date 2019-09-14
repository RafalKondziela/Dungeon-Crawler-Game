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


#Moster Class

    #TODO - Klasa ogólna dla każdego potwora. Po niej dziedziczyć będą poszczególne potwory
    # - name (nazwa potwora)
    # - HP(Ilość życia potwora)
    # - ATT (ilość ataku potwora)


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



#######################################################################

# Methods ( Tu znajdują się metody wykorzystywane przez silnik podczas przebeigu gry)



#create_rooms() - tworzy instancje wszystkich lokacji dostępnych w grze


#move_f(player) - przesuwa gracza o 1 pole do przodu


#move_b(player) - przesuwa gracza o 1 pole do tyłu


#move_l(player) - przesuwa gracza o 1 pole w lewo


#move_r(player) - przesuwa gracza o 1 pole w prawo



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



#######################################################################
#Temporary test area :

game_map = Map(5,7)


game_map.generate_map(5,7)  
