# SelfGPT

SelfGPT is a Django-based application that lets users upload PDF documents, index them into a local vector store, and ask questions about the content in natural language.

## Features

- User authentication with Django
- PDF upload and document management
- PDF ingestion into a Chroma vector store
- Retrieval-augmented question answering using Mistral
- Responsive chat interface for interacting with uploaded documents

## Project Structure

- accounts/: authentication views, forms, templates, and user account flow
- home/: document upload, chat views, and PDF management
- rag/: ingestion, chunking, embedding, retrieval, and LLM pipeline logic
- SelfGPT/: Django project settings and URL configuration

## Requirements

- Python 3.12+
- PostgreSQL
- A Mistral API key

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd SelfGPT
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If you are using the project metadata in pyproject.toml, you can also install with:

   ```bash
   pip install -e .
   ```

4. Create your environment file:

   ```bash
   cp .env.example .env
   ```

5. Update the values in .env for your local setup.

## Environment Variables

The project reads configuration from a .env file. A sample file is available in .env.example.

Required variables:

- SECRET_KEY
- DEBUG
- ALLOWED_HOSTS
- DB_NAME
- DB_USER
- DB_PASSWORD
- DB_HOST
- DB_PORT
- MISTRAL_API_KEY

Example:

```env
SECRET_KEY=change-me-to-a-strong-random-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DB_NAME=selfgpt
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=localhost
DB_PORT=5432

MISTRAL_API_KEY=your_mistral_api_key_here
```

## Database Setup

Make sure PostgreSQL is running and create a database that matches DB_NAME.

Example:

```bash
createdb selfgpt
```

## Run the Project

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Then open:

```text
http://127.0.0.1:8000/
```

## Usage

1. Create an account or log in.
2. Upload a PDF document from the home page.
3. Wait for the document to be ingested.
4. Open the document chat view and ask questions about its content.

## Notes

- The project uses Chroma for local vector storage under the chroma_db directory.
- Static files are handled with WhiteNoise.
- For production deployment, review Django security settings and environment configuration carefully.
