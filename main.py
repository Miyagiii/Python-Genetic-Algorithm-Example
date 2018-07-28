
# Coded by Apathy/TheSpaceCowboy
# Git: https://www.github.com/thespacecowboy42534
# Date: 28/07/18
# A simple genetic algorithm example

#Imports
from Population import Person
import random

#Globals
endProduct = [] # Holds the end product of the algorithm
 # Stores the words input by the user in in binary format this is because there are less combinations of binary characters than there are ascii
 # Aswell as this its stored as seperate items so i can at each letter individually this may be less efficent although through my testing this
 # was faster for me.
PHRASES = []

POPLEN = 450 # Stores population length (450 appears to be when the algorithm loses efficency 
population = [] # Stores the entire population 

def retPhrase(phrase): # This function converts the text to binary
    for x in range(len(phrase)):
        PHRASES.append(bin(ord(phrase[x].replace(" ","_"))).replace("0b",""))
    
def generatePopulation(PHRASE): # This function generates a person and appeneds them to the population list
    for x in range(POPLEN):
        population.append(Person(len(PHRASE)))

def fitness(PHRASE): # Runs the fitness function on all of the people
    for people in population:
        people.calcFitness(PHRASE)
        
def evaluation(gen,PHRASE): # The evaluation stage which pretty much just sorts the population by fitness and displays information
    population.sort(key=lambda x: x.fitness, reverse=True)
    print("Best of generation",gen,":",chr(int(population[0].dna,2)),population[0].fitness)
    print("Goal: "+chr(int(PHRASE,2)))

def crossover():
    pool = [] # Creates a pool of potential parents
    for pop in population: 
        for x in range(int(pop.fitness)):
            pool.append(pop)
    # Selects 2 parents and does the crossover process
    parent1 = random.choice(pool) 
    parent2 = random.choice(pool)
    population[-1] = parent1.crossover(parent2)
    
def test(endProduct, phraseCounter,PHRASE,finished,totalGen): # This test the population to see if the solution was found

    for people in population:
        if(PHRASE == people.dna): # If the Phrase is the same as the dna move onto the next phrase 
            endProduct.append(people.dna)
            del population[:] # Reset population
            
            phraseCounter+=1
            
            if(finished <= phraseCounter): # If the phrase counter is the same as or higher than the length of the phrase end the program
                    text = ""
                    for people in endProduct:
                        text += chr(int(people,2))
                        
                    print("Finished: "+text+" in a total of "+str(totalGen)+" generations with "+str((len(PHRASES)/totalGen)*100)+"% efficency")
                    exit()
            return phraseCounter,True,True
    return phraseCounter,False,False

    

       


def main(): # The main loop of the program which runs all the functions above one after another
    # Local variables I had to do this because I need to set some of these variables however if I directly set them while they are outside of the scope
    # of the function python seems to make it a local variable which breaks the program maybe I can fix this later but for right now this works
    phraseCounter = 0 # Controls which phrase we are working on first
    PHRASE = PHRASES[phraseCounter] # Initalisation of the phrase
    finished = len(PHRASES) # Finished is the length of the 
    gen = 0 # Stores the current generation of the current phrase
    totalGen = 0 # Stores the total amount of generations
    generatePopulation(PHRASE) # Initalises the population
    while True:
        fitness(PHRASE) 
        evaluation(gen,PHRASE)
        crossover()
        gen+=1
        totalGen+=1
        phraseCounter,reset,flipped = test(endProduct, phraseCounter,PHRASE,finished,totalGen)
        PHRASE = PHRASES[phraseCounter]
        if(flipped): # If the phrase is changed a new generation is created
            generatePopulation(PHRASE)
        if(reset == True): # Resets the counter for the generations
            gen = 0

retPhrase(input("Input a sentence: "))
main()

