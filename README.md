<div align="center">

# ELI5: Master Any Concept Through Active Learning 🎓

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000)](https://github.com/your-username/eli5-api) <!-- Replace with actual repo link -->
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.0-009688.svg)](https://fastapi.tiangolo.com/)
[![Instructor](https://img.shields.io/badge/Instructor-1.0.0-orange.svg)](https://github.com/jxnl/instructor)
[![Gemini LearnLM 1.5 Pro](https://img.shields.io/badge/LearnLM-1.5-red.svg)](https://deepmind.google/technologies/gemini/learnlm/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) <!-- Assuming you have a LICENSE file -->

</div>

<p align="center">
  <img src="assets/logo.png" alt="ELI5 API Banner" width="250"/>
</p>

---

## **Summary**

ELI5 (Explain Like I'm 5) is an AI-powered learning assistant designed to help users deeply understand complex topics by breaking them down and guiding them to explain concepts in their own words. Inspired by the Feynman Technique, this **stateless** API challenges users with thought-provoking hints and skeptical questions rather than direct corrections, fostering critical thinking and reinforcing comprehension through an iterative learning process managed by the client.

---

## 🤔 How It Works (Workflow)

1.  **Generate Atomic Topics:** User provides a general topic (e.g., "Quantum Physics"). The API breaks it down into smaller, manageable atomic topics (e.g., "Wave-particle duality", "Quantum entanglement").
2.  **Define Learning Goal:** User selects an atomic topic and provides their initial explanation. The API analyzes the explanation and returns a specific learning goal to the client.
3.  **Iterative Refinement:** User submits refined explanations *along with the previously generated learning goal*. The API provides feedback (skeptical questions or hints) based on the explanation and the goal.
4.  **Goal Achievement:** This client-managed loop continues. The user repeatedly calls the API with their explanation and the goal until the API indicates the explanation meets the learning goal, signifying a solid grasp of the atomic topic.

---

## ✨ Key Features

-   **🔍 General-to-Atomic Decomposition:** Converts broad subjects into specific, focused learning units.
-   **🎯 Goal-Oriented Learning:** Establishes clear learning objectives based on initial understanding, returned to the client.
-   **🤔 Socratic Feedback:** Provides guiding questions and hints instead of direct answers to stimulate deeper thinking.
-   **🔄 Iterative Refinement Loop:** Enables repeated explanation and improvement until mastery, driven by the client passing the goal state.
-   **🚫 Adjustable Rate Limiting:** Configurable rate limit per user/IP using Redis to maintain stability.
-   **🌐 Stateless Design:** Each API request contains all necessary information; no server-side session state is maintained between requests.

---

## 🛠 Tech Stack

ELI5 API leverages modern and efficient technologies:

-   **Backend:** [FastAPI](https://fastapi.tiangolo.com/) (Python 3.11+)
-   **AI Model:** [Gemini LearnLM 1.5 Pro](https://deepmind.google/technologies/gemini/learnlm/) education fine-tuned model for topic decomposition, goal generation, and feedback.
-   **Structured Output:** [Instructor](https://github.com/jxnl/instructor) for reliable LLM responses.
-   **Server:** [Uvicorn](https://www.uvicorn.org/) ASGI server.
-   **Rate Limiting:** [Redis](https://redis.io/) (Optional, for rate limiting).
-   **Deployment:** [Docker](https://www.docker.com/) & [Docker Compose](https://docs.docker.com/compose/) (Optional, for containerization.)

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3.11+
-   pip (Python package installer)
-   Docker (for Docker deployment option)
-   Docker Compose (for Docker deployment option)
-   Access to a Redis instance (Optional, only if using rate limiting)
-   API Key for Gemini (configured via environment variables)

---

## 🚀 Getting Started

### **Option 1: Running Locally**

#### 1️⃣ Clone the Repository
```bash
# Replace with your actual repository URL
git clone https://github.com/username/eli5-api.git
cd eli5-api
```
**Note:** Replace `https://github.com/username/eli5-api.git` with the actual URL of your repository.

#### 2️⃣ Install Dependencies
Make sure you have Python 3.11+ installed.
```bash
pip install -r requirements.txt
```

#### 3️⃣ Configure Environment Variables
Create a `.env` file in the root directory and add necessary configurations (e.g., Gemini API Key). If using rate limiting, add Redis connection details. Refer to `.env.example` if provided.
```dotenv
# .env
GEMINI_API_KEY=your_api_key_here
# Optional for Rate Limiting:
# REDIS_HOST=localhost
# REDIS_PORT=6379
# Add other relevant variables
```

#### 4️⃣ Run the Server
```bash
uvicorn main:app --reload
```

#### 5️⃣ Access API Documentation
Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to interact with the API via Swagger UI.

---

### **Option 2: Using Docker**

#### 1️⃣ Clone the Repository
```bash
# Replace with your actual repository URL
git clone https://github.com/username/eli5-api.git
cd eli5-api
```
**Note:** Replace `https://github.com/username/eli5-api.git` with the actual URL of your repository.

#### 2️⃣ Configure Environment Variables
Ensure your `docker-compose.yml` file correctly references an `.env` file or has environment variables set for the API service (Gemini Key, Redis details if using rate limiting, etc.). Create/update the `.env` file as needed (see Option 1, Step 3).

#### 3️⃣ Run with Docker Compose
Make sure Docker and Docker Compose are installed and running.
```bash
# If using Redis for rate limiting, ensure it's defined in docker-compose.yml
docker-compose up -d --build
```
This command builds the images (if necessary) and starts the API service (and optionally Redis) in detached mode.

#### 4️⃣ Access API Documentation
Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

## 📰 API Endpoints

The core API endpoints are:

| Endpoint              | Method | Description                                                                                   |
| --------------------- | ------ | --------------------------------------------------------------------------------------------- |
| `/generate-topics`    | `POST` | Generates atomic subtopics from a general topic.                                              |
| `/start-session`      | `POST` | Analyzes an initial explanation for an atomic topic and returns a learning goal to the client. |
| `/submit-explanation` | `POST` | Submits a refined explanation *and the learning goal* and receives feedback/goal status.      |

➡️ **For detailed request/response models and interactive testing, visit the API documentation:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 💪 Contributing

Contributions are welcome and greatly appreciated! To contribute:

1.  Fork the Project repository.
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the Branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

Please ensure your code adheres to standard practices and includes tests where applicable.

Star the repo if you find it useful! ⭐

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details. Free to use, modify, and distribute!

---

🚀 **ELI5 API – Master anything by explaining it simply.**
