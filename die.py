from random import random

# A Python class for a die that can be loaded/weighted on a specific side or not
class Die:
    possibilities = [1, 2, 3, 4, 5, 6]

    def __init__(self, weighted=False, weightedSide=-1, weightedProb=1/6):
        """
        :param weighted: Whether the die is weighted or not
        :param weightedSide: The side the die is weighted on
        :param weightedProb: The probability of the die landing on the weighted side
        """

        self.weighted = weighted
        self.weightedSide = weightedSide
        self.weightedProb = weightedProb
        self.nonWeigitedProb = (1 - weightedProb) / 5
        self.possibilities = [1, 2, 3, 4, 5, 6]

        try:
            self.possibilities.remove(weightedSide)
        except ValueError:
            pass
    
    def roll(self) -> int:
        """
        Roll the die and return the result
        """
        float = random()

        if self.weighted: # If the die is weighted
            if float < self.weightedProb:
                return self.weightedSide
            elif float >= self.weightedProb and float < self.weightedProb + self.nonWeigitedProb:
                return self.possibilities[0]
            elif float >= self.weightedProb + self.nonWeigitedProb and float < self.weightedProb + self.nonWeigitedProb*2:
                return self.possibilities[1]
            elif float >= self.weightedProb + self.nonWeigitedProb*2 and float < self.weightedProb + self.nonWeigitedProb*3:
                return self.possibilities[2]
            elif float >= self.weightedProb + self.nonWeigitedProb*3 and float < self.weightedProb + self.nonWeigitedProb*4:
                return self.possibilities[3]
            else:
                return self.possibilities[4]

        else: # If the die is not weighted
            if float < 1/6:
                return 1
            elif float >= 1/6 and float < 2/6:
                return 2
            elif float >= 2/6 and float < 3/6:
                return 3
            elif float >= 3/6 and float < 4/6:
                return 4
            elif float >= 4/6 and float < 5/6:
                return 5
            else:
                return 6