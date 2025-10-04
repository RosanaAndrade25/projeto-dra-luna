let questions = [];
let currentQuestionIndex = 0;

const somErro = new Audio("static/uh-oh.mp3");
const somAcerto = new Audio("static/aplausos.mp3");

async function loadQuestions() {
  const res = await fetch("/api/questions");
  questions = await res.json();
  showQuestion(0);
}

function showQuestion(index) {
  const container = document.getElementById("quiz-container");
  const q = questions[index];
  let html = `<div class="question-text">${q.text}</div>
                <div class="image-wrapper">
                    <img class="question-image" src="${q.image_url}" alt="Ilustração">
                </div>`;
  q.options.forEach((opt) => {
    html += `<button class="option-btn" onclick="checkAnswer(${opt.id}, ${opt.is_correct})">${opt.text}</button>`;
  });
  container.innerHTML = html;
}

function checkAnswer(optionId, isCorrect) {
  const selected = questions[currentQuestionIndex].options.find(
    (o) => o.id === optionId
  );
  const feedbackDiv =
    document.getElementById("feedback") ||
    (() => {
      const div = document.createElement("div");
      div.id = "feedback";
      document.getElementById("quiz-container").appendChild(div);
      return div;
    })();
  feedbackDiv.textContent = selected.feedback;
  feedbackDiv.className = "feedback " + (isCorrect ? "correct" : "incorrect");
  feedbackDiv.style.display = "block";

  if (isCorrect) somAcerto.play();
  else somErro.play();

  const nextBtn =
    document.getElementById("next-btn") ||
    (() => {
      const btn = document.createElement("button");
      btn.id = "next-btn";
      btn.textContent = "Próxima Pergunta! 🚀";
      btn.onclick = nextQuestion;
      document.getElementById("quiz-container").appendChild(btn);
      return btn;
    })();
  nextBtn.style.display = "inline-block";

  document.querySelectorAll(".option-btn").forEach((b) => (b.disabled = true));
}

function nextQuestion() {
  currentQuestionIndex++;
  if (currentQuestionIndex < questions.length) {
    showQuestion(currentQuestionIndex);
    document.getElementById("feedback").style.display = "none";
    document.getElementById("next-btn").style.display = "none";
  } else {
    document.getElementById("quiz-container").innerHTML = `
            <div class="final-screen">
                <h2>Parabéns, Explorador Cientista! 🎉</h2>
                <p>Agora, pegue um papel, giz de cera e desenhe como você se sentiu sendo um cientista hoje! 🖍️</p>
                <img src="static/fim.png" style="max-width:100%; margin-top:20px; border-radius:15px;">
            </div>`;
  }
}
