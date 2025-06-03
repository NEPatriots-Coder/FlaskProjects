# app.py
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Our Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        
  # CREATE - Add a new book
@app.route('/books', methods=['POST'])
def create_book():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not all(key in data for key in ['title', 'author', 'price']):
            return jsonify({'error': 'Missing required fields'}), 400
        
        new_book = Book(
            title=data['title'],
            author=data['author'],
            price=data['price']
        )
        
        db.session.add(new_book)
        db.session.commit()
        
        return jsonify({
            'message': 'Book created successfully',
            'book': new_book.to_dict()
        }), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
  # READ - Get all books
@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books])

# READ - Get a specific book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = Book.query.get_or_404(id)
    return jsonify(book.to_dict())    
        
# UPDATE - Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    # Check if book exists first
    book = Book.query.get(id)
    if not book:
        return jsonify({'error': f'Book with ID {id} not found'}), 404
    
    try:
        # Force=True will ignore content type header issues
        data = request.get_json(force=True)
        
        if data is None:
            return jsonify({'error': 'Invalid JSON data'}), 400
            
        if 'title' in data:
            book.title = data['title']
        if 'author' in data:
            book.author = data['author']
        if 'price' in data:
            # Ensure price is converted to float
            try:
                book.price = float(data['price'])
            except ValueError:
                return jsonify({'error': 'Price must be a valid number'}), 400
            
        db.session.commit()
        return jsonify({
            'message': 'Book updated successfully',
            'book': book.to_dict()
        })
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400



# DELETE - Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get_or_404(id)
    
    try:
        db.session.delete(book)
        db.session.commit()
        return jsonify({
            'message': 'Book deleted successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Create the database tables
with app.app_context():
    db.create_all()
# base route
@app.route("/")
def hello_world():
    return "<p>Hello, Lamar!</p>"

if __name__ == '__main__':
    app.run(debug=True)