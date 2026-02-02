# RSS Feed Reader (CLI)

A beginner-friendly **RSS Feed Reader built in Python** that fetches news from an RSS feed and lets the user read articles **interactively, one by one**, directly in the terminal.

Unlike a simple dump of headlines, this tool behaves more like a reader: it shows one news item at a time and asks the user whether they want to continue reading.

---

## 📌 What this project does

* Fetches an RSS feed using a feed URL
* Parses the feed using a standard RSS parser
* Displays:

  * Feed title
  * Article title
  * Summary
  * Link
  * Published date
* Shows **one news item at a time**
* Asks the user whether they want to continue reading
* Stops cleanly when the user chooses to exit

This is a **command-line (CLI) application**, designed to be simple, readable, and interactive.

---

## 🧠 How it works (high-level)

1. The program fetches and parses the RSS feed using `feedparser`
2. All feed entries are stored in a list
3. The reader displays one entry at a time
4. After each entry, the user decides whether to continue
5. The program exits gracefully when the user says no

This approach avoids overwhelming the user with too much information at once.

---

## 🛠️ Tech Stack

* **Python 3.14**
* **feedparser** — a Python library for parsing RSS and Atom feeds
* **Git & GitHub** for version control

The focus is on fundamentals, not frameworks.

---

## 📂 Project Structure

```
rss-feed-reader/
│
├── main.py        # Main application logic
├── .gitignore     # Git ignored files
├── README.md      # Project documentation
└── venv/          # Virtual environment (not tracked)
```

---

## 🚀 How to Run This Project (Step by Step)

### 1️⃣ Clone the repository

```
git clone https://github.com/Riyansh-H1/rss-feed-reader.git
cd rss-feed-reader
```

---

### 2️⃣ Create and activate a virtual environment

Create the virtual environment:

```
python -m venv venv
```

Activate it (Windows PowerShell):

```
venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

### 3️⃣ Install dependencies

```
pip install feedparser
```

---

### 4️⃣ Run the program

```
python main.py
```

The program currently uses the BBC News RSS feed by default.

You can change the feed URL inside `main.py`:

```python
url = "https://feeds.bbci.co.uk/news/rss.xml"
```

---

## 🧩 Example Interaction

```
--------------------------------------------------
Feed Title: BBC News
--------------------------------------------------

News 1:

Title: Example headline
Summary: Example summary text...
Link: https://www.bbc.com/...
Published on: Tue, 30 Jan 2026

--------------------------------------------------
Do you want to read more news? (y/n): y
```

---

## 🧪 Error Handling

* If the RSS feed contains no entries, the program informs the user
* Missing fields such as summary or link are handled safely
* The program exits cleanly when the user chooses to stop

---

## 📘 What I Learned From This Project

* How RSS feeds work and how they differ from web scraping
* How to use third-party libraries effectively in Python
* Writing interactive CLI programs
* Handling user input and program flow
* Structuring Python code using functions
* Managing a project with Git and GitHub
* Using virtual environments for dependency isolation

---

## 🔮 Possible Improvements

* Allow users to input any RSS feed URL at runtime
* Add validation for invalid URLs
* Limit the maximum number of articles
* Convert the CLI reader into a Flask-based web application
* Improve formatting and readability

---

## 👤 Author

**Riyansh Hariramani**
GitHub: [https://github.com/Riyansh-H1](https://github.com/Riyansh-H1)

---

This project is intentionally simple and interactive, focusing on strong Python fundamentals and clean program flow rather than complexity.
