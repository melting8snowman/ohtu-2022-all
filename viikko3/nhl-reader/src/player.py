class Player:
    def __init__(self, name, nationality, team, goals, assists, games):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.goals = goals
        self.assists = assists
        self.games = games 
        self.points = assists + goals

    def printti(self):
        line = self.name, self.nationality
        return line
    
    def __str__(self):
        #return self.name
        return f"{self.name:20} {self.team:3} {self.goals:3} + {self.assists:3} = {self.points:3}"
    

