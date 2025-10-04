const movieScenes = [
  {
    image: "static/dra_luna_1.png",
    text: "Olá, exploradores! Eu sou a Dra. Luna, cientista das maravilhas da natureza!",
  },
  {
    image: "static/dra_luna_2.png",
    text: "Hoje, recebi uma mensagem URGENTE do Polvo Pingo! Ele está sendo perseguido por um tubarão!",
  },
  {
    image: "static/dra_luna_3.png",
    text: "Precisamos ajudá-lo a se camuflar! Será que ele pode mudar de cor como um camaleão?",
  },
  {
    image: "static/dra_luna_4.png",
    text: "E tem mais! A plantinha Florisbela está triste... Será que ela precisa de luz, água ou de um abraço?",
  },
  {
    image: "static/dra_luna_5.png",
    text: "Vamos descobrir juntos os segredos dos seres vivos? Cada um tem um superpoder especial!",
  },
  {
    image: "static/dra_luna_6.png",
    text: "Venham comigo para o Laboratório da Dra. Luna! Cada pergunta é uma missão... e cada erro, uma nova descoberta!",
  },
];

let currentSceneIndex = 0;

function showScene(index) {
  document.getElementById("movie-image").src = movieScenes[index].image;
  document.getElementById("movie-text").textContent = movieScenes[index].text;
  const btn = document.getElementById("next-scene-btn");
  if (index === movieScenes.length - 1) {
    btn.textContent = "🔬 Entrar no Laboratório!";
    btn.onclick = () => {
      document.getElementById("movie-screen").style.display = "none";
      document.getElementById("quiz-screen").style.display = "block";
      loadQuestions();
    };
  } else {
    btn.textContent = "▶️ Próxima Cena";
    btn.onclick = () => showScene(++currentSceneIndex);
  }
}

document.addEventListener("DOMContentLoaded", () => showScene(0));
