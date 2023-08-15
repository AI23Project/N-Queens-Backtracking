import random
import numpy as np

# Define the size of the board
N = int(input("Enter the size of the board: "))

# Define the parameters for Differential Evolution
POPULATION_SIZE = 100
MUTATION_FACTOR = 0.5
CROSSOVER_PROBABILITY = 0.7
MAX_GENERATIONS = 1000

# Define the fitness function for the N-Queens problem
def fitness_function(board):
    # Count the number of conflicts (queens attacking each other)
    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(i-j) == abs(board[i]-board[j]):
                conflicts += 1
    return conflicts

# Define the mutation function for Differential Evolution
def mutation(population, target_vector):
    a, b, c = random.sample(population, 3)
    mutant_vector = np.clip(a + MUTATION_FACTOR * (np.array(b) - np.array(c)), 0, N-1).astype(int)

    return mutant_vector

# Define the crossover function for Differential Evolution
def crossover(target_vector, mutant_vector):
    crossover_points = [random.randint(0, N-1) for i in range(N)]
    trial_vector = []
    for i in range(N):
        if random.random() < CROSSOVER_PROBABILITY or i == crossover_points[i]:
            trial_vector.append(mutant_vector[i])
        else:
            trial_vector.append(target_vector[i])
    return trial_vector

# Initialize the population with random solutions
population = [np.random.randint(0, N, N) for i in range(POPULATION_SIZE)]

# Run the Differential Evolution algorithm
for generation in range(MAX_GENERATIONS):
    # Evaluate the fitness of the population
    fitness_values = [fitness_function(board) for board in population]
    best_fitness = min(fitness_values)
    best_solution = population[np.argmin(fitness_values)]
    print('Generation {}: Best fitness = {}'.format(generation, best_fitness))
    if best_fitness == 0:
        break
    # Generate offspring using Differential Evolution
    offspring = []
    for i in range(POPULATION_SIZE):
        target_vector = population[i]
        mutant_vector = mutation(population, target_vector)
        trial_vector = crossover(target_vector, mutant_vector)
        offspring.append(trial_vector)
    # Replace the population with the offspring
    population = offspring

print('Best solution found:')
for i in range(N):
    row = ['_' if j != best_solution[i]  else 'Q' for j in range(N)]
    print(' '.join(row))
