# fastAPI-firestore-demo

## 🚀 Overview

This is a simple, production-style FastAPI backend application that demonstrates:

* RESTful GET endpoint using FastAPI
* Reading environment variables securely
* Returning JSON data
* Saving responses to Google Firestore

## 📊 Features

* **GET /student** endpoint that returns student business data
* **Postcode** is dynamically fetched from environment variables
* Response is **persisted in Firestore** in a collection called `responses`
* Firestore authentication handled via **Google Service Account JSON key**
* Easily extensible and beginner-friendly

## 📝 Requirements

* Python 3.8+
* `fastapi`, `uvicorn`, `google-cloud-firestore`

Install dependencies:

```bash
pip install fastapi uvicorn google-cloud-firestore
```

## 🌐 Environment Setup

1. Set your environment variable for POSTCODE:

   * Mac/Linux:

     ```bash
     export POSTCODE=12345
     ```
   * Windows:

     ```cmd
     set POSTCODE=12345
     ```

2. Download your Google Cloud service account JSON file and save it in the same folder as your script.

3. Update the file name in the code:

```python
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-credentials-file.json"
```

## 🔧 Running the App

```bash
uvicorn filename:app --reload
```

If your Python file is called `main.py`, use:

```bash
uvicorn main:app --reload
```

Then visit:

```
http://127.0.0.1:8000/address
```

Or test it in Swagger UI:

```
http://127.0.0.1:8000/docs
```

## 📃 Response Example

```json
{
  "street": "Main Street",
  "city": "Toronto",
  "country": "Canada",
  "postcode": "12345"
}
```

## 📉 Production-Style Features

* Uses **environment variables** instead of hardcoding
* Firestore DB connection via **secure credentials**
* Separation of logic into clean, testable structure
* JSON format compatible with real-world applications

## 🎥 Demo Video (Add your link here)

\[Google Drive Link to Demo Video]

## 💼 Author

Mehrin Fathima — Internship Task Submission

