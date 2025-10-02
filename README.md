# Data Preprocessing Toolkit

This repository provides a **professional Python toolkit** to solve common problems in real-world datasets:  
handling **missing values**, detecting **outliers**, and fixing **encoding issues**.

---

##  Features
- Handle missing values (drop, fill with mean/median/mode)
- Detect outliers using Z-score and IQR methods
- Fix common text encoding issues (UTF-8, latin-1, Persian/Arabic normalization)
- Save cleaned dataset for analytics or machine learning

---

##  Project Structure
data-preprocessing-toolkit/
├── preprocess.py # Main preprocessing script
├── input.csv # Example input dataset
└── output_clean.csv # Processed dataset


##  How to Run
1. Install dependencies:
   ```bash
   pip install pandas numpy chardet

2. Run the script:
   ```bash
   python preprocess.py

 ## Example Input:
id,name,age,income

1,Ali,30,5000

2,Reza,,10000

3,Sara,25,999999

4,Hossein,27,?

## Example Output
id,name,age,income

1,Ali,30,5000

2,Reza,27.3,10000

3,Sara,25,5400

4,Hossein,27,5400


### Author

Ali Zamanpour 

Freelance Data Engineer & AI Specialist

### License

MIT License
