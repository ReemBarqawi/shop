<div align="center">
  <img src="docs/cozycart_logo2.png" alt="CozyCart Logo" width="130" width="150" style="border-radius: 50%; background: none; display: block; margin: auto;"/>

  # 🛍️ **CozyCart**
  ### *A Mini E-Commerce System Built with Django*
  **Author:** Reem Barqawi  
  **Framework:** Django (Python) • **Database:** PostgreSQL  
</div>

---

## 📖 Overview

CozyCart is a lightweight e-commerce application built with Django as my capstone project for the General Assembly Bridging Program. 
It’s designed to provide a simple yet elegant shopping experience:

- 🧑‍💼 **Admins** can manage products and categories (CRUD operations).  
- 🛍️ **Customers** can browse and view products add products to cart .  

The project demonstrates my understanding of:  
✅ Django Models, Views, and Templates (MVT)  
✅ Authentication & Authorization  
✅ PostgreSQL integration  
✅ Responsive front-end with CSS  
✅ Git workflow and version control  

---

## 💡 Background

I created this project to strengthen my backend development skills and understand how **real-world web apps** manage data, users, and authentication.  
**CozyCart** represents a key step in my journey toward becoming a professional **full-stack developer**.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | Django 5.x |
| **Database** | PostgreSQL |
| **Environment Management** | python-dotenv |
| **Frontend** | HTML, CSS |
| **Version Control** | Git & GitHub |

---

## ✨ Features

✅ Django project structure set up  
✅ PostgreSQL database connected  
✅ Secure `.env` configuration  
✅ User authentication (Sign Up, Login, Logout)  
✅ Admin/Customer role separation  
✅ CRUD functionality for products and categories  
✅ Responsive front-end layout  

---

## 🚀 Future Improvements

- 💳 Payment integration (Stripe)    
- 🎨 Improve UI using Tailwind CSS or Bootstrap  
- 📊 Add admin analytics dashboard  

---

## 🧱 Entity-Relationship Diagram (ERD)

![ERD Diagram](docs/erd.png)

---


## 🪄 Getting Started

### 1️⃣ Clone the repository  
```bash
git clone https://git.generalassemb.ly/reembarqawi/shop
cd mini_shop_project
```

2️⃣ Create a virtual environment

```bash
python -m venv venv
Mac/Linux:  source name-of-venv/bin/activate
Windows:  source name-of-venv/scripts/activate
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

4️⃣ Configure environment variables

Create a .env file in the root directory:

```bash
SECRET_KEY=django-insecure-CHANGE_THIS_SECRET_KEY
DEBUG=True
DATABASE_URL=postgres://postgres:reem1234@localhost:5432/shop_db
```

5️⃣ Run migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

6️⃣ Open in browser
👉 http://127.0.0.1:8000

---

🌟 Lessons Learned

This project helped me:

Set up and structure a Django project from scratch

Work with PostgreSQL databases

Implement authentication & user roles

Build clean and maintainable HTML templates

---


👩🏻‍💻 Author

Reem Barqawi
📊 Aspiring Data Analyst & Web Developer
[🔗 LinkedIn](https://www.linkedin.com/in/reem-barqawi200)

---
<div align="center"> <sub>✨ Built with passion & curiosity — CozyCart © 2025 ✨</sub> </div> ```
