# URL Shortener with Redirection API

This project is a simple URL shortener service built with FastAPI. It allows users to shorten long URLs and provides a way to redirect them back to their original URLs using the shortened link.

## Project Overview

The project consists of two main APIs:

1. **Shorten URL API**: Takes a long URL and generates a shortened version.
2. **Redirect to Original URL API**: Takes a shortened URL and redirects the user to the original URL.

### Project Structure

# url-shortener/ 
├── main.py 
## FastAPI app with all endpoints 
├── models.py 
## Database models for storing URLs 
├── database.py 
## Database connection and setup 
├── requirements.txt 
## Required dependencies 
└── README.md 


### Technologies Used

- **FastAPI**: A modern, fast web framework for building APIs with Python 3.7+.
- **SQLAlchemy**: ORM for managing database connections and querying.
- **postgreSQL**: A lightweight database used for storing URL mappings.
- **Uvicorn**: ASGI server to run the FastAPI application.

---

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### Step 2: Set Up the Environment

```bash
# Create a virtual environment (optional but recommended)
python3 -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
pip install -r requirements.txt
```

## API endpoints

# URL Shortener Project

This URL shortener uses a unique short code for each long URL. When the shortened URL is accessed, the system looks up the original URL from the database and performs a 3xx redirect.

## How It Works:

### Shortening:

1. **Submit Long URL**: When a long URL is submitted, the system generates a unique short code.
2. **Check for Duplicates**: The system ensures that no two long URLs have the same short code by checking the database for duplicates.
3. **Save to Database**: The original URL is saved in the database along with the short code.

### Redirecting:

1. **Access Short URL**: When a short code is accessed, the system looks up the corresponding original URL from the database.
2. **Redirect**: If found, the system sends a 3xx redirect response, instructing the browser to navigate to the original URL.

