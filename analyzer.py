import os
import csv
import sys
from pathlib import Path


# Converts hex to right format (8e30123t to 8E 30 12 3T)
def normalize_hex(s: str) -> str:
    s = s.replace(" ", "").upper()
    return " ".join(s[i:i+2] for i in range(0, len(s), 2))

# Gets the Header and Trailer byte data from the file
def get_header_trailer(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            file_size = os.fstat(f.fileno()).st_size
            head = f.read(32).hex()
            f.seek(max(0,file_size - 16), os.SEEK_SET)
            tail = f.read(16).hex()
            return head,tail
    else:
        print("\nInvalid file path\n")
        sys.exit(1)

# Prints the Detected Extension and returns it
def validate_extension(ext_path):
    _, ext = os.path.splitext(ext_path)
    print(f"\nGiven File extension: {ext}\n")
    ext = ext.lstrip('.').upper()
    plain_txt_files = ["TXT","CSV","LOG"]
    markup_lang = ["HTML","XML","JSON"]
    config_files = ["INI","CFG","YAML"]
    genric_scrips = ["PY","SH","BAT","PHP"]
    if ext in plain_txt_files:
        print("Given file is a plain text file(.txt, .csv, .log) which has no standard Magic Bytes to verify\n")
        sys.exit(1)
    if ext in markup_lang:
        print("Given file is a text-based formatted (.html, .xml, .json) which has no standard Magic Bytes to verify\n")
        sys.exit(1)
    if ext in config_files:
        print("Given file is a plain text and highly variable in their header bytes (.ini, .cfg, .yaml) which has no standard Magic Bytes to verify\n")
        sys.exit(1)
    if ext in genric_scrips:
        print("Given file is a script file (.py, .sh, .bat, .php) which has no standard Magic Bytes to verify\n")
        sys.exit(1)
    return ext

# Gets all the matching headers that starts with our file signature and returns the largest matching header
def get_main_header(key,CSV_PATH):
    temp_header_list = []
    with open(CSV_PATH, newline="", encoding="utf-8", errors="ignore") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if key.startswith(row["Header"]):
                temp_header_list.append(row["Header"])
    if temp_header_list:    
        return max(temp_header_list)

def main():

    banner = r"""
    _______ __        _____ _                   __                
   / ____(_) /__     / ___/(_)___ _____  ____ _/ /___  __________ 
  / /_  / / / _ \    \__ \/ / __ `/ __ \/ __ `/ __/ / / / ___/ _ \
 / __/ / / /  __/   ___/ / / /_/ / / / / /_/ / /_/ /_/ / /  /  __/
/_/   /_/_/\___/   /____/_/\__, /_/ /_/\__,_/\__/\__,_/_/   \___/ 
           ___            /_____                                  
          /   |  ____  ____ _/ /_  ______  ___  _____             
         / /| | / __ \/ __ `/ / / / /_  / / _ \/ ___/             
        / ___ |/ / / / /_/ / / /_/ / / /_/  __/ /                 
       /_/  |_/_/ /_/\__,_/_/\__, / /___/\___/_/                  
                            /____/                                
    """
    print(banner)
    best_header = []
    description = []  
    
    #Determine the directory where the current Python script is located.
    script_dir = Path(__file__).parent

    #Constructs the path for Hex.csv file combining it with the Python script's directory path
    CSV_PATH = script_dir / "Hex.csv"



    #Takes file path as input and removes quotes ("",'')
    file_path = input("Please enter the File's path you want to check :- ")
    file_path = file_path.replace('"','').replace("'","")

    header,trailer = get_header_trailer(file_path)
    key = normalize_hex(header)
    key2 = normalize_hex(trailer)
    ext = validate_extension(file_path)
    best_header = get_main_header(key,CSV_PATH)

    # Check in CSV file for right header and store all matching header's Description
    if best_header:
        with open(CSV_PATH, newline="", encoding="utf-8", errors="ignore") as g:
            read = csv.DictReader(g)
            for row2 in read:
                if row2["Header"] == best_header:
                    if ext in row2["File Extension"].split('|'):
                        description.append(row2["ASCII File Description"])                 
    else:
        print("No Data Found\n")

    # If data is present in description list Print them
    if description:
        print("✅ VALID FILE\n")
        print("Description : " + " (or) ".join(description) + "\n")
    else:
        print("⚠️  File extension mismatch. Potential disguise.\n")

if __name__ == "__main__":
    main()

