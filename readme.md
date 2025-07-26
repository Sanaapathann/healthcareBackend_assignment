# Healthcare Management System 🏥

A simple Django + DRF-based backend for managing Patients, Doctors, and User Authentication.

---

## ✅ How to Run / Setup the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Sanaapathann/healthcareBackend_assignment.git
cd healthcare_application
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # For Windows
# OR
source venv/bin/activate  # For macOS/Linux
```

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables

Create a `.env` file in the root with:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
```

> ⚠️ If you're using SQLite (default), you can skip the POSTGRES settings.

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create a Superuser (for admin access)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit: /admin/

---

## 🔄 API Testing with Postman

* Import the Postman collection file:
  **`healthcareapp.postman_collection.json`**
* It contains 15+ requests:

  * Register/Login user
  * Add / View / Update / Delete Patients
  * Add / View / Update / Delete Doctors
  * Map Patients to Doctors

---

## ✅ How This Project Was Made

### 🛠️ Tech Stack

* **Backend:** Django 4+, Django REST Framework
* **Database:** SQLite (or PostgreSQL if preferred)
* **Testing:** Postman
* **Admin Panel:** Django Admin
* **Environment:** `.env` with secrets and config

---

###  💻  Key Features Implemented

1. **User Authentication (JWT-based)**

   * `POST /api/auth/register/`
   * `POST /api/auth/login/`

2. **Patient Management**

   * `POST /api/patients/`
   * `GET /api/patients/`
   * `GET /api/patients/<id>/`
   * `PUT /api/patients/<id>/`
   * `DELETE /api/patients/<id>/`

3. **Doctor Management**

   * `POST /api/doctors/`
   * `GET /api/doctors/`
   * `GET /api/doctors/<id>/`
   * `PUT /api/doctors/<id>/`
   * `DELETE /api/doctors/<id>/`

4. **Patient–Doctor Mapping**

   * You can assign multiple doctors to a patient and fetch the related data.

---

### 🧱 User Types

* **Normal users:** Can register and manage their own patients/doctors.
* **Admin (staff/superuser):** Can access everything via `/admin/`.

---

### 🧪 Testing

* 15+ API endpoints tested using Postman (collection included).
* Data can also be added via Django Admin for easy testing and relationships.

---
