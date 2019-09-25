from Siemowit_Engine import Siemowit_Engine

#TEST AREA :
game_map = Siemowit_Engine.Map(5,7)
new_map = game_map.generate_map(5,7)
Stefan = Siemowit_Engine.Player('Stefan',30,0,1,0,'fist','Stefan',{},30)
potion = Siemowit_Engine.Item('potion',10)
room_Fight = Siemowit_Engine.Room("Widzisz potwora")
room_Loot = Siemowit_Engine.Room("Widze skrzynke")


monsters = ['Bat','Rat']

while(0 == 0):
    if(new_map[Stefan.pos_x][Stefan.pos_y] == 5):
        print("KONIEC")
        break
    Siemowit_Engine.into_room(Stefan,new_map,monsters,potion,room_Fight,room_Loot)
    Siemowit_Engine.check_roads(Stefan,new_map)
    Siemowit_Engine.travel(Stefan)
    
    
    
    
#Game:
