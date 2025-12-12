async function getPrediction() {
    const data = {
        feature1: parseFloat(document.getElementById("f1").value),
        feature2: parseFloat(document.getElementById("f2").value),
        feature3: parseFloat(document.getElementById("f3").value)
    };

    const response = await fetch("https://YOUR_BACKEND_URL/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    
    document.getElementById("result").innerText =
        "Prediction → " + result.prediction;
}
