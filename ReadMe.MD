# Probatio – AI-Powered Python Test Runner

**Probatio** is a full-stack automated testing app that lets users upload Python scripts and apply intelligent testing strategies — like unit tests, property-based tests, and smart random input fuzzing. This is a portfolio-ready QA project built with React + FastAPI + Pytest + Hypothesis + AST.

---

## Features

- Upload `.py` files via drag-and-drop or browse
- Run:
  - Unit tests (via Pytest)
  - Property-based tests (via Hypothesis)
  - Random testing (AST-based argument detection)
- See live test output with:
  - Function-level PASS/FAILs
  - Error messages
  - Input values used
- Summary statistics: per-function pass/fail ratios
- Toggle dark/light mode
- Responsive UI with animations

---

## Tech Stack

---

### Web Client (React)

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)

---

### API Server (FastAPI)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-121212?style=for-the-badge&logo=uvicorn&logoColor=white)

---

### Testing & Backend Logic

![Pytest](https://img.shields.io/badge/Pytest-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Hypothesis](https://img.shields.io/badge/Hypothesis-E83E8C?style=for-the-badge&logo=python&logoColor=white)
![AST Parsing](https://img.shields.io/badge/AST-6C3483?style=for-the-badge&logo=python&logoColor=white)
![subprocess](https://img.shields.io/badge/Subprocess-1E88E5?style=for-the-badge&logo=gnubash&logoColor=white)

---

### Tooling

![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![npm](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

---


## File Structure

```bash
PROBATIO/
├── backend/
│   ├── api/routes.py
│   ├── core/test_runner.py
│   ├── engine/
│   │   ├── unit.py
│   │   ├── property.py
│   │   └── random.py
│   ├── models/schemas.py
│   ├── samples/sample1.py
│   ├── utils/file_ops.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── index.css
│   │   ├── main.tsx
│   │   └── components/
│   │       ├── FileUpload.tsx
│   │       ├── Results.tsx
│   │       ├── StrategySelector.tsx
│   │       └── ThemeToggle.tsx
│   └── index.html
├── README.md
```

---

## Getting Started

1. Clone the Repo

```bash
git clone https://github.com/YOUR_USERNAME/probatio.git
cd probatio
```

2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn main:app --reload
# Backend will run on http://localhost:8000
```

3. Frontend Setup

```bash
cd frontend
npm install
npm run dev
# Frontend runs at http://localhost:5173
```