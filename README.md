# 📚 Multi-PDF RAG System
### Intelligent Document Question Answering with Retrieval-Augmented Generation

<p align="center">
  <strong>Upload documents. Ask questions. Get context-aware AI answers.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-Framework-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Django%20REST%20Framework-API-red?style=for-the-badge&logo=django" alt="Django REST Framework"/>
  <img src="https://img.shields.io/badge/JWT-Authentication-black?style=for-the-badge" alt="JWT"/>
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" alt="In Development"/>
</p>

---

## 🚀 Overview

**Multi-PDF RAG System** is an AI-powered document question-answering project designed to help users retrieve relevant information from multiple PDF documents using Retrieval-Augmented Generation (RAG).

Instead of manually searching through lengthy documents, users will be able to upload PDFs, ask natural-language questions, and receive answers grounded in relevant document content.

The backend is being developed with **Django REST Framework**, JWT-based authentication, and a modular API architecture designed to support document management, retrieval, and AI-powered conversations.

> 🎯 **Project goal:** Build a modular, secure, and extensible backend for interacting intelligently with information contained in multiple PDF documents.

## ✨ Key Features

### 🔐 Authentication and API Security
- User registration and login endpoints.
- JWT-based authentication using access and refresh tokens.
- Protected user profile endpoint.
- Versioned REST API structure.

### 📄 Document Management — In Development
- PDF upload and validation.
- Document ownership and management.
- Text extraction and chunking pipeline.
- Preparation of document content for semantic retrieval.

### 🧠 Retrieval-Augmented Generation — Planned
- Generate embeddings from document chunks.
- Retrieve semantically relevant passages.
- Use retrieved context to generate answers.
- Support question answering across multiple documents.

### 💬 AI Conversations — Planned
- Conversation and message management.
- Context-aware question-answering workflows.
- Document-grounded responses.
- Potential source references for generated answers.

## 🏗️ System Architecture

The intended processing pipeline is:

```text
                  CLIENT / FRONTEND
                         |
                         v
                  Django REST API
                         |
             +-----------+-----------+
             |                       |
             v                       v
      JWT Authentication       PDF Management
                                     |
                                     v
                             PDF Text Extraction
                                     |
                                     v
                               Text Chunking
                                     |
                                     v
                              Embeddings
                                     |
                                     v
                              Vector Store
                                     |
User Question ----------------------+
             |
             v
      Semantic Retrieval
             |
             v
      Relevant Context
             |
             v
        LLM Generation
             |
             v
       AI Answer + Sources
```

*This diagram represents the target architecture. Components beyond the currently implemented authentication layer are part of the development roadmap.*

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Application framework |
| Django REST Framework | REST API development |
| SimpleJWT | Access and refresh token authentication |
| PostgreSQL | Relational database target |
| Git & GitHub | Version control and collaboration |
| RAG, embeddings and vector search | Planned document intelligence pipeline |
| Large Language Models (LLMs) | Planned answer generation |

## 📁 Project Structure

```text
Multi-Pdf-Rag-System/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── collection/
│   └── ...
│
├── documents/
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── .gitignore
├── requirements.txt
└── README.md
```

*The structure above highlights the main project components; individual files may evolve as development progresses.*

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MAhmad253/Multi-Pdf-Rag-System.git
cd Multi-Pdf-Rag-System
```

### 2. Create and activate a virtual environment

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use your existing activated virtual environment instead.

### 3. Install dependencies

If `requirements.txt` is present:

```bash
python -m pip install -r requirements.txt
```

If it is not present yet, install your project's actual dependencies and generate the file from the environment in which the project runs:

```bash
python -m pip freeze > requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file and configure the variables expected by your Django settings.

For example:

```dotenv
SECRET_KEY=replace-with-a-local-secret
DEBUG=True
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost
DB_PORT=5432
```

These names are examples. Make sure they match the variables your `config/settings.py` actually reads.

