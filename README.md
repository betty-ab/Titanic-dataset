# Task 3: Data Analysis with Pandas

## Project Overview
This project focuses on data manipulation and exploratory data analysis (EDA) using the **Pandas** library. It demonstrates the ability to build custom datasets from scratch and perform deep-dive analysis on real-world historical data to uncover survival patterns.

##  Tech Stack
* **Language:** Python 3.10+
* **Library:** Pandas
* **Environment:** Google Colab / Jupyter Notebook
* **Source Data:** Titanic Dataset (train.csv)

---

##  Project Structure

### Part 1: Custom Dataset Foundation
I created a custom  dataset using a Python dictionary to demonstrate:
* Building DataFrames from structured dictionaries.
* Generating 15 rows of diverse data (Strings, Integers).
* Implementing a **Custom Index** using list comprehension (`f'INV-{i}'`) for unique identification.

### Part 2: Titanic Real-World Analysis
A comprehensive analysis of the Titanic disaster focusing on the following steps:
1. **Exploration:** Using `.head()`, `.info()`, and `.describe()` to understand data types and statistics.
2. **Data Cleaning:** * Handled missing **Age** values using the **Median**.
   * Handled missing **Embarked** values using the **Mode**.
   * Dropped the **Cabin** column due to high null counts.
   * Ensured data integrity by removing duplicates.
3. **Data Analysis:** Used `groupby()` to calculate survival rates across different demographics.
4. **Filtering:** Isolated specific cohorts (surviving females and children) to verify survival trends.

---

##  Step 5: Insights (Final Evaluation)

Based on the analysis, here are the clear answers to the research questions:

### 1. Who was more likely to survive?
**Females** were significantly more likely to survive. The survival rate for women was approximately **74%**, while the survival rate for men was only around **19%**. 
### 2. Did class affect survival?
**Yes, social class was a major factor.** There is a direct correlation between a passenger's class and their survival probability:
* **1st Class:** ~63% survival rate
* **2nd Class:** ~47% survival rate
* **3rd Class:** ~24% survival rate

### 3. Were children prioritized?
**Yes.** The data shows that **Children (Ages 0-12)** had a higher survival rate than most adult categories, confirming that age was a prioritized factor during the evacuation.

### 4. What combination had the highest survival rate?
The highest survival probability was found among **Females in 1st Class**, with a survival rate nearing **97%**. Conversely, the lowest survival probability was found among **Males in 3rd Class**.

---

## 🚀 How to Run this Project
1. Open the Google Colab Link-    https://colab.research.google.com/drive/1-u8dODHqhfBIfCMf-O9jKGtM6JlZmfLY?usp=sharing
2. Ensure you have an active internet connection to fetch the dataset from the remote URL.
3. Run all cells to see the results and the generated DataFrames.

