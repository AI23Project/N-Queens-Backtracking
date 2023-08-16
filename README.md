# N-Queens
an N-Queens Problem Solver using the Backtracking Algorithm

# Backtracking Algorithms
This Python code is an implementation of the N-Queens problem using the backtracking algorithm. The N-Queens problem is a puzzle where you have to place N queens on an NxN chessboard in such a way that no two queens threaten each other.

```python
def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True
```

1. The `is_safe` function checks if it is safe to place a queen at a given position on the board. It takes three parameters: the current board configuration, the row, and the column of the position being checked. It iterates over the rows above the current row and checks if any of the previously placed queens conflict with the current position. If there is a conflict, it returns `False`; otherwise, it returns `True`.

```python
def backtracking(n):
    board = [-1] * n
    row = 0

    board[0] = random.randint(0, n-1)
    
    while row < n:
        col = board[row] + 1

        while col < n:
            if is_safe(board, row, col):
                board[row] = col
                row += 1
                break
            col += 1

        if col == n:
            board[row] = -1
            row -= 1

        elif row == n:
            return board

    return None

```

2. The `backtracking` function takes a single parameter `n` representing the size of the chessboard. It initializes an empty board of size `n` and sets the first queen's position randomly on the first row.

3. It enters a while loop that continues until all queens are placed on the board. Inside the loop, it starts from the current row and tries to find a safe position by incrementing the column value. If a safe position is found, it places the queen at that position and moves to the next row. If no safe position is found in the current row, it goes back to the previous row and tries to find a different position.

4. If it reaches a point where it cannot place any queen on the board, it goes back to the previous row and tries a different position. If all rows have been explored and a valid solution is found, it returns the board configuration. Otherwise, it returns `None` if no solution is possible.

The code employs the backtracking algorithm to explore and backtrack through different configurations until a valid solution is found or all possibilities are exhausted.

### Diagrams
![block_diagram](./block_backtrack.jpeg)
![flow_diagram](./flowchart_backtrack.jpeg)


# Differential Evolution Algo

## Initialization

```python
# Define the size of the board
N = 8

# Define the parameters for Differential Evolution
POPULATION_SIZE = 100
MUTATION_FACTOR = 0.5
CROSSOVER_PROBABILITY = 0.7
MAX_GENERATIONS = 1000
```

In the first few lines of the code, we define the size of the board (N) and the parameters for Differential Evolution. These parameters include the population size (POPULATION_SIZE), the mutation factor (MUTATION_FACTOR), the crossover probability (CROSSOVER_PROBABILITY), and the maximum number of generations (MAX_GENERATIONS).

## Fitness Function

```python
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
```

The fitness function takes a board configuration as input and returns a fitness value based on how many conflicts (queens attacking each other) are present on the board. The function loops over each pair of queens on the board and checks if they are in the same row or diagonal. If they are, the conflicts counter is incremented. The lower the number of conflicts, the better the fitness value.

## Mutation Function

```python
# Define the mutation function for Differential Evolution
def mutation(population, target_vector):
    a, b, c = random.sample(population, 3)
    mutant_vector = np.clip(a + MUTATION_FACTOR * (b - c), 0, N-1)
    return mutant_vector
```

The mutation function takes a population and a target vector as input and returns a mutant vector. The function selects three random individuals from the population and generates a mutant vector by adding a scaled difference between two of them to the third one. The scaling factor is given by the mutation factor (MUTATION_FACTOR). The np.clip() function is used to keep the mutant vector within the bounds of the board size (0 to N-1).

## Crossover Function

```python
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
```

The crossover function takes a target vector and a mutant vector as input and returns a trial vector. The function selects random crossover points for each element of the vectors and generates a trial vector by selecting random elements from the mutant and target vectors. The probability of selecting an element from the mutant vector is given by the crossover probability (CROSSOVER_PROBABILITY).

## Differential Evolution Algorithm

```python
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
```

The main part of the code runs the Differential Evolution algorithm. The algorithm starts by initializing a population of random solutions. It then repeatedly generates offspring using Differential Evolution, evaluating their fitness and replacing the population with the offspring until a satisfactory solution is found or the maximum number of generations is reached.

In each generation, the fitness of the population is evaluated using the fitness function. The best fitness value and corresponding solution are tracked and printed. If the best fitness value is 0, meaning an optimal solution has been found, the algorithm stops.

To generate offspring, the algorithm loops over each individual in the population and generates a target vector. It then generates a mutant vector using the mutation function and a trial vector using the crossover function. The offspring population is built by appending the trial vectors.

Finally, the population is replaced with the offspring population, and the process continues to the next generation.

### Diagrams
![block_diagram_diff](./block_diff.jpeg)
![flow_diagram_diff](./flowchart_diff.jpeg)