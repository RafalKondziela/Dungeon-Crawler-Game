from Siemowit_Engine import Siemowit_Engine

#TEST AREA :
game_map = Siemowit_Engine.Map(5,7)
new_map = game_map.generate_map(5,7)
Stefan = Siemowit_Engine.Player('Stefan',30,0,1,0,'fist','Stefan',{},30)
Rat = Siemowit_Engine.Monster('Rat',15,5,10)
Bat = Siemowit_Engine.Monster('Bat',10,3,5)

monsters = [Bat,Rat]

while(0 == 0):
    Siemowit_Engine.into_room(Stefan,new_map)
    Siemowit_Engine.travel(Stefan)
    if(game_map[player.pos_y][player.pos_x - 1] == 5):
        print("KONIEC")
        break
    
    
    
#Game:
