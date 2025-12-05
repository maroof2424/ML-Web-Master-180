const API_URL = "https://<your-backend>.onrender.com/predict";

async function predict() {
  const age = document.getElementById("age").value;
  const bmi = document.getElementById("bmi").value;
  const glucose = document.getElementById("glucose").value;

  const response = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ age, bmi, glucose }),
  });

  const result = await response.json();
  document.getElementById("result").innerText =
    "Prediction: " + result.prediction;
}
