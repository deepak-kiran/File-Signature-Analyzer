A Python-based cybersecurity tool for validating files using magic numbers

File Signature Analyzer is a lightweight cybersecurity utility that analyzes a file’s magic number (header bytes) and determines:

✔ Whether the file is valid
✔ Which known file signatures (from a CSV database) match
✔ Which signatures match as prefixes

This project is useful for:

Malware analysis
File integrity verification
Detecting spoofed or renamed files
Cybersecurity learning and forensics

🔍 How It Works

Every file begins with a specific byte sequence called a magic number.

The Python script:
Reads a database of magic numbers from Hex.csv
Extracts the file’s actual header bytes
Normalizes them for comparison
Finds all database entries whose magic number is a prefix of the file header
Finds the longest matching magic number
Returns all the file descriptions associated with those strongest matches

This ensures highly accurate detection even when multiple formats share similar prefixes.

📦 Features

✔ CSV-driven signature database
✔ Detects file type based on magic numbers
✔ Prefix-based matching
✔ Supports multi-extension formats (ZIP, DOCX, XLSX, PDF, etc.)
✔ Extracts max-precision match
✔ Outputs file extensions, descriptions, and more
✔ Works on any OS (Windows, Linux, macOS)
✔ No external dependencies

📂 Project Structure
FileSignatureInspector/
│
├── Hex.csv                 # Magic number database
├── analyzer.py             # Core lookup engine
├── README.md               # Project documentation
└── example.bin             # Optional test file

🚀 Getting Started
1. Clone the repository
git clone https://github.com/deepak-kiran/File-Signature-Analyzer.git
cd File-Signature-Inspector

2. Ensure your CSV file is present

Your Hex.csv must contain:
ASCII File Description, Header, File Extension, File Class, Header Offset, Trailer
...

3. Run the script
python analyzer.py

🤝 Contributing
Pull requests are welcome!
If you want to add more signatures, update Hex.csv in the correct format.

📄 License
MIT License — free for personal and commercial use.

🌟 Support the Project
If you find this useful, give the repo a ⭐ on GitHub!
It helps others discover the tool and motivates further development.
