
import random, math

#-----------------------------------------------------------------#

def simulate(sample, start, trials):
    """ sample = number of accounts in the simulation
        start = initial account size
        trials = number of trials we're running for
    """
    
    population = []
    for num in range(sample):
        population.append(start)

    factors = [0, 1.4, 2, .7, .5]        
    day = 0
    
    while day < trials:
        for num in range(sample):
            population[num] *= random.choice(factors)
        day += 1
    
        zeroes = 0
        for num in range(sample):
            if population[num] == 0:
                zeroes += 1
                        
        print("Day: ", day)
        print("Survivors: ", sample - zeroes)
        print("Deaths: ", zeroes)
        print("Max: ", max(population))
        print("Min: ", min(population))
        print("Average: ", sum(population) / sample)
        
        if sample % 2 == 0:
            median = sorted(population)[sample // 2]
        else:
            median = sorted(population)[(sample + 1) // 2]
        print("Median: ", median)
        
        print("-----------------------------")
    
#-----------------------------------------------------------------#
    
simulate(1000, 10000, 10)


