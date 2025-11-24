const weightInput = document.querySelector("#weight");
const heightInput = document.querySelector("#height");
const calcBtn = document.querySelector("#calcBtn");
const resultDiv = document.querySelector("#result");

calcBtn.addEventListener("click", () => {
    const weight = parseFloat(weightInput.value);
    const height = parseFloat(heightInput.value);

    if (!weight || !height) {
        resultDiv.innerText = "Please enter valid numbers!";
        resultDiv.classList.add("error");
        return;
    }

    const heightInM = height / 100;
    const bmi = weight / (heightInM * heightInM);

    resultDiv.innerText = `Your BMI is ${bmi.toFixed(2)}`;

    if (bmi < 18.5) {
        resultDiv.style.backgroundColor = "#87cefa"; // light blue
    } else if (bmi < 25) {
        resultDiv.style.backgroundColor = "#90ee90"; // light green
    } else {
        resultDiv.style.backgroundColor = "#ff7f7f"; // light red
    }
});
