
class Player:


    def __init__(self, height, weight, age,position, team=None):
        self.height = height
        self.weight = weight
        self.age = age
        self.position = position
        if self.team==None:
            self.team = []
        else:
             self.team== team



        def add_team(self,team):
            print(f"the player is from the {team} team")




class NationalTeamPlayer(Player):
    def __init__(self,height,weight,age,position,team=None, nationalTeam=None):
                    super().__init__(height, weight, age, position, team)
                    self.nationalTeam =nt


team = ["Nuggets","Pistons", "Lakers"]
nikola = NationalTeamPlayer("nikola","2.13","113","24","center",nt)

print (nikola.nationalTeam)
