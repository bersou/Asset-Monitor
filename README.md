# Monitor de Ativos (Preditivo)

Este projeto simula o funcionamento de um sensor de ativos preditivo, com coleta, análise e visualização de dados de vibração e temperatura.

## Componentes:
- `sensor_simulator.py`: Gera dados simulados.
- `api_server.py`: Fornece dados via API REST.
- `index.html`, `style.css`, `script.js`: Dashboard interativo com gráficos.

## Como rodar:
```bash
pip install flask
python sensor_simulator.py  # Em um terminal
python api_server.py        # Em outro terminal
```

Abra `index.html` no navegador.
https://monitor-de-ativos.onrender.com
