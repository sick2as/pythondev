import random,p
class player:
    def __init__(self,name):
        self.lives = 3
        self.name = name
        self.health = 100
    def looselife(self): 
        self.lives = self.lives -1
    def resetlives(self):
        self.lives = 3
class enmey:
         def __init__(self,name):
            print(name,"is attacking")
            self.qlives = 3
            self.name = name
            self.health = 100
         def elooselife(self): 
                        self.qlives = self.qlives -1
         def edie(self):
                        if self.lives != 0:
                            pass
                        else:
                            print(f"{self.name} is now dead :( ")
         def eresetlives(self):
                        self.lives = 3
name = input("what's your name: ")
a = player(name)
def game():
 o = None
 arc = True
 while arc == True:
    if a.lives == 0:
        print(f"Sorry {a.name} you have died")
        arc = False
    else:
        q = random.randint(1,3)
        if q == 1:
            spider = enmey("spider")
        if q == 2:
            spider = enmey("spider")
        if q == 3:
            spider = enmey("spider")
        while spider.qlives !=0:
            choice = input("what attack would you like to use 1. Fire ball 100dmg -1 life 2. gold fist 50dmg -1/2 life: ")
            if choice == "devtools":
                c = input("what devtool shall you use?")
                if c == "/endlife":
                    a.looselife()
                if c == "//win":
                    spider.lives = 0
                if c == ":/givelife":
                    a.lives = a.lives + 1
                  
            if choice == "1":
                if o != "on cooldown":
                 spider.elooselife()
                 print("Spider has lost -1 lives")
                 damage = random.randint(50,100)
                 if a.health != 0:
                  print(f"Spider has done {damage} damage")
                  a.health = a.health -  damage
                 else: 
                     print(f"Spider hsa done {damage} damage and you lost a life")
                     a.lives = a.lives -1
                     a.health = 100
                 o = "on cooldown"
                else:
                  print("On cooldown")
            elif choice == "2":

                spider.health = spider.health -50
                if spider.health <= 0:
                    spider.elooselife()
                    print("Spider has lost a life")
                    spider.health = 100
                if a.health != 0:
                                  print(f"Spider has done {damage} damage")
                                  a.health = a.health -  damage
                else: 
                                     print(f"Spider hsa done {damage} damage and you lost a life")
                                     a.lives = a.lives -1
                                     a.health = 100
                    

        if spider.qlives == 0:
            print("Spider has died congrats player")
            arc = False
#p.findpath()
run()
