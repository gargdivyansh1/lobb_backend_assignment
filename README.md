# URL Shortener with Redirection API

This project is a simple URL shortener service built with FastAPI. It allows users to shorten long URLs and provides a way to redirect them back to their original URLs using the shortened link.

## Project Overview

The project consists of two main APIs:

1. **Shorten URL API**: Takes a long URL and generates a shortened version.
2. **Redirect to Original URL API**: Takes a shortened URL and redirects the user to the original URL.

### Project Structure

url-shortener/
    ├── main.py 
    ├── models.py  
    ├── database.py 
    ├── requirements.txt 
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

## Database

The application uses SQLite to store the mappings between the short codes and original URLs. The URL model has the following fields:

- **original_url**: The original long URL
- **short_url**: The generated shortened URL code

# Testing

To test the application:

1. Run the server as described above.

2. Use a tool like Postman or curl to test the POST and GET requests.

3. Example test with curl:
    * Shorten a URL:  

```bash  
curl -X 'POST' 'http://localhost:8000/shorten' \
  -H 'Content-Type: application/json' \
  -d '{"long_url": "https://www.example.com"}'
```
* Redirect using shortened URL:  

```bash
curl -L 'http://localhost:8000/abc123'
```


This URL shortener uses a unique short code for each long URL. When the shortened URL is accessed, the system looks up the original URL from the database and performs a 3xx redirect.

## How It Works:

### Shortening:

1. **Submit Long URL**: When a long URL is submitted, the system generates a unique short code.
2. **Check for Duplicates**: The system ensures that no two long URLs have the same short code by checking the database for duplicates.
3. **Save to Database**: The original URL is saved in the database along with the short code.

### Redirecting:

1. **Access Short URL**: When a short code is accessed, the system looks up the corresponding original URL from the database.
2. **Redirect**: If found, the system sends a 3xx redirect response, instructing the browser to navigate to the original URL.

