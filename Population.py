# Coded by Apathy/TheSpaceCowboy
# Git: https://www.github.com/thespacecowboy42534
# Date: 28/07/18
# A simple genetic algorithm example

# Imports
import string,random

class Person:
    
    def __init__(self, length : int):
        self.dna = ''.join(random.choices(['0','1'], k=length)) # Random binary dna
        self.fitness = float(0) # Fitness
        self.mutateRate = 0.1 # How likely it is to mutate
        
    def calcFitness(self,phrase : str): # Calculates the fitness by seeing how many digits are in the correct place and adding that to a score which is divided by the
                                        # Length of the phrase to give a fitness percentage
        fit = 0
        for x in range(len(phrase)):
            if(phrase[x] == self.dna[x]):
                fit+= 1
        self.fitness = (fit/len(phrase))* 100

    def crossover(self,person): # Crossover takes a random amount of genes from each parent and makes a baby
        babyDNA = ""
        genes = person.dna+self.dna
        babyDNA = ''.join(random.choices(population=(genes),k=len(person.dna)))
        baby = Person(len(person.dna))
        baby.setDNA(str(babyDNA))
        baby.mutate()
        return baby
    def setDNA(self,genes : str): # Allows me to manually set dna
        self.dna = genes
        
    def mutate(self): # Mutation factor to add diversity to the population
        if(random.uniform(0,1)<= self.mutateRate):
            temp = list(self.dna)
            temp[random.randint(0,len(self.dna)-1)] = ''.join(random.choices(['0','1']))
            self.dna = ''.join(temp)
        
