const input = document.querySelector("#userInput");
const btn = document.querySelector("#btn");

btn.addEventListener("click", () => {
    console.log("User typed:", input.value);
});
