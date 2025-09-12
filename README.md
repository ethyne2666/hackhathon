
# 🛒 Daily Basis – Essential Delivery Web App

Daily Basis is a subscription-based e-commerce web application built with **Django**.  
Unlike regular one-time order apps, our platform allows users to **schedule daily/weekly recurring deliveries** for essentials like milk, bread, eggs, vegetables, etc.  

---

Our aim was to create a real-world solution for daily essential deliveries with features like subscription scheduling, pause/resume orders, and time-slot based delivery.  

---

## 🚀 Features
- User authentication (Signup/Login/Profile Management).  
- Product listings with detailed product pages.  
- Cart & Orders (one-time + subscription-based).  
- Schedule recurring deliveries (daily/weekly).  
- Pause/resume delivery option.  
- Built fully with **Django** (backend + templates).  

---

## 📷 Screenshots

Below are some screenshots of the web application to give an overview of the UI:

### 🛒 Shopping Cart
Shows products added to cart and order summary with checkout option.  
![Cart](images%20for%20readme/cart.jpeg)

### 📦 Items Page
Displays available daily essentials (milk, bread, eggs, vegetables, etc.) for subscription or one-time orders.  
![Items](images%20for%20readme/items.jpeg)

### 💳 Payment Page
Checkout and payment integration for subscriptions or single orders.  
![Payment](images%20for%20readme/payment.jpeg)

### ⏰ Scheduled Orders
Schedule your deliveries daily or weekly at fixed times (morning/evening).  
![Scheduler](images%20for%20readme/scheduleroder.jpeg)

### 🔍 Search Functionality
Search products easily using the built-in search bar.  
![Search](images%20for%20readme/search.jpeg)

---

## 🤝 How to Contribute

We welcome contributions! Follow the steps below to get started:

### 1️⃣ Fork the Repository
Click on the **Fork** button (top-right) to make your own copy of this repo.

### 2️⃣ Clone Your Fork
```bash
git clone https://github.com/<your-username>/dailybasis.git
cd dailybasis

```

### 3️⃣ Setup Virtual Environment
```bash
python -m venv venv
```
Activate it:  
- On Windows:  
  ```bash
  venv\Scripts\activate
  ```
- On Linux/Mac:  
  ```bash
  source venv/bin/activate
  ```

### 4️⃣ Install Dependencies
Check installed packages:
```bash
pip list
```
If any required package is missing, install:
```bash
pip install django pillow
```

### 5️⃣ Run the Development Server
```bash
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your browser to see the website live.

---

## 🌱 Making Changes

1. Create a new branch for your feature/bugfix:  
   ```bash
   git checkout -b feature-name
   ```

2. Make your changes in the code.  

3. Commit and push to your fork:  
   ```bash
   git add .
   git commit -m "Added feature-name"
   git push origin feature-name
   ```

4. Go to the original repo and **create a Pull Request (PR)**.  

We will review your PR and merge it 🚀

---

## 📌 Tech Stack
- **Backend:** Django  
- **Database:** SQLite (with plans to move to cloud-managed DBs)  
- **Frontend:** HTML, CSS, Bootstrap, Django Templates  

---

## 📜 License
This project is open-source. Feel free to use, improve, and share with proper credits.  

---

## 🔗 Links
- Project GitHub Repo: [https://github.com/ethyne2666/hackhathon.git]  
- Hackathon Journey Blog Post: [https://www.linkedin.com/posts/charan-kumar-ab5568311_failed-my-first-hackathon-status-code-2-activity-7366140843952336897-D5gW?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAE9IbikBW96zQqil07xmvUZxaH5MQ-JIVOI]  

---
