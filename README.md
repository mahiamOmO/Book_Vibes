# 📚 Book Vibes

**Book Vibes** is a Django-based web application designed to provide users with a seamless online bookstore experience. Users can browse a curated collection of books, add them to their cart, and place orders with ease. The platform aims to enhance the reading journey by offering an intuitive and user-friendly interface.

---

## 🧑‍🏫 Faculty & Course Information

- **Faculty:** Tahmid Taki Rahman  
- **Course:** CSE 322 – Software Engineering

---

## 🚀 Features

- **User Authentication:** Secure registration and login functionalities.
- **Book Catalog:** Browse books by categories and genres.
- **Search Functionality:** Efficient search to find books quickly.
- **Shopping Cart:** Add or remove books from the cart.
- **Order Management:** Place orders and view order history.
- **E-book Access:** Download available e-books directly.

---

## 🖼️ Screenshot

## 📸 Screenshots

### 🏠 Home Page
![Home Page](screenshort/home page.png)

### 🔐 Login Page
![Login Page](screenshort/log in page.png)

### 📝 Add New Book Option
![Add New Book Option](screenshort/add new book option.png)

### ⚙️ Admin Site Access
![Admin Site Access](screenshort/admin site access.png)

### 📖 Book Details Page
![Book Details Page](screenshort/book details page.png)

### 📚 Book Page
![Book Page](screenshort/book page.png)

### 📘 Admin Chapter Read
![By Admin Chapter Read](screenshort/by admin chapter read.png)

### ➕ Chapter Add
![Chapter Add](screenshort/chapter add.png)

### 📘 Chapter E-Book
![Chapter E-Book](screenshort/chapter ebook.png)

### 🆕 Create Account
![Create Account](screenshort/create acc.png)

### ❌ Delete Book Option
![Delete Book Option](screenshort/delete book option.png)

### 📥 E-book Add New Book
![E-book Add New Book](screenshort/ebook add new book.png)

### 🏠 E-book Homepage
![E-book Homepage](screenshort/ebook homepage.png)

### 📝 Edit Book Info
![Edit Book Info](screenshort/edit book info.png)

### 📤 Update E-book
![Update E-book](screenshort/update ebook.png)

---

---

## 🛠️ Technologies Used

- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite
- **Others:** Bootstrap for responsive design

---

## 📂 Project Structure

```
Book_Vibes/
├── bookstore/       # Core application
├── cart/            # Shopping cart functionalities
├── ebook/           # E-book management
├── files/           # Static and media files
├── order/           # Order processing
├── search/          # Search functionalities
├── store/           # Storefront views
├── templates/       # HTML templates
├── static/          # Static files (CSS, JS, Images)
├── screenshots/     # Screenshots used in README
├── db.sqlite3       # SQLite database
├── manage.py        # Django management script
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
```

---

## 🖥️ Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/mahiamOmO/Book_Vibes.git
   cd Book_Vibes
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

6. **Access the Application:**

   Open your browser and navigate to `http://localhost:8000/`

   
## 🧪 Testing

To run tests, use:

```bash
python manage.py test

---

## ✅ Usage

- **Register/Login:** Create an account or log in to access features.
- **Browse Books:** Explore the collection and view book details.
- **Add to Cart:** Select books and add them to your shopping cart.
- **Place Orders:** Proceed to checkout and confirm your orders.
- **Download E-books:** Access and download available e-books.

---

## 📧 Contact

For any queries or feedback, please reach out to:

- **Email:** [your-email@example.com]
- **GitHub:** [@mahiamOmO](https://github.com/mahiamOmO)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
