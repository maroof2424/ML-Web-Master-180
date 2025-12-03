document.getElementById("predictBtn").addEventListener("click", async () => {

    // Collect values
    const data = {
        pregnancies: Number(document.getElementById("pregnancies").value),
        glucose: Number(document.getElementById("glucose").value),
        bp: Number(document.getElementById("bp").value),
        bmi: Number(document.getElementById("bmi").value),
        age: Number(document.getElementById("age").value)
    };

    const resultEl = document.getElementById("result");
    const loaderEl = document.getElementById("loader");

    // Input validation
    for (let key in data) {
        if (!data[key]) {
            resultEl.innerText = `Please enter ${key}`;
            resultEl.style.color = "orange";
            return;
        }
    }

    // Show loader
    loaderEl.classList.remove("hidden");
    resultEl.innerText = "";

    try {
        const response = await fetch("https://your-backend.herokuapp.com/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const output = await response.json();

        // Hide loader
        loaderEl.classList.add("hidden");

        // Show result
        if (output.prediction === 1) {
            resultEl.innerText = "Result: Diabetic";
            resultEl.style.color = "red";
        } else {
            resultEl.innerText = "Result: Not Diabetic";
            resultEl.style.color = "green";
        }

    } catch (error) {
        loaderEl.classList.add("hidden");
        resultEl.innerText = "Error: Could not connect to backend!";
        resultEl.style.color = "orange";
        console.log(error);
    }
});
