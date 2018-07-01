import random

class Die:
    '''Die class'''

    def __init__(self,sidesParam=6):
        '''Die([sidesParam])
        creates a new Die object
        int sidesParam is the number of sides
        (default is 6)
        -or- sidesParam is a list/tuple of sides'''
        # if an integer, create a die with sides
        #  from 1 to sides
        if isinstance(sidesParam,int):
            sidesParam = range(1,sidesParam+1)
        self.sides = list(sidesParam)
        self.numSides = len(self.sides)
        # roll the die to get a random side on top to start
        self.roll()

    def __str__(self):
        '''str(Die) -> str
        string representation of Die'''
        return 'A ' + str(self.numSides) + '-sided die with ' + \
               str(self.get_top()) + ' on top'

    def roll(self):
        '''Die.roll()
        rolls the die'''
        # pick a random side and put it on top
        self.top = self.sides[random.randrange(self.numSides)]

    def get_top(self):
        '''Die.get_top() -> object
        returns top of Die'''
        return self.top

    def set_top(self,value):
        '''Die.set_top(value)
        sets the top of the Die to value
        Does nothing if value is illegal'''
        if value in self.sides:
            self.top = value
    def sum_tops(self,dieList):
        '''sum_tops(dieList) -> object
        returns the sum of the tops of the dice in dieList'''
        return sum([die.get_top() for die in dieList])  
    def add(self,other):
        '''Die.add(Die) -> object
        returns the sum of the two dice's tops'''
        return self.top + other.top    
    def flip(self):
        top_index = self.sides[self.top - 1] - 1
        print (top_index)
        reversed_sides = self.sides
        reversed_sides = reversed_sides[::-1]
        print (reversed_sides)
        return reversed_sides[top_index]  

def decathlon_400_meters():
    '''decathlon_400_meters() -> int
    plays a solitare version of Reiner Knizia's 400 Meters
    returns final score'''
    # initializes rerolls, score, and dice
    score = 0
    rerolls = 5
    d1 = Die([1,2,3,4,5,-6])
    d2 = Die([1,2,3,4,5,-6])
    # play 4 rounds
    for gameround in range(1,5):
        print("Your total score so far is "+str(score))
        print("Round " + str(gameround) + " -- you have " + \
              str(rerolls) + " rerolls left.")
        while True:
            # roll the dice
            input("Press enter to roll.")
            d1.roll()
            d2.roll()
            roundscore = d1.get_top() + d2.get_top()
            print("You rolled " + str(d1.get_top()) + " and " + \
                  str(d2.get_top()) + " for a total of " + str(roundscore))
            # if the player has no rerolls, they're stuck with this
            if rerolls==0:
                print("You're out of rerolls so you have to keep this.")
                break
            # see if they want to reroll
            response = 'x'
            while response.lower() not in 'yn':
                response = input("Do you want to reroll (y/n)? ")
            if response.lower() == 'n':
                break  # keeping this roll, move on the the next roll
            # they're using a reroll
            rerolls -= 1
            print("OK, you have "+str(rerolls)+" rerolls left.")
        score += roundscore  # update the score
    return score