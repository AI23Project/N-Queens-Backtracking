const n_queens_input = document.getElementById('n_queens_input')
const btn = document.getElementById('btn')
const err_message = document.getElementById('error_message')
const result_div = document.getElementById("result")
let result= [];
btn.addEventListener("click", (e) => {
    e.preventDefault();
    if(n_queens_input.value < 1) {
    err_message.style.display = "block"
    }
    else {
        const click_btn = async () => {
            const res = await fetch(`/?n_queens_input=${Math.round(n_queens_input.value)}`, {
              method: "POST",
            });
            const data = await res.json();
            result = data.result
            result_div.innerHTML = ""
            result_div.innerHTML += result
          };
          click_btn()
        err_message.style.display = "none"
    }
  });

