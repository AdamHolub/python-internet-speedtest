<h1 align="center">⚡ Python Internet Speed Test</h1>

![Python](https://img.shields.io/badge/-Python-3776AB?logo=python\&logoColor=white\&style=for-the-badge)
![Speedtest](https://img.shields.io/badge/-Speedtest-EA4335?style=for-the-badge)
![Console](https://img.shields.io/badge/-Console-222222?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=github\&logoColor=black\&style=for-the-badge)

---

A colorful internet speed test written in Python.

This project measures:

- Download speed
- Upload speed
- Ping
- Closest / best server

It also includes a `.bat` launcher so the program can be started with a single click on Windows.

---

<details>
  <summary>📑 Table of Contents</summary>
  <ol>
    <li><a href="#-features">Features</a></li>
    <li><a href="#-quick-start">Quick Start</a></li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#-project-structure">Project Structure</a></li>
    <li><a href="#-example-output">Example Output</a></li>
    <li><a href="#-how-it-works">How It Works</a></li>
    <li><a href="#-future-improvements">Future Improvements</a></li>
    <li><a href="#-license">License</a></li>
  </ol>
</details>

## 🚀 Features

- Colored console output
- Measures:
  - Download speed
  - Upload speed
  - Ping
  - Closest / best server
- Loading spinner while testing
- `.bat` launcher for one-click startup
- Works with virtual environments (`.venv`)

## ⚡ Quick Start

```bash
git clone https://github.com/your-username/python-internet-speedtest.git
cd python-internet-speedtest
```

Create and activate a virtual environment:

```bash
py -m venv .venv
.venv\Scripts\activate
```

Install required packages:

```bash
py -m pip install -r requirements.txt
```

Run the program:

```bash
python speedtest_console.py
```

Or simply double-click:

```text
speedtest.bat
```

## 🖥 Usage

When started, the program automatically:

1. Finds the nearest server
2. Measures ping
3. Measures download speed
4. Measures upload speed
5. Prints the results in color

Speed colors:

- 🔴 Red = slow
- 🟡 Yellow = average
- 🟢 Green = fast

## 📁 Project Structure

```text
python-internet-speedtest/
│
├── speedtest_console.py      # Main Python program
├── speedtest.bat             # Windows launcher
├── requirements.txt          # Required Python packages
├── README.md
└── LICENSE
 
```

## 📷 Example Output

```text
=== INTERNET SPEED TEST ===

Server: Vodafone (Prague, Czech Republic)
Ping: 12 ms
Download: 183.45 Mbps
Upload: 34.28 Mbps

Completed.
```

## ⚙ How It Works

The program uses:

- `speedtest-cli` to communicate with Speedtest servers
- `colorama` for colored console output
- A separate thread for the loading spinner so the console does not freeze while the test is running

Important parts:

```python
init(autoreset=True)
```

Automatically resets colors after each print.

```bat
cd /d "%~dp0"
```

Changes the current directory to the location of the `.bat` file, so the Python script always starts correctly.

## 🔮 Future Improvements

Possible ideas for future versions:

- Speed graph in terminal
- GUI version with charts
- Multiple server selection

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
