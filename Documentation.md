# SQLGenie

## 1. Solution Description

**SQLGenie** is an API-based solution that simplifies database querying for users unfamiliar with SQL. It leverages OpenAI's GPT-4 model to translate natural language questions into SQL queries. Users provide a query in plain text, and the application returns an SQL query that can be executed on a database. This solution aims to reduce the complexity of interacting with databases by abstracting away SQL syntax, allowing even non-technical users to generate valid SQL queries.

### Purpose
This application bridges the gap between natural language and structured query language, enhancing productivity and reducing the learning curve for database management.

### Functionalities
- **Natural Language Processing (NLP)**: Converts natural language input into SQL queries.
- **GPT-4 Integration**: Uses OpenAI's GPT-4 model (`gpt-4o-mini`) for query generation.
- **RESTful API**: Provides an API interface for external systems to interact with SQLGenie.

## 2. API User Guide

### Base URL
```
http://127.0.0.1:5000
```

### Endpoints

#### **POST /ask**

**Description:** 
This endpoint accepts a natural language query and returns an SQL query. 
`query`: The natural language text that describes the SQL query the user wants to generate.

**Request Format:**

**Endpoint**: `/ask`  
**Method**: `POST`  
**Content-Type**: `application/json`

**Request Body:**
```json
{
    "query": "<natural-language-query>"
}
```

**Response Example:**
- Status: 200 OK
- Content-Type: application/json

**Response Body:**
```json
{
  "data": "<sql-query>",
}
```

**Error Response:**
- **400 Bad Request** Returned when the input is not valid JSON or if an exception occurs during query processing.
  ```json
  {
    "error": "Invalid input, expected JSON"
  }
  ```
- **404 Not Found** Returned when the requested resource is not found.
  ```json
  {
    "error": "Resource Not Found"
  }
  ```
- **405 Method Not Allowed** Returned when a method other than POST is used.
  ```json
  {
    "error": "Method Not Allowed"
  }
  ```

## 3. Input/Output Details

### Example Success Request
```bash
curl -X POST http://127.0.0.1:5000/ask \
-H "Content-Type: application/json" \
-d '{"query": "Get all users who signed up in the last 30 days"}'
```

### Example Success Output
```json
{
  "data": "SELECT * FROM users WHERE signup_date >= NOW() - INTERVAL 30 DAY;",
}
```

## Example Error Request
```bash
curl -X POST http://127.0.0.1:5000/ask \
-H "Content-Type: application/json" \
-d "invalid text"
```

## Example Error Response
```json
{
  "data": "Invalid input, expected JSON;",
}
```

## 4. Setup Instructions

### Dependencies
- **Python Version:** 3.12
- **Required Python Packages:** Listed in `requirements.txt`

### Steps to Set Up Locally

1. **Install Dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

2. **Set Environment Variable:**
   Ensure the `OPEN_API_KEY` environment variable is set with your OpenAI API key.
   ```sh
   export OPEN_API_KEY='your_open_api_key_here'
   ```

3. **Run Application:**
   ```sh
   gunicorn --workers=2 --bind=127.0.0.1:5000 app:app
   ```

4. **Access Application:**
   Open your browser and navigate to `http://127.0.0.1:5000` to view the application.

### Docker Instructions

1. **Build Docker Image:**
   ```sh
   docker build --platform linux/amd64 -t mathmateai/sql-genie:latest -f Dockerfile .
   ```

2. **Run Docker Container:**
   ```sh
   docker run -e OPEN_API_KEY='your_open_api_key_here' -p 5000:5000 --name sql-genie -d mathmateai/sql-genie
   ```

3. **Docker Compose:**
   ```sh
   docker compose --project-name sql-genie -f docker-compose.yml up --force-recreate --build -d
   ```