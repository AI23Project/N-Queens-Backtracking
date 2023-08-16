const n_queens_input = document.getElementById('n_queens_input')
const population_size = document.getElementById('population_size')
const max_generations = document.getElementById('max_generations')
const result_table = document.getElementById("queens_table");
const solved_way_options = document.querySelectorAll(".solved_way_option");
const btn = document.getElementById('btn')
const err_message = document.getElementById('error_message')
let result= [];
let solved_way = "backtracking";

const display_queens = (result) => {
  const matrix = [];
  for (let i = 0; i < result.length; i++) {
    matrix[i] = [];
    for (let j = 0; j < result.length; j++) {
      if (result[i] === j) {
        matrix[i].push("Q");
      } else {
        matrix[i].push('   ');
      }
    }
  }
  return matrix;
};

function get_selceted_solved_way() {
  solved_way_options.forEach((option) => {
    if (option.classList.contains("active")) {
      solved_way = option.dataset.way;
    }
  });
  return solved_way;
}

solved_way_options.forEach((option) => {
  option.addEventListener("click", () => {
    solved_way_options.forEach((option) => option.classList.remove("active"));
    option.classList.add("active");
  });
});

btn.addEventListener("click", (e) => {
  let url;
    e.preventDefault();
    if(n_queens_input.value < 1) {
    err_message.style.display = "block"
    }
    else {
        const click_btn = async () => {
            const res = await fetch(`${url = solved_way === "backtracking" ? `/?n_queens_input=${Math.round(n_queens_input.value)}&solved_by=backtracking` : `/?n_queens_input=${Math.round(n_queens_input.value)}&solved_by=differential_evolution&population_size=${population_size.value}&max_generations=${max_generations.value}`}`, {
              method: "POST",
            });
            const data = await res.json();
            result = data.result
            const matrix = display_queens(result);
            result_table.innerHTML = ""
            for (let i = 0; i < matrix.length; i++) {
              const row = document.createElement("tr");
              for (let j = 0; j < matrix[i].length; j++) {
                const cell = document.createElement("td");
                cell.innerHTML = matrix[i][j];
                row.appendChild(cell);
              }
              result_table.appendChild(row);
            }
          };
          click_btn()
        err_message.style.display = "none"
    }
  });
