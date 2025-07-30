const vibracaoCtx = document.getElementById('vibracaoChart').getContext('2d');
const temperaturaCtx = document.getElementById('temperaturaChart').getContext('2d');

const vibracaoChart = new Chart(vibracaoCtx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Velocidade RMS (mm/s)',
      data: [],
      borderColor: 'red',
      tension: 0.3
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  }
});

const temperaturaChart = new Chart(temperaturaCtx, {
  type: 'line',
  data: {
    labels: [],
    datasets: [{
      label: 'Temperatura (°C)',
      data: [],
      borderColor: 'orange',
      tension: 0.3
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  }
});

function gerarSimulacao() {
  const agora = new Date().toLocaleTimeString();
  const vibracao = (Math.random() * 10 + 5).toFixed(2);
  const temperatura = (Math.random() * 30 + 40).toFixed(1);

  vibracaoChart.data.labels.push(agora);
  vibracaoChart.data.datasets[0].data.push(vibracao);
  if (vibracaoChart.data.labels.length > 20) {
    vibracaoChart.data.labels.shift();
    vibracaoChart.data.datasets[0].data.shift();
  }

  temperaturaChart.data.labels.push(agora);
  temperaturaChart.data.datasets[0].data.push(temperatura);
  if (temperaturaChart.data.labels.length > 20) {
    temperaturaChart.data.labels.shift();
    temperaturaChart.data.datasets[0].data.shift();
  }

  vibracaoChart.update();
  temperaturaChart.update();
}

setInterval(gerarSimulacao, 2000);