# 🚀 Interactive Dashboard Platform

A full-stack, real-time dashboard platform that allows users to create, customize, and persist dynamic data visualizations.

Built with a modern tech stack including React, FastAPI, PostgreSQL, and WebSockets, this project simulates a production-grade analytics dashboard used in real-world SaaS applications.

---

## ✨ Features

* 🔐 **User Authentication (JWT)**

  * Secure login and registration system
  * Token-based session handling

* 📊 **Real-Time Data Streaming**

  * Live updates via WebSockets
  * Simulated streaming analytics data

* 🧩 **Drag-and-Drop Dashboard**

  * Fully customizable widget layout
  * Built with responsive grid system

* 💾 **Persistent User Layouts**

  * Saved to PostgreSQL database
  * User-specific dashboards

* 🎨 **Modern UI/UX**

  * Glassmorphism design
  * Responsive layout with sidebar navigation

---

## 🧱 Tech Stack

### Frontend

* React
* Chart.js
* react-grid-layout

### Backend

* FastAPI
* WebSockets
* SQLAlchemy ORM

### Database

* PostgreSQL

### Authentication

* JWT (python-jose)
* Password hashing (bcrypt)

### Deployment

* Vercel (Frontend)
* Render (Backend & Database)

---

## 🖥️ Architecture

Frontend (React)
⬇️
FastAPI Backend (API + WebSockets)
⬇️
PostgreSQL Database

---

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MuneebAhmed2000/interactive-dashboard-platform.git
cd interactive-dashboard-platform
```

---

### 2. Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
```

#### Create PostgreSQL Database

```sql
CREATE DATABASE dashboard_db;
```

#### Update database connection

In `app/database.py`:

```python
DATABASE_URL = "postgresql://username:password@localhost:5432/dashboard_db"
```

#### Run backend

```bash
python -m uvicorn app.main:app --reload
```

---

### 3. Frontend Setup

```bash
cd frontend
npm install
npm start
```

---

## 🔐 Authentication Flow

1. User registers or logs in
2. Backend returns JWT token
3. Token is stored in localStorage
4. Token is attached to API requests
5. Backend identifies user and loads their dashboard

---

## 📡 Real-Time Data

* WebSocket endpoint: `/ws`
* Sends simulated analytics data every few seconds
* Updates charts dynamically on the frontend

---

## 📊 Future Improvements

* Multiple dashboards per user
* Role-based access control
* Data export (CSV / PDF)
* Advanced analytics widgets (heatmaps, pie charts)
* Full production deployment with CI/CD

---

## 💼 Resume Description

**Interactive Dashboard Platform**

* Built a full-stack real-time analytics dashboard using React, FastAPI, and PostgreSQL
* Implemented JWT-based authentication and user-specific persistent layouts
* Designed a drag-and-drop UI with live data updates using WebSockets
* Deployed scalable frontend and backend services using Vercel and Render

---

## 📸 Screenshots

![Login](screenshots/login.png)

![Dashboard](screenshots/dashboard.png)

---

## 🧠 What I Learned

* Full-stack application architecture
* Real-time data handling with WebSockets
* Authentication and security best practices
* Database design with SQLAlchemy and PostgreSQL
* Deployment and cloud infrastructure

---

## 👤 Author

**Muneeb Ahmed**

LinkedIn: https://www.linkedin.com/in/muneebahmed18/ 

MS Data Science Student

---

## 📄 License

This project is for educational and portfolio purposes.
