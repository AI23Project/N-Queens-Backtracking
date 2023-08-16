import random
import numpy as np

def differential_evolution(N, POPULATION_SIZE, MUTATION_FACTOR, CROSSOVER_PROBABILITY, MAX_GENERATIONS):
    population = [np.random.randint(0, N, N) for i in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):

        fitness_values = [fitness_function(N, board) for board in population]
        best_fitness = min(fitness_values)
        best_solution = population[np.argmin(fitness_values)]
        print('Generation {}: Best fitness = {}'.format(generation, best_fitness))
        if best_fitness == 0:
            break
        offspring = []
        for i in range(POPULATION_SIZE):
            target_vector = population[i]
            mutant_vector = mutation(N, population, target_vector, MUTATION_FACTOR)
            trial_vector = crossover(N, target_vector, mutant_vector, CROSSOVER_PROBABILITY)
            offspring.append([int(x) for x in trial_vector])

        population = offspring

    queen_positions = [int(x) for x in best_solution]
    return queen_positions

def fitness_function(N, board):

    conflicts = 0
    for i in range(N):
        for j in range(i+1, N):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(i-j) == abs(board[i]-board[j]):
                conflicts += 1
    return conflicts

def mutation(N, population, target_vector, MUTATION_FACTOR):
    a, b, c = random.sample(population, 3)
    mutant_vector = np.clip(a + MUTATION_FACTOR * (np.array(b) - np.array(c)), 0, N-1).astype(int)

    return mutant_vector

def crossover(N, target_vector, mutant_vector, CROSSOVER_PROBABILITY):
    crossover_points = [random.randint(0, N-1) for i in range(N)]
    trial_vector = []
    for i in range(N):
        if random.random() < CROSSOVER_PROBABILITY or i == crossover_points[i]:
            trial_vector.append(mutant_vector[i])
        else:
            trial_vector.append(target_vector[i])
    return trial_vector

