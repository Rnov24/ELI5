<div align="center">

# ELI5: Master Any Concept Through Active Learning 🎓

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.103.0-009688.svg)
![Instructor](https://img.shields.io/badge/Instructor-1.0.0-orange.svg)
![Gemini LearnLM 1.5 Pro](https://img.shields.io/badge/LearnLM-1.5-red.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

<p align="center">
  <img src="assets/logo.png" alt="Feynman API Banner" width="250"/>
</p>

---

## **Summary**
ELIS (Explain Like Im 5) is an AI-powered learning assistant designed to help users deeply understand complex topics by breaking them down and explaining them in their own words. Inspired by the Feynman Technique, this API challenges users with thought-provoking hints rather than direct corrections, fostering critical thinking and reinforcing comprehension through an iterative learning process.

---

## ✨ Key Features
- **🔍 General-to-Atomic** – Converts a broad topic into several specific atomic topics.
- **🧠 Understanding Analysis** – Determines the user's comprehension level based on their initial explanation.
- **🤔 Clue-Based Feedback** – Provides skeptical questions to help users identify gaps in their explanations.
- **🔄 Iterative Learning Until Goals Are Met** – The process repeats until the explanation meets the required standard.
- **🚀 Stateful Interaction** – Manages user session state with Redis to track progress.
- **🚫 Adjustable Rate Limiting** – Configurable rate limit per user/IP to maintain stability and flexibility.

---

## 🛠 Tech Stack
Feynman API is built using modern and efficient technologies:

- **FastAPI** – High-performance web framework for building APIs.
- **Instructor** – Structured API responses with ease.
- **Gemini 2.0** – AI model for goal generation and feedback.
- **Uvicorn** – Lightning-fast ASGI server for running FastAPI applications.
- **Redis** – Used for session management and rate limiting.
- **Docker** – Containerized deployment for scalability.

---

## 🚀 Getting Started

### **Option 1: Running Locally**

#### 1⃣ Clone the Repository
```bash
git clone https://github.com/username/feynman-api.git
cd feynman-api
```

#### 2⃣ Install Dependencies
Make sure you have Python 3.11+ installed.
```bash
pip install -r requirements.txt
```

#### 3⃣ Run the Server
```bash
uvicorn main:app --reload
```

#### 4⃣ Access API Documentation
Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

### **Option 2: Using Docker**

#### 1⃣ Clone the Repository
```bash
git clone https://github.com/username/feynman-api.git
cd feynman-api
```

#### 2⃣ Run with Docker Compose
Make sure Docker and Docker Compose are installed.
```bash
docker-compose up -d
```

#### 3⃣ Access API Documentation
Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

## 📰 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/generate_atomic` | `POST` | Generates atomic subtopics from a general topic. |
| `/start_session` | `POST` | Starts a new learning session with an atomic topic and an initial explanation. |
| `/submit_explanation` | `POST` | Submits a refined explanation and receives feedback. |
| `/check_goal` | `GET` | Checks if the learning goal has been met. |

➡️ **For detailed API documentation, visit:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 💪 Contributing

Contributions are welcome! To contribute:

1. Fork the repo.
2. Create a new branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

Star the repo and spread the word! 🚀

---

## 🦀 License
This project is released under the **MIT License**. Free to use and modify!

🚀 **Feynman API – Because the best way to learn is to teach!**
