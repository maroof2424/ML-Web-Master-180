const form = document.querySelector("#predict-form");
const loader = document.querySelector("#loader");
const resultBox = document.querySelector("#result");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  resultBox.classList.add("hidden");

  const data = {
    pregnancies: Number(document.querySelector("#pregnancies").value),
    glucose: Number(document.querySelector("#glucose").value),
    bp: Number(document.querySelector("#bp").value),
    skin: Number(document.querySelector("#skin").value),
    insulin: Number(document.querySelector("#insulin").value),
    bmi: Number(document.querySelector("#bmi").value),
    dpf: Number(document.querySelector("#dpf").value),
    age: Number(document.querySelector("#age").value),
  };

  loader.classList.remove("hidden");

  try {
    const res = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data),
    });

    if (!res.ok) throw new Error("Backend error");

    const output = await res.json();
    showResult(output.prediction);

  } catch (err) {
    showError("API Error. Try again.");
  } finally {
    loader.classList.add("hidden");
  }
});

function showResult(pred) {
  resultBox.classList.remove("hidden");

  if (pred === 1) {
    resultBox.textContent = "Diabetic 😔";
    resultBox.className = "result bad";
  } else {
    resultBox.textContent = "Not Diabetic 😄";
    resultBox.className = "result ok";
  }
}

function showError(msg) {
  resultBox.classList.remove("hidden");
  resultBox.textContent = msg;
  resultBox.className = "result bad";
}
