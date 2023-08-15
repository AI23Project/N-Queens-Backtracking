const dime_input = document.getElementById('dime_input')
const btn = document.getElementById('btn')
const err_message = document.getElementById('error_message')

btn.addEventListener("click", (e) => {
    e.preventDefault();
    if(dime_input.value < 1) {
    err_message.style.display = "block"
    }
    else {
        const click_btn = async () => {
            const res = await fetch(`/?dime_input=${Math.round(dime_input.value)}`, {
              method: "POST",
            });
            const data = await res.json();
            console.log(data); //
          };
          click_btn();
        err_message.style.display = "none"
    }
  });

