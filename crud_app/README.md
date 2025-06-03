# Flask Book API

A RESTful API for managing a book collection using Flask and PostgreSQL.

## Setup Instructions

### Database Setup
Run a PostgreSQL instance using Docker:
```bash
docker run --name flask_postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -p 5432:5432 -d postgres
```

### Application Setup
1. Install dependencies:
```bash
pip install flask flask-sqlalchemy psycopg2-binary
```

2. Run the application:
```bash
python app.py
```

The server will start at http://127.0.0.1:5000

## API Endpoints

### Books Resource

#### GET /books
Returns a list of all books.

#### GET /books/{id}
Returns details of a specific book.

#### POST /books
Creates a new book.

Request body:
```json
{
  "title": "Book Title",
  "author": "Author Name",
  "price": 19.99
}
```

#### PUT /books/{id}
Updates an existing book.

Request body (all fields optional):
```json
{
  "title": "Updated Title",
  "author": "Updated Author",
  "price": 14.99
}
```

#### DELETE /books/{id}
Deletes a book.

## Example Usage

### Create a book
```bash
curl -X POST http://127.0.0.1:5000/books \
-H "Content-Type: application/json" \
-d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 9.99}'
```

### Get all books
```bash
curl -X GET http://127.0.0.1:5000/books
```

### Update a book's price
```bash
curl -X PUT http://127.0.0.1:5000/books/1 \
-H "Content-Type: application/json" \
-d '{"price": 14.99}'
```

### Delete a book
```bash
curl -X DELETE http://127.0.0.1:5000/books/1
```

## Project Structure

- `app.py`: Main application file containing the Flask app, database models, and API routes
- `.gitignore`: Git configuration to exclude unnecessary files
- `README.md`: Project documentation

## Technologies Used

- Flask: Web framework
- SQLAlchemy: ORM for database operations
- PostgreSQL: Database
- Docker: Container for PostgreSQL