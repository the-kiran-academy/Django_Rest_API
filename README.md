# Django REST API Project Setup

## 📌 **Prerequisites**
- Python installed (`>= 3.x`)
- pip installed

---

## ⚙️ Setup Instructions

### 1. Extract the Project
- Extract the ZIP file into a folder.

---

### 2. Install Python and pip
- Verify Python installation by running:
```bash
python --version

---

- If pip is not installed, install it by running
```bash
python -m ensurepip --default-pip

### 3. Create a Virtual Environment
- Open a terminal or command prompt in the extracted project folder.
```bash
python -m venv venv

- Activate the virtual environment:
```bash
.\venv\Scripts\activate

### 4. Install Required Packages
- Install all dependencies using the requirements.txt file:
```bash
pip install -r requirements.txt

### 5. Apply Migrations
- Create and apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate

### 6. Run the Django Server
- Start the server:
```bash
python manage.py runserver



### Note: Change mysql password in settings.py (as per your DB)