**Security:** Never commit your real `.env` file, database credentials, or production secret key. Keep `.env` in `.gitignore`.

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The local API server will be available at:

`http://127.0.0.1:8000/`

## 🔌 API Endpoints

The backend uses a versioned API structure.

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/v1/auth/register/` | Register a user |
| POST | `/api/v1/auth/login/` | Obtain JWT tokens |
| POST | `/api/v1/auth/refresh/` | Refresh an access token |
| GET | `/api/v1/auth/me/` | Retrieve the authenticated user's profile |
| POST | `/api/v1/documents/` | Planned document upload endpoint |
| GET | `/api/v1/documents/` | Planned document listing endpoint |
| POST | `/api/v1/chat/` | Planned conversational endpoint |
| POST | `/api/v1/search/` | Planned semantic search endpoint |

*Authentication endpoints reflect the current implementation described in this project. The document, chat, and search routes are planned and should not be considered operational until implemented and tested.*

### Authentication Flow

```text
Register
   |
   v
Login with credentials
   |
   v
Receive Access + Refresh Tokens
   |
   v
Send Access Token in Authorization Header
   |
   v
Access Protected Endpoints
```

For protected requests, the expected header is:

```http
Authorization: Bearer YOUR_ACCESS_TOKEN
```

## 🗺️ Development Roadmap

- [x] Initial Django project structure
- [x] Accounts application and custom user model
- [x] User registration and login APIs
- [x] JWT access and refresh token endpoints
- [x] Protected user profile endpoint
- [x] GitHub repository and version control setup
- [ ] Complete and test document upload API
- [ ] Add PDF validation and file storage
- [ ] Implement PDF text extraction
- [ ] Build a text chunking pipeline
- [ ] Integrate an embedding model and vector store
- [ ] Implement semantic search
- [ ] Integrate an LLM for grounded answers
- [ ] Add conversations and message history
- [ ] Add automated tests and API documentation
- [ ] Containerize and prepare for deployment

## 🧪 Testing

API endpoints can be tested using Postman or another REST API client.

Recommended test coverage as the project grows:

- Registration validation and duplicate-user handling.
- Login success and invalid credentials.
- JWT authentication and token expiration.
- Unauthorized access to protected endpoints.
- Document type, size, and upload validation.
- User-specific document access permissions.
- Retrieval relevance and answer grounding.
- Error handling and API response consistency.

## 🔒 Security Considerations

Security is an important part of the backend design.

- Keep secrets and credentials in environment variables.
- Protect private endpoints with authentication and appropriate permissions.
- Restrict users to their own documents and conversations.
- Validate uploaded files and enforce upload size limits.
- Use HTTPS and production-safe Django settings when deployed.
- Avoid exposing sensitive document content in logs or error responses.

These controls should be implemented and verified before the system is considered production-ready.

## 🎯 Learning and Engineering Goals

This project is an opportunity to apply practical backend and AI engineering concepts, including:

- REST API design and versioning.
- Authentication and authorization.
- Relational database modeling.
- File handling and document processing.
- Semantic search and vector retrieval.
- Retrieval-Augmented Generation.
- Modular application architecture.
- Git branching, code review, and collaborative development.

## 🤝 Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Commit with a descriptive message.
5. Open a Pull Request for review.

Example:

```bash
git switch -c feature/document-upload
git add .
git commit -m "Add document upload API"
git push -u origin feature/document-upload
```

## 👨‍💻 Author

**Ahmad — AI & Backend Development**

Building practical applications with Python, Django REST Framework, and Generative AI.

- GitHub: [@MAhmad253](https://github.com/MAhmad253)
- Project Repository: [Multi-Pdf-Rag-System](https://github.com/MAhmad253/Multi-Pdf-Rag-System)

---

<p align="center">
  <strong>Building the foundation for intelligent document understanding.</strong>
  <br/>
  <sub>From secure REST APIs to context-aware AI — one component at a time.</sub>
</p>
