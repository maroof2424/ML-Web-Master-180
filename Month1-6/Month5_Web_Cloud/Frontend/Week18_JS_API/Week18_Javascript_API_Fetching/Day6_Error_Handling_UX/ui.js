const btn = document.querySelector("#send-btn");
const input = document.querySelector("#value-input");
const loader = document.querySelector("#loader");
const alertBox = document.querySelector("#alert-box");

btn.addEventListener("click", async () => {
  const value = input.value.trim();

  if (!value) {
    showAlert("Please enter something!", "error");
    return;
  }

  btn.disabled = true;
  loader.classList.remove("hidden");
  alertBox.classList.add("hidden");

  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/posts/1000000");

    if (!response.ok) {
      throw new Error("Backend returned an error");
    }

    const data = await response.json();

    showAlert("Request Successful!", "success");
  } 
  catch (error) {
    showAlert("Something went wrong. Try again.", "error");
  } 
  finally {
    loader.classList.add("hidden");
    btn.disabled = false;
  }
});

function showAlert(msg, type) {
  alertBox.textContent = msg;
  alertBox.className = `alert ${type}`;
  alertBox.classList.remove("hidden");
}
