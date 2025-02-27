document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("bmiForm").addEventListener("submit", function (event) {
        event.preventDefault();

        let age = document.getElementById("age").value;
        let gender = document.getElementById("gender").value;
        let weight = document.getElementById("weight").value;
        let height = document.getElementById("height").value;

        fetch("/api/recommend", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ age, gender, weight, height })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById("bmiValue").textContent = `BMI: ${data.bmi}`;
            document.getElementById("bmiDescription").textContent = data.recommendations.description;

            let tipsContainer = document.getElementById("tipsContainer");
            tipsContainer.innerHTML = "<h3>Tips:</h3><ul>" + 
                data.recommendations.tips.map(tip => `<li>${tip}</li>`).join("") + "</ul>";

            let foodRec = data.recommendations.food_recommendations;
            document.getElementById("foodRecommendations").innerHTML = `
                <h3>Food Recommendations:</h3>
                <p><strong>Breakfast:</strong> ${foodRec.breakfast}</p>
                <p><strong>Lunch:</strong> ${foodRec.lunch}</p>
                <p><strong>Dinner:</strong> ${foodRec.dinner}</p>
            `;
        })
        .catch(error => console.error("Error fetching recommendations:", error));
    });
});
