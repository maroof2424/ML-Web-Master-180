document.getElementById("predictBtn").addEventListener("click", async () => {
    
    const data = {
        pregnancies: Number(document.getElementById("pregnancies").value),
        glucose: Number(document.getElementById("glucose").value),
        bp: Number(document.getElementById("bp").value),
        bmi: Number(document.getElementById("bmi").value),
        age: Number(document.getElementById("age").value)
    };

    const resultEl = document.getElementById("result");
    resultEl.innerText = "Predicting...";

    try {
        const response = await fetch("https://your-backend.herokuapp.com/predict", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(data)
        });

        const output = await response.json();

        if (output.prediction === 1) {
            resultEl.innerText = "Result: Diabetic";
            resultEl.style.color = "red";
        } else {
            resultEl.innerText = "Result: Not Diabetic";
            resultEl.style.color = "green";
        }

    } catch (error) {
        resultEl.innerText = "Error: Could not connect to backend!";
        resultEl.style.color = "orange";
        console.log(error);
    }
});
