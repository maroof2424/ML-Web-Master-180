async function predict() {
    const f1 = parseFloat(document.getElementById("f1").value);
    const f2 = parseFloat(document.getElementById("f2").value);
    const f3 = parseFloat(document.getElementById("f3").value);

    // Temporary demo logic
    const prediction = (f1 + f2 + f3) > 50 ? "High" : "Low";

    document.getElementById("result").innerText = "Prediction: " + prediction;
}
