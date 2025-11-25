const btn = document.querySelector("#loadBtn");
const titleEl = document.querySelector("#title");

const API_URL = "https://jsonplaceholder.typicode.com/posts/1";

btn.addEventListener("click", () => {

    fetch(API_URL)
        .then(response => {
            return response.json();
        })
        .then(data => {
            titleEl.innerText = data.title;
            console.log("API data:", data);
        })
        .catch(error => {
            titleEl.innerText = "Error loading data!";
            console.error("Fetch error:", error);
        });

});
