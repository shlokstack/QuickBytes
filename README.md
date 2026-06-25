# 🍴 QuickBytes

A modern **Restaurant Ordering System** built using **Python** and **Streamlit**. QuickBytes allows customers to browse a dynamic menu, place food orders, validate their budget, download a bill, and stores orders locally for restaurant management.

---

## 🚀 Features

* 🍕 Dynamic menu loaded from a JSON file
* 👤 Customer information form
* 🥗 Multiple food selection
* 💰 Budget validation before placing an order
* 🧾 Downloadable restaurant bill
* 📂 Order storage using CSV
* 🎈 Interactive and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

* Python
* Streamlit
* JSON
* CSV
* Git & GitHub

---

## 📁 Project Structure

```text
QuickBytes/
│── foodApp.py          # Main Streamlit application
│── menu.json           # Restaurant menu
│── requirements.txt    # Project dependencies
│── README.md           # Documentation
│── .gitignore
└── orders.csv          # Generated locally (ignored by Git)
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/shlokstack/QuickBytes.git
```

### 2. Move into the project directory

```bash
cd QuickBytes
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run foodApp.py
```

---

## 📖 How It Works

1. Enter customer details.
2. Select food items from the menu.
3. Set your maximum budget.
4. The application calculates the total amount.
5. If the total exceeds the budget, a warning is displayed.
6. If the order is valid:

   * Order summary is displayed.
   * Bill can be downloaded.
   * Order is stored locally in CSV format.

---

## 📸 Application Preview

> Add screenshots here after taking them.

```text
assets/
│── home.png
│── order-summary.png
```

Example:

```markdown
![Home Screen](assets/home.png)
```

---

## 🌟 Future Improvements

* 🔐 Admin Login
* 📊 Restaurant Dashboard
* 📈 Sales Analytics
* 💳 Online Payment Integration
* 📱 Responsive UI
* 🗄️ Database Integration (MySQL/PostgreSQL)
* 🤖 AI-powered Food Recommendation
* ☁️ Cloud Deployment

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

## 👨‍💻 Author

**Shlok Shah**

GitHub: https://github.com/shlokstack

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
