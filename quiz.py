from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Simple Quiz App</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            #quiz-container { width: 50%; margin: auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px; background-color: #f9f9f9; }
            button { display: block; width: 100%; padding: 10px; margin: 5px 0; background-color: blue; color: white; border: none; cursor: pointer; }
            button:hover { background-color: darkblue; }
        </style>
        <script>
            let questions = [
                {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
                {"question": "Which programming language is used for web development?", "options": ["Python", "Java", "C++", "JavaScript"], "answer": "JavaScript"},
                {"question": "What is 5 + 3?", "options": ["5", "7", "8", "10"], "answer": "8"}
            ];
            let currentQuestionIndex = 0;
            let score = 0;

            function showQuestion() {
                if (currentQuestionIndex < questions.length) {
                    let q = questions[currentQuestionIndex];
                    document.getElementById("question").innerText = q.question;
                    let optionsHtml = "";
                    q.options.forEach(option => {
                        optionsHtml += `<button onclick="checkAnswer('${option}')">${option}</button><br>`;
                    });
                    document.getElementById("options").innerHTML = optionsHtml;
                } else {
                    document.getElementById("quiz-container").innerHTML = `<h2>Your Score: ${score} / ${questions.length}</h2>`;
                }
            }

            function checkAnswer(selected) {
                let correctAnswer = questions[currentQuestionIndex].answer;
                if (selected === correctAnswer) { score++; }
                currentQuestionIndex++;
                showQuestion();
            }

            window.onload = showQuestion;
        </script>
    </head>
    <body>
        <h1>Simple Quiz App</h1>
        <div id="quiz-container">
            <h2 id="question"></h2>
            <div id="options"></div>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
