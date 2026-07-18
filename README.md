https://orcid.org/my-orcid?orcid=0009-0004-1872-1153
https://doi.org/10.5281/zenodo.21431640
-------------
# GRA-Genius-Agent

Intelligent agent based on GRA-Obnulenka principle: balances structural stability and entropy to maximize "interest" (I = S · E).  
Filters out states with S < S_crit. Demonstrates superior creativity in dialogue and symbolic regression tasks.

## How it works
- For each candidate response, compute stability S and entropy E.
- Apply GRA filter: discard candidates with S < S_crit.
- Select candidate with maximal I = S · E.

## Tech Stack
- Python 3.10, FastAPI, Uvicorn
- Frontend: pure HTML/CSS/JS
- Containerization: Docker, docker-compose

## Quick Start (Docker)
```bash
docker-compose up --build
```
Then open http://localhost:8000

## Manual Run
```bash
pip install -r requirements.txt
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
Open frontend/index.html in browser.

## Configuration
Edit `backend/config.py` to adjust:
- `S_CRIT` – stability threshold
- `LAMBDA_WEIGHTS` – hierarchical level weights
- `MODEL_NAME` – LLM for candidate generation (if used)

## Future Work
- Integrate with Llama 3 / Mistral for richer candidates
- Reinforcement learning based on interest
- Multi-agent collaboration

## License
MIT
