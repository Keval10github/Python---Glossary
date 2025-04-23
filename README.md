
# 📘 Python Glossary

A Flask-based web application that allows users to search data from an Excel file in real time. Features a clean and modern UI with a responsive layout and interactive elements.

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.7 or higher**  
2. **pip** – Python package installer  
3. **Virtualenv** (optional but recommended)

---

## 📁 Folder Structure

```
excel-search-app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (optional if not using inline styles)
├── data/
│   └── glossary.xlsx
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Running the App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/excel-search-app.git
cd excel-search-app
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Excel file

Place your `glossary.xlsx` file inside the `data/` directory.

### 5. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the app.

---

## 🧠 Technologies Used

- **Python (Flask)** – for backend server logic  
- **HTML, CSS, JavaScript** – for frontend UI  
- **Pandas** – for reading and filtering Excel data  
- **Jinja2** – for template rendering in Flask  

---

## ✨ Features

- 🔍 **Responsive search form**
- 📊 **Stylish table with hover effects and animations**
- 🎨 **Modern gradient background** using theme colors:  
  `#CADCFC`, `#8AB6F9`, `#00246B`
- ⏳ **Loading spinner** for search feedback
- 🚫 **"No results found" alert**
- 🧾 **Footer with source code link**
- 📱 **Mobile responsive layout**

---

## 📦 requirements.txt

```
flask
pandas
openpyxl
```

---

## 📝 Example: `app.py`

```python
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_excel('data/glossary.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('search', '')
    if query:
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)].to_dict(orient='records')
    else:
        results = []
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ✅ Future Enhancements

- Pagination for large Excel datasets  
- Option to upload and parse different Excel files  
- Column-specific search functionality  

---

## 📎 Credits

**Design & Code by**: [YourName](
# 📘 Python Glossary Excel Search Web App

A Flask-based web application that allows users to search data from an Excel file in real time. Features a clean and modern UI with a responsive layout and interactive elements.

---

## 🔧 Prerequisites

Before you begin, ensure you have the following installed:

1. **Python 3.7 or higher**  
2. **pip** – Python package installer  
3. **Virtualenv** (optional but recommended)

---

## 📁 Folder Structure

```
excel-search-app/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── style.css (optional if not using inline styles)
├── data/
│   └── glossary.xlsx
├── requirements.txt
└── README.md
```

---

## 🚀 Installation & Running the App

### 1. Clone the repository

```bash
git clone https://github.com/your-username/excel-search-app.git
cd excel-search-app
```

### 2. (Optional) Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Excel file

Place your `glossary.xlsx` file inside the `data/` directory.

### 5. Run the app

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser to use the app.

---

## 🧠 Technologies Used

- **Python (Flask)** – for backend server logic  
- **HTML, CSS, JavaScript** – for frontend UI  
- **Pandas** – for reading and filtering Excel data  
- **Jinja2** – for template rendering in Flask  

---

## ✨ Features

- 🔍 **Responsive search form**
- 📊 **Stylish table with hover effects and animations**
- 🎨 **Modern gradient background** using theme colors:  
  `#CADCFC`, `#8AB6F9`, `#00246B`
- ⏳ **Loading spinner** for search feedback
- 🚫 **"No results found" alert**
- 🧾 **Footer with source code link**
- 📱 **Mobile responsive layout**

---

## 📦 requirements.txt

```
flask
pandas
openpyxl
```

---

## 📝 Example: `app.py`

```python
from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)
df = pd.read_excel('data/glossary.xlsx')

@app.route('/', methods=['GET', 'POST'])
def index():
    query = request.form.get('search', '')
    if query:
        results = df[df.apply(lambda row: row.astype(str).str.contains(query, case=False).any(), axis=1)].to_dict(orient='records')
    else:
        results = []
    return render_template('index.html', query=query, results=results)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ✅ Future Enhancements

- Pagination for large Excel datasets  
- Option to upload and parse different Excel files  
- Column-specific search functionality  

---

## 📎 Credits Team Members

**Design & Code by**: [Keval Ravani](https://github.com/Keval10github)
[Jay Rajodiya](https://github.com/JayRajodiya)
[Angel Jagaria]()
---



