# ============================================
# TASK 1: JSON Parsing - Read students.json
# ============================================

import json

def task1_read_students():
    """Read and print student details from students.json"""
    print("=" * 50)
    print("TASK 1: Reading Students Data")
    print("=" * 50)
    
    try:
        with open('students.json', 'r') as file:
            students = json.load(file)
            
        for student in students:
            print(f"\nStudent ID: {student.get('id')}")
            print(f"Name: {student.get('name')}")
            print(f"Age: {student.get('age')}")
            print(f"Grade: {student.get('grade')}")
            print(f"Major: {student.get('major', 'N/A')}")
            print("-" * 30)
            
    except FileNotFoundError:
        print("Error: students.json file not found!")
        print("Creating sample students.json file...")
        # Create sample file
        sample_students = [
            {"id": 1, "name": "Ali Karimov", "age": 20, "grade": "A", "major": "Computer Science"},
            {"id": 2, "name": "Madina Tosheva", "age": 19, "grade": "B", "major": "Mathematics"},
            {"id": 3, "name": "Sardor Yusupov", "age": 21, "grade": "A", "major": "Physics"}
        ]
        with open('students.json', 'w') as file:
            json.dump(sample_students, file, indent=4)
        print("Sample file created! Run the function again.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in students.json")


# ============================================
# TASK 2: Weather API - OpenWeatherMap
# ============================================

import requests

def task2_get_weather(city="Tashkent", api_key="YOUR_API_KEY_HERE"):
    """Fetch and display weather data for a city"""
    print("\n" + "=" * 50)
    print("TASK 2: Weather Information")
    print("=" * 50)
    
    # Note: You need to sign up at openweathermap.org to get a free API key
    # Replace YOUR_API_KEY_HERE with your actual API key
    
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # For Celsius
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for bad status codes
        
        data = response.json()
        
        print(f"\nWeather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Feels Like: {data['main']['feels_like']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Pressure: {data['main']['pressure']} hPa")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        print("\nNote: You need to:")
        print("1. Sign up at https://openweathermap.org/api")
        print("2. Get your free API key")
        print("3. Replace 'YOUR_API_KEY_HERE' with your actual API key")
    except KeyError:
        print("Error: Unexpected response format from API")


# ============================================
# TASK 3: JSON Modification - Books Manager
# ============================================

