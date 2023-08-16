const n_queens_input = document.getElementById('n_queens_input')
const population_size = document.getElementById('population_size')
const max_generations = document.getElementById('max_generations')
const solved_way_options = document.querySelectorAll(".solved_way_option");
const btn = document.getElementById('btn')
const err_message = document.getElementById('error_message')
const result_div = document.getElementById("result")
let result= [];
let solved_way = "backtracking";


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
          console.log(solved_way);
            const res = await fetch(`${url = solved_way === "backtracking" ? `/?n_queens_input=${Math.round(n_queens_input.value)}&solved_by=backtracking` : `/?n_queens_input=${Math.round(n_queens_input.value)}&solved_by=differential_evolution&population_size=${population_size.value}&max_generations=${max_generations.value}`}`, {
              method: "POST",
            });
            const data = await res.json();
            result = data.result
            console.log(result);
            result_div.innerHTML = ""
            result_div.innerHTML += result
          };
          click_btn()
        err_message.style.display = "none"
    }
  });
  // 
