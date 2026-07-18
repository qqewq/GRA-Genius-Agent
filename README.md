# GRA Genius Agent 🤖✨

**ИИ-агент, построенный на принципе гармонии энтропии и негоэнтропии (GRA-Обнулёнка).**  
Он не просто отвечает на вопросы — он выбирает наиболее **интересные** и **структурно устойчивые** ответы, имитируя гениальное мышление.

[English version below](#english-version)

---

## Русская версия

### Описание
Агент реализует архитектуру, описанную в статье «GRA-Обнулёнка: мыслящий мультиверс».  
Каждое действие (ответ) оценивается по двум критериям:
- **S** — иерархическая стабильность (структурная глубина)
- **E** — энтропия (живой хаос, разнообразие возможных продолжений)

Итоговый **интерес** вычисляется как `I = S * E`.  
Агент отбрасывает варианты с `S < S_крит` (GRA-фильтр) и выбирает тот, который максимизирует `I`.

Таким образом, агент всегда стремится к балансу между осмысленностью и новизной — ключевому свойству гениальности.

### Технологии
- **Бекенд**: Python 3.10, FastAPI, Uvicorn
- **Фронтенд**: чистый HTML + CSS + JavaScript (без фреймворков)
- **Модель**: опционально интеграция с Hugging Face Transformers (например, GPT-2 или DialoGPT) для генерации кандидатов
- **Контейнеризация**: Docker, docker-compose

### Установка и запуск

#### Через Docker (рекомендуется)
```bash
docker-compose up --build
```
После запуска откройте `http://localhost:8000` — фронтенд, API доступен на `http://localhost:8000/api`.

#### Вручную
```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Затем откройте `frontend/index.html` в браузере (или настройте статику).

### Пример использования
Отправьте агенту любое сообщение. Он сгенерирует несколько вариантов ответа (в демо-версии используются шаблоны), оценит их по `S` и `E`, отфильтрует и вернёт лучший.

### Настройка
В `backend/config.py` можно изменить:
- `S_CRIT` — порог стабильности (по умолчанию 0.5)
- `LAMBDA_WEIGHTS` — веса уровней иерархии
- `MODEL_NAME` — имя модели для генерации кандидатов (если используется)

### Архитектура
![Архитектура](docs/architecture.png) (скоро)

### Дальнейшее развитие
- Подключение реальной LLM (например, Llama 3 или Mistral) для генерации кандидатов
- Обучение с подкреплением на основе внутренней награды `I`
- Визуализация динамики `S`, `E`, `I` в реальном времени
- Интеграция с GRA-репозиториями (GRA-Core, GRA-Obnulenka)

### Лицензия
MIT © 2026

---

## English Version

### Description
The agent implements the architecture from the paper "GRA-Obnulenka: The Thinking Multiverse".  
Each action (response) is evaluated by:
- **S** — hierarchical stability (structural depth)
- **E** — entropy (lively chaos, diversity of possible continuations)

The final **interest** is `I = S * E`.  
The agent discards candidates with `S < S_crit` (GRA filter) and selects the one with highest `I`.

Thus, the agent always seeks a balance between meaningfulness and novelty — a hallmark of genius.

### Technologies
- **Backend**: Python 3.10, FastAPI, Uvicorn
- **Frontend**: plain HTML + CSS + JavaScript
- **Model**: optional integration with Hugging Face Transformers (e.g., GPT‑2, DialoGPT)
- **Containerization**: Docker, docker-compose

### Installation & Run

#### Using Docker (recommended)
```bash
docker-compose up --build
```
Then open `http://localhost:8000` for the frontend, API at `http://localhost:8000/api`.

#### Manually
```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Then open `frontend/index.html` in your browser.

### Example
Send any message. The agent will generate several candidate responses (using templates in demo), compute `S` and `E`, filter, and return the best one.

### Configuration
Edit `backend/config.py` to adjust:
- `S_CRIT` — stability threshold (default 0.5)
- `LAMBDA_WEIGHTS` — hierarchy level weights
- `MODEL_NAME` — model name for candidate generation

### Roadmap
- Integrate a real LLM (e.g., Llama 3, Mistral) for candidate generation
- Reinforcement learning with intrinsic reward `I`
- Real-time visualization of `S`, `E`, `I`
- Integration with GRA repositories (GRA-Core, GRA-Obnulenka)

### License
MIT © 2026
