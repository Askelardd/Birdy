function updateProgress(progress) {
    const progressText = document.getElementById('progressText');
    const fill = document.querySelector('.progress-circle-fill');

    const percentage = Math.min(progress, 100);
    progressText.innerText = `${percentage}%`;
    fill.style.transform = `rotate(${percentage / 100 * 360}deg)`;
  }

  // Exemplo: Atualiza a barra de progresso para 50% após 2 segundos
  setTimeout(() => {
    updateProgress(50);
  }, 2000);