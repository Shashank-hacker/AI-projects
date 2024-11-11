from random import choice 
from copy import deepcopy
class Game:
    def __init__(self):                                                       #game class, pretty much self explanatory
        self.game= [[None,None,None],[None,None,None],[None,None,None]]
        self.player= "o"
        self.moves= [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
        self.utility= 0
    def move(self,mov):                                #makes a move 
        if mov  not in self.moves:
            raise Exception("Invalid Move")
        else:
            self.switch()
            self.game[mov[0]][mov[1]]= self.player
            self.utility=self.check()
            self.moves.remove(mov)
    def switch(self):                              #used for switching the player after making a move
        if self.player=="x":
            self.player="o"
        else:
            self.player="x"
    def check(self):                              #used to check if the game is over or not
        x= self.game
        for i in x:
            if i[0]==i[1]==i[2] and i[0]!=None:
                return 1 if self.player=='x' else -1        
        for i in range(3):
            if x[0][i]==x[1][i]==x[2][i]!=None:
                return 1 if self.player=='x' else -1
        if x[0][0]==x[1][1]==x[2][2]!=None or x[0][2]==x[1][1]==x[2][0]!=None:
            return 1 if self.player=='x' else -1
        return 0
    def show(self):
        for row in self.game:
            print(" | ".join(cell if cell is not None else " " for cell in row))
            print("---------")            
    #I coded a lot of static functions for making it easier to code minvalue and maxvalue and aimin functions.. I don't know if they were necessary or not
    @staticmethod
    def actions(game):                                #takes game as input and returns out all available moves
        aas=game
        a=[]
        for index1,i in enumerate(aas):
            for index2,j in enumerate(i):
                if j is None:
                    a.append((index1,index2))
        return a
    @staticmethod
    def result(game,action):                            #takes a state and a move and returns the resulting state
        b= deepcopy(game)
        b[action[0]][action[1]]= Game.player(game)
        return b
    @staticmethod
    def utilitycheck(x):                      #takes a state and tells it's utility (-1 is o wins 0 if no one wins or game hasn't ended)
        for i in x:
            if i[0]==i[1]==i[2] and i[0]!=None:
                return 1 if Game.player(x)=='x' else -1        
        for i in range(3):
            if x[0][i]==x[1][i]==x[2][i] and x[0][i]!=None:
                return 1 if Game.player(x)=='x' else -1
        if (x[0][0]==x[1][1]==x[2][2] or x[0][2]==x[1][1]==x[2][0]) and x[1][1]!=None:
            return 1 if Game.player(x)=='x' else -1
        return 0    
    @staticmethod
    def player(game):                        #takes a state and returns who's move is it
        x=0
        y=0
        for i in game:
            for j in i:
                if j=="x":
                    x+=1
                elif j=="o":
                    y+=1
        if x==y:
            return "x"
        return "o"
    @staticmethod
    def minvalue(game):                                                     #takes a game and returns it's minimum value that can be achieved if opponent plays optimally
        if Game.terminal(game):                                            #checking if game is over
            return Game.utilitycheck(game)
        v=1                                                  #setting the initial value of v to be the maximum it could be
        for action1 in Game.actions(game):                                    #running a loop with actions
            v=min(v,Game.maxvalue(Game.result(game,action1)))                 #v would be equal to minmum of current v and the maximum value achievable in the next state as the opposite player will try to play optimally
        return v                                                            #returning v
    @staticmethod
    def maxvalue(game):                        #maxvalue which will return maximum value of a state 
        if Game.terminal(game):                #checking if game has already ended
            return Game.utilitycheck(game)  
        v=-1                     #setting inital value of v to be as minimum as it could be
        for action1 in Game.actions(game):                            #running a loop in actions 
            v=max(v,Game.minvalue(Game.result(game,action1)))         #v would be equal to maximum value of current v and minimum value returned by that action's state as opponent will play to oppose
        return v                                                      
    @staticmethod
    def terminal(game):         #checks if the game has already ended or not
        if Game.utilitycheck(game)==0:
            for i in game:
                for j in i:
                    if j==None:
                        return False 
        return True 
#diffrent gamemodes irrevelant to the main problem
def twoplayer():
    gam= Game()
    while gam.utility==0:
        if gam.moves==[]:
            print("The game has ended in a draw")
            break
        gam.show()
        gam.move(tuple(int(i) for i in input("Enter the coordinates of the square you wanna play in(rc): ")))
        if gam.utility==1:
            gam.show()
            print("x wins")    
            break
        gam.show()
        gam.move(tuple(int(i) for i in input("Enter the coordinates of the square you wanna play in(rc): ")))
        if gam.utility==-1:
            gam.show()
            print("o wins")
            break
def noobai():
    gam= Game()
    while gam.utility==0:
        if gam.moves==[]:
            print("The game has ended in a draw")
            break
        gam.show()
        gam.move(tuple(int(i) for i in input("Enter the coordinates of the square you wanna play in(rc): ")))
        if gam.utility==1:
            gam.show()
            print("x wins")    
            break
        gam.move(choice(gam.moves))
        if gam.utility==-1:
            gam.show()
            print("o wins")
            break
def aimin(game):
    best_action = None
    best_score = float('-inf')  # Start with the lowest possible score for maximizing player
    for action in Game.actions(game):
        score = Game.minvalue(Game.result(game, action))  # Get the score for the minimizing player
        if score > best_score:  # We're looking for the maximum score
            best_action = action
            best_score = score
    return best_action
def proaix():                            #Just logic to play the game against the ai
    gam= Game()
    while gam.utility==0:
        if gam.moves==[]:
            print("The game has ended in a draw")
            break
        gam.show()
        gam.move(tuple(int(i) for i in input("Enter the coordinates of the square you wanna play in(rc): ")))
        if gam.utility==1:
            gam.show()
            print("x wins")    
            break
        gam.move(aimin(gam.game)) #here we're calling aimin function on game to get the best possible move for o
        if gam.utility==-1:
            gam.show()
            print("o wins")
            break
def main():
    a= input("Enter 1 for twoplayer, 2 for noobai, 3 for perfect ai: ")
    match a:
        case "1":
            twoplayer()
        case "2":
            noobai()
        case "3":
            proaix()
if __name__=="__main__":
    main()
    input()
