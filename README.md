# 📚 **Book Catalog API**

A simple **Book Catalog RESTful API** built with **FastAPI**, **SQLAlchemy**, and **Pydantic** to demonstrate CRUD operations, validation, async endpoints, and testing proficiency.

---

## ✅ **Features**

* 📖 **CRUD operations** for managing books
* ⚡ **Async endpoint** for listing books
* 🛡️ **Pydantic validation** for data integrity
* 💾 **SQLite database** with SQLAlchemy ORM
* 🧪 **Unit and integration tests** with pytest
* 📄 **Auto-generated OpenAPI documentation**

---

## 🗂️ **Project Structure**

```
book-catalog-api/
├── app/
│   ├── main.py          # FastAPI app and endpoints
│   ├── models.py        # SQLAlchemy Book model
│   ├── schemas.py       # Pydantic schemas with validation
│   ├── crud.py          # CRUD operations
│   └── database.py      # DB setup
├── tests/
│   ├── test_main.py     # Integration tests
│   └── test_crud.py     # Unit tests
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

---

## 🚀 **Setup Instructions**

### **1. Clone the repository**

```bash
git clone https://github.com/aqeeladil/book-catalog-api.git
cd book-catalog-api
```

### **2. Create virtual environment**

```bash
python -m venv venv
```

Activate:

* **Windows:** `venv\Scripts\activate`
* **macOS/Linux:** `source venv/bin/activate`

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

### **4. Run the application**

```bash
uvicorn app.main:app --reload
```

### **5. Access API Docs**

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 **Running Tests**

Run all unit and integration tests with:

```bash
python -m pytest
```

This will execute tests under the `tests/` folder, covering:

* **Unit tests:** CRUD business logic (`test_crud.py`)
* **Integration tests:** API endpoints (`test_main.py`)

---

## 🧪 **Testing Strategy**

This project uses **pytest** with a clear and structured testing strategy:

* **Unit tests** (`tests/test_crud.py`):

  * Directly test CRUD functions with a test database (uses a temporary SQLite file (tempfile.NamedTemporaryFile) to ensure proper cleanup across all operating systems).
  * Ensure business logic works independently from routes.

* **Integration tests** (`tests/test_main.py`):

  * Use FastAPI’s TestClient to send requests to endpoints.
  * Validate end-to-end flow: create → read → update → delete.

* **Fixtures** are used to:

  * Avoid code duplication (DRY compliance).
  * Set up fresh data per test for isolation and reliability.

* **Test database**:

  * SQLite used for simplicity.
  * Cleaned up after test module execution.

---

## 🔧 **Endpoints Summary**

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| GET    | /books/     | List all books (async)  |
| GET    | /books/{id} | Retrieve a single book  |
| POST   | /books/     | Create a new book       |
| PUT    | /books/{id} | Update an existing book |
| DELETE | /books/{id} | Delete a book           |

---

