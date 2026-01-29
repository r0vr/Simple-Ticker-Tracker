# Simple Ticker Tracker

## Written by: Owen Pearson

### Project Description

A simple program I made to help me get better at Python,
as well as libraries like pandas. This program uses pandas
as well as yfinance to pull stock prices.

### How To Use

The user inputs a stock ticker and is presented with options
for various sources of data to view, such as income statements,
SEC filings, stock price history, and general company info.
These sources are also (with the exception of info) printed
to either .csv or .json files. These files can be viewed at
a later time inside the program, or via your own software.

---

### Installation

**Prerequisites:**

- Python 3.8 or higher recommended
- [git](https://git-scm.com/) (to clone the repository)
- [pip](https://pip.pypa.io/en/stable/) (for installing Python packages)

**1. 

```bash
git clone https://github.com/r0vr/Simple-Ticker-Tracker.git
cd stt
```

**2.

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

**3. 


```bash
pip install -r requirements.txt
```

**4. 

```bash
python main.py
```

---

## License

This project is licensed under [GPL v3](LICENSE)

**Troubleshooting:**  
If you encounter problems, ensure your Python and pip versions are up to date.  
For more help, open an issue in the [GitHub repository](https://github.com/r0vr/stt/issues).

---

**_Thanks for checking out my first project! Feedback is always welcome._**
