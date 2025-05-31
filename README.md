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

## 📸 Screenshots

> ⚠️ Make sure your image files are placed in a folder named `screenshots/` in your project root, and filenames use underscores or hyphens (no spaces).

### 🏠 Home Page  
![Home Page](./screenshot/home_page.png)

### 🔐 Login Page  
![Login Page](screenshots/login_page.png)

### 📝 Add New Book Option  
![Add New Book Option](screenshots/add_new_book_option.png)

### ⚙️ Admin Site Access  
![Admin Site Access](screenshots/admin_site_access.png)

### 📖 Book Details Page  
![Book Details Page](screenshots/book_details_page.png)

### 📚 Book Page  
![Book Page](screenshots/book_page.png)

### 📘 Admin Chapter Read  
![By Admin Chapter Read](screenshots/by_admin_chapter_read.png)

### ➕ Chapter Add  
![Chapter Add](screenshots/chapter_add.png)

### 📘 Chapter E-Book  
![Chapter E-Book](screenshots/chapter_ebook.png)

### 🆕 Create Account  
![Create Account](screenshots/create_account.png)

### ❌ Delete Book Option  
![Delete Book Option](screenshots/delete_book_option.png)

### 📥 E-book Add New Book  
![E-book Add New Book](screenshots/ebook_add_new_book.png)

### 🏠 E-book Homepage  
![E-book Homepage](screenshots/ebook_homepage.png)

### 📝 Edit Book Info  
![Edit Book Info](screenshots/edit_book_info.png)

### 📤 Update E-book  
![Update E-book](screenshots/update_ebook.png)

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

---

## 🧪 Testing

To run tests, use:

```bash
python manage.py test
```

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
- **LinkedIn:** [mahiamomo](https://www.linkedin.com/in/mahiamomo12/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
