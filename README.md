# File-Signature-Analyser
A Python-based cybersecurity tool for validating files using magic numbers

File Signature Analyzer is a lightweight cybersecurity utility that analyzes a file’s magic number (header bytes) and determines:

- Whether the file is valid <br>
- Which known file signatures (from a CSV database) match <br>
- Which all extensions match as prefixes <br>

## This project is useful for:

- Malware analysis<br>
- File integrity verification<br>
- Detecting spoofed or renamed files<br>
- Cybersecurity learning and forensics<br>

## 🔍 How It Works

Every file begins with a specific byte sequence called a magic number.

The Python script:<br>
1. Reads a database of magic numbers from Hex.csv<br>
2. Extracts the file’s actual header bytes<br>
3. Normalizes them for comparison<br>
4. Finds all database entries whose magic number is a prefix of the file header<br>
5. Finds the longest matching magic number<br>
6. Returns all the file descriptions associated with those strongest matches<br>

This ensures highly accurate detection even when multiple formats share similar prefixes.

## 📦 Features

- CSV-driven signature database<br>
- Detects file type based on magic numbers<br>
- Prefix-based matching<br>
- Supports multi-extension formats (ZIP, DOCX, XLSX, PDF, etc.)<br>
- Extracts max-precision match<br>
- Outputs file extensions, descriptions, and more<br>
- Works on any OS (Windows, Linux, macOS)<br>
- No external dependencies<br>


## 🚀 Getting Started
1. Clone the repository <br>
```sh
git clone https://github.com/deepak-kiran/File-Signature-Analyzer.git
```
2. Change directory
```sh
cd File-Signature-Inspector
```
3. Run the script using python
```sh
python analyzer.py
```
## 🤝 Contributing
Pull requests are welcome!
If you want to add more signatures, update Hex.csv in the correct format.

## 📄 License
MIT License — free for personal and commercial use.

🌟 Support the Project
If you find this useful, give the repo a ⭐ on GitHub!
It helps others discover the tool and motivates further development.