def load_books():
    """Load books from JSON file"""
    try:
        with open('books.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error reading books.json. Creating new file.")
        return []

def save_books(books):
    """Save books to JSON file"""
    with open('books.json', 'w') as file:
        json.dump(books, file, indent=4)

def add_book(books):
    """Add a new book"""
    print("\n--- Add New Book ---")
    book_id = len(books) + 1 if books else 1
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    genre = input("Enter genre: ")
    
    new_book = {
        "id": book_id,
        "title": title,
        "author": author,
        "year": year,
        "genre": genre
    }
    
    books.append(new_book)
    save_books(books)
    print(f"✓ Book '{title}' added successfully!")

def update_book(books):
    """Update existing book information"""
    print("\n--- Update Book ---")
    display_books(books)
    
    try:
        book_id = int(input("\nEnter book ID to update: "))
        book = next((b for b in books if b['id'] == book_id), None)
        
        if book:
            print(f"\nUpdating: {book['title']}")
            print("(Press Enter to keep current value)")
            
            title = input(f"Title [{book['title']}]: ") or book['title']
            author = input(f"Author [{book['author']}]: ") or book['author']
            year = input(f"Year [{book['year']}]: ") or book['year']
            genre = input(f"Genre [{book['genre']}]: ") or book['genre']
            
            book.update({
                "title": title,
                "author": author,
                "year": year,
                "genre": genre
            })
            
            save_books(books)
            print("✓ Book updated successfully!")
        else:
            print("Book not found!")
    except ValueError:
        print("Invalid input!")

def delete_book(books):
    """Delete a book"""
    print("\n--- Delete Book ---")
    display_books(books)
    
    try:
        book_id = int(input("\nEnter book ID to delete: "))
        book = next((b for b in books if b['id'] == book_id), None)
        
        if book:
            confirm = input(f"Delete '{book['title']}'? (yes/no): ")
            if confirm.lower() == 'yes':
                books.remove(book)
                save_books(books)
                print("✓ Book deleted successfully!")
            else:
                print("Deletion cancelled.")
        else:
            print("Book not found!")
    except ValueError:
        print("Invalid input!")

def display_books(books):
    """Display all books"""
    if not books:
        print("\nNo books in library.")
        return
    
    print("\n--- Library Books ---")
    for book in books:
        print(f"ID: {book['id']} | {book['title']} by {book['author']} ({book['year']}) - {book['genre']}")

def task3_book_manager():
    """Main book management system"""
    print("\n" + "=" * 50)
    print("TASK 3: Book Management System")
    print("=" * 50)
    
    books = load_books()
    
    while True:
        print("\n--- Menu ---")
        print("1. View all books")
        print("2. Add new book")
        print("3. Update book")
        print("4. Delete book")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            display_books(books)
        elif choice == '2':
            add_book(books)
            books = load_books()  # Reload to get updated list
        elif choice == '3':
            update_book(books)
            books = load_books()
        elif choice == '4':
            delete_book(books)
            books = load_books()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# ============================================
# TASK 4: Movie Recommendation System
# ============================================

import random

def task4_movie_recommender(api_key="YOUR_OMDB_API_KEY"):
    """Movie recommendation system using OMDb API"""
    print("\n" + "=" * 50)
    print("TASK 4: Movie Recommendation System")
    print("=" * 50)
    
    # Note: Get free API key from http://www.omdbapi.com/apikey.aspx
    
    genres = {
        '1': 'action',
        '2': 'comedy',
        '3': 'drama',
        '4': 'horror',
        '5': 'sci-fi',
        '6': 'thriller',
        '7': 'romance'
    }
    
    print("\nAvailable Genres:")
    for key, genre in genres.items():
        print(f"{key}. {genre.title()}")
    
    choice = input("\nSelect a genre (1-7): ")
    
    if choice not in genres:
        print("Invalid choice!")
        return
    
    selected_genre = genres[choice]
    
    # Sample popular movies by genre (you can expand this list)
    movie_keywords = {
        'action': ['batman', 'matrix', 'avengers', 'gladiator', 'inception'],
        'comedy': ['hangover', 'superbad', 'airplane', 'bridesmaids', 'dumb'],
        'drama': ['shawshank', 'godfather', 'forrest', 'green mile', 'beautiful mind'],
        'horror': ['exorcist', 'shining', 'conjuring', 'quiet place', 'hereditary'],
        'sci-fi': ['interstellar', 'star wars', 'blade runner', 'arrival', 'ex machina'],
        'thriller': ['silence lambs', 'seven', 'gone girl', 'zodiac', 'prisoners'],
        'romance': ['titanic', 'notebook', 'eternal sunshine', 'before sunrise', 'love actually']
    }
    
    keyword = random.choice(movie_keywords[selected_genre])
    
    try:
        url = f"http://www.omdbapi.com/?apikey={api_key}&s={keyword}&type=movie"
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get('Response') == 'True' and data.get('Search'):
            movie = random.choice(data['Search'])
            
            # Get detailed info
            detail_url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie['imdbID']}&plot=full"
            detail_response = requests.get(detail_url)
            detail_data = detail_response.json()
            
            print(f"\n🎬 Recommended Movie: {detail_data.get('Title')}")
            print(f"Year: {detail_data.get('Year')}")
            print(f"Genre: {detail_data.get('Genre')}")
            print(f"Director: {detail_data.get('Director')}")
            print(f"Actors: {detail_data.get('Actors')}")
            print(f"IMDb Rating: {detail_data.get('imdbRating')}/10")
            print(f"\nPlot: {detail_data.get('Plot')}")
        else:
            print("No movies found for this genre.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movie data: {e}")
        print("\nNote: You need to:")
        print("1. Get a free API key from http://www.omdbapi.com/apikey.aspx")
        print("2. Replace 'YOUR_OMDB_API_KEY' with your actual API key")


# ============================================
# MAIN PROGRAM
# ============================================

def main():
    """Run all tasks"""
    print("\n" + "=" * 50)
    print("HOMEWORK SOLUTIONS")
    print("=" * 50)
    
    while True:
        print("\n--- Select a Task ---")
        print("1. Task 1: Read Students JSON")
        print("2. Task 2: Weather API (Tashkent)")
        print("3. Task 3: Book Management System")
        print("4. Task 4: Movie Recommendation")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            task1_read_students()
        elif choice == '2':
            # Replace with your actual API key
            task2_get_weather("Tashkent", "YOUR_API_KEY_HERE")
        elif choice == '3':
            task3_book_manager()
        elif choice == '4':
            # Replace with your actual API key
            task4_movie_recommender("YOUR_OMDB_API_KEY")
        elif choice == '5':
            print("\nThank you! Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
