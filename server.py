from flask import Flask, render_template, request, jsonify
import numpy as np
from backtracking import backtracking, is_safe
from nQueensDE import differential_evolution, fitness_function, mutation, crossover

app = Flask(__name__)

@app.route('/')
def render_server():
    return render_template('n-queens.html')


@app.route('/', methods=['POST'])
def solve_n_queens():
    if request.method == 'POST':
        n_queens_input = request.args.get('n_queens_input', type=int)
        solved_by = request.args.get('solved_by', type=str)
        population_size = request.args.get('population_size', type=int)
        max_generations = request.args.get('max_generations', type=int)
        result = None 
        if solved_by == "backtracking":
            result =  backtracking(n_queens_input)
        elif solved_by == "differential_evolution":
            queen_positions = differential_evolution(n_queens_input, population_size, 0.5, 0.7, max_generations)
            result = queen_positions
            print('Queen positions:')
            print(result) 
    return jsonify({"state_code": 200, "n_queens_input": n_queens_input, "result": result, "solved_by": solved_by})


if __name__ == "__main__":
    app.run(debug=True, port=4000)
