# 🔐 File Integrity Checker

## 📌 Project Description

The File Integrity Checker is a cybersecurity tool designed to monitor and detect unauthorized changes in files. It works by generating and comparing hash values (MD5, SHA1, SHA256) to ensure file integrity. Any modification in a file is immediately detected and logged.

---

## 🎯 Objectives

* Detect file tampering using hashing techniques
* Provide real-time monitoring of files
* Alert users about unauthorized changes
* Maintain logs for security analysis

---

## 🛠️ Technologies Used

* Python
* Hashlib (for hashing algorithms)
* Watchdog (for real-time monitoring)
* Tkinter (for GUI)
* JSON (for storing file hashes)

---

## ⚙️ Features

* 🔍 Real-time file monitoring
* 🔐 Multiple hash algorithms (MD5, SHA1, SHA256)
* 📧 Email alert system
* 📝 Logging system for changes
* 🖥️ User-friendly GUI interface
* 📂 File tracking and verification

---

## 📁 Project Structure

```
File-Integrity-Checker/
│── main.py
│── helper.py
│── database.json
│── logs.txt
│── README.md
```

---

## 🚀 How to Run

1. Install required libraries:

```
pip install watchdog
```

2. Run the program:

```
python main.py
```

---

## 📸 Output

* Displays file status in GUI
* Alerts user when file is modified
* Logs all changes in log file

---

## 🔒 Use Cases

* Detect unauthorized file access
* Monitor sensitive system files
* Ensure data integrity in organizations
* Useful in cybersecurity and forensic analysis

---

## 📊 Future Enhancements

* Cloud backup integration
* Advanced alert systems (SMS/Push notifications)
* AI-based anomaly detection
* Multi-user support

---

## 👨‍💻 Author

**Sankalp Mankar**
Cybersecurity Enthusiast

---

## 📌 Conclusion

This project demonstrates how hashing techniques can be effectively used to detect file changes and ensure data integrity, making it a valuable tool in cybersecurity.
