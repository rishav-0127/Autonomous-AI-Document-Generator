# 🤖 Autonomous AI Document Generator

An Autonomous AI Agent that understands a user's request, creates its own execution plan, generates high-quality business content using Groq LLMs, and exports the final output as a professionally formatted Microsoft Word (.docx) document.

The application provides a clean Streamlit interface and is fully containerized using Docker, making it easy to deploy on Hugging Face Spaces.

---

# 🚀 Features

- 🤖 Autonomous AI task planning
- 🧠 LLM-powered content generation using Groq (Llama 3.3 70B)
- 📄 Professional Microsoft Word (.docx) generation
- 🎯 Interactive Streamlit UI
- 🐳 Docker support
- ☁️ Hugging Face deployment ready
- 🔐 Secure API key management using environment variables
- 📥 One-click document download

---

# 📄 Supported Documents

- Business Proposal
- Technical Design Document
- Project Plan
- Standard Operating Procedure (SOP)
- Business Report
- Product Requirement Document
- Meeting Minutes
- Market Research Report
- Technical Documentation

---

# 🛠 Tech Stack

- Python 3.11
- Streamlit
- FastAPI
- Groq API
- Llama 3.3 70B Versatile
- python-docx
- Pydantic
- Docker

---

# 📁 Project Structure

```text
Autonomous-AI-Document-Generator/
│
├── app.py
├── agent.py
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
├── README.md
├── generated_docs/
└── .env (Local Only)
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/rishav-0127/Autonomous-AI-Document-Generator.git
```

Move into the project

```bash
cd Autonomous-AI-Document-Generator
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a file named

```
.env
```

Add your Groq API Key

```env
GROQ_API_KEY=your_groq_api_key
```

Example

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxx
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at

```
http://localhost:8501
```

---

# 🐳 Docker

## Build Docker Image

```bash
docker build -t autonomous-agent .
```

## Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env autonomous-agent
```

Open

```
http://localhost:8501
```

---

# ☁️ Deploy on Hugging Face

1. Create a new Hugging Face Space.
2. Select **Docker** as the SDK.
3. Connect your GitHub repository or upload the project.
4. Go to **Settings → Variables and Secrets**.
5. Add the following secret:

```
GROQ_API_KEY
```

6. Paste your Groq API key as the value.
7. Hugging Face will automatically build and deploy the application.

---

# 🧠 How It Works

1. User enters a document request.
2. The AI Agent analyzes the request.
3. A structured execution plan is created.
4. The agent executes every task sequentially.
5. Content is generated using Groq LLM.
6. All generated sections are combined.
7. A professional Microsoft Word document is created.
8. The final document is available for download.

---

# 📌 Example Prompt

```
Create a comprehensive business proposal for implementing an AI-powered hospital management system. Include an executive summary, business objectives, implementation roadmap, budget estimation, ROI analysis, security considerations, project timeline, future enhancements, and conclusion.
```

---

# 📸 Screenshots

You can add screenshots of:

- Home Page
- AI Processing
- Generated Document
- Download Button

---

# 🔮 Future Enhancements

- Retrieval-Augmented Generation (RAG)
- Multi-Agent Architecture
- PDF Export
- Memory Support
- Document Templates
- Database Integration
- Authentication
- Cloud Storage
- Vector Database Integration
- Multi-language Document Generation

---

# 💻 Tech Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
Autonomous AI Agent
   │
   ▼
Execution Planner
   │
   ▼
Groq LLM
   │
   ▼
Task Executor
   │
   ▼
DOCX Generator
   │
   ▼
Download Document
```

---

# 👨‍💻 Author

**Rishav Mehta**

AI / ML Engineer

GitHub

https://github.com/rishav-0127

LinkedIn

(Add Your LinkedIn Profile)

---

# 📜 License

MIT License

Copyright (c) 2026 Rishav Mehta

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files, to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

---

⭐ If you found this project useful, consider giving it a Star on GitHub!
