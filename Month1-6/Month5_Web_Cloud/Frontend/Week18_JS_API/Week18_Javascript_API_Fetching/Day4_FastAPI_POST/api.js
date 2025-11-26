const ageInput = document.querySelector("#age");
const bmiInput = document.querySelector("#bmi");
const glucoseInput = document.querySelector("#glucose");
const predictBtn = document.querySelector("#predictBtn");
const resultEl = document.querySelector("#result");

const API_URL = "http://127.0.0.1:8000/predict";

async function getPrediction() {
    const data = {
        age: Number(ageInput.value),
        bmi: Number(bmiInput.value),
        glucose: Number(glucoseInput.value)
    };

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) throw new Error("Network response was not ok");

        const result = await response.json();
        console.log("Backend response:", result);

        resultEl.innerText = `Prediction: ${result.prediction}`;

    } catch (error) {
        console.error("Error:", error);
        resultEl.innerText = "Error! Check backend or CORS settings.";
    }
}

predictBtn.addEventListener("click", getPrediction);
