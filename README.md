# Monitor de Ativos (Preditivo)

## 🚀 Demonstração Ao Vivo

**Acesse a aplicação em funcionamento:** **[https://monitor-de-ativos.onrender.com](https://monitor-de-ativos.onrender.com)**

---

Este projeto simula o funcionamento de um sensor de ativos preditivo, com coleta, análise e visualização de dados de vibração e temperatura em tempo real.

## Componentes:
- `sensor_simulator.py`: Script para gerar dados simulados e popular o banco de dados inicial.
- `api_server.py`: Aplicação Flask que serve a página principal e fornece os dados via uma API REST.
- `templates/index.html`: A estrutura HTML do dashboard.
- `static/`: Pasta contendo os arquivos de estilo (`style.css`) e de lógica do frontend (`script.js`).

## Como Rodar Localmente

1.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Gere o banco de dados inicial (se necessário):**
    ```bash
    python sensor_simulator.py
    ```

3.  **Inicie o servidor web:**
    ```bash
    python api_server.py
    ```

4.  **Acesse no navegador:** Abra seu navegador e visite `http://127.0.0.1:5000`.
