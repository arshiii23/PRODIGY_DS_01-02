📊 Task 01: Population Distribution Visualization

📌 Project Overview

This project focuses on analyzing and visualizing population data using Python. The goal is to understand how population is distributed across different countries using graphical representations such as histograms and bar charts.
🎯 Objective

Create a Histogram to visualize the distribution of population across countries
Create a Bar Chart to compare populations of the top countries
Gain hands-on experience with data handling and visualization libraries
🗂️ Dataset

Source: World Bank Population Dataset
File Used: "API_SP.POP.TOTL_DS2_en_csv_v2.csv"
The dataset contains:
Country names
Country codes
Year-wise population data (1960–2023)
🛠️ Technologies Used

Python
Pandas (Data manipulation)
Matplotlib (Data visualization)
Seaborn (Enhanced visualization)
🚀 Steps Performed

Data Loading
Imported dataset using Pandas
Skipped unnecessary header rows
Data Cleaning
Selected relevant columns (Country Name & Year)
Removed missing values
Data Visualization
📊 Histogram

Displays distribution of population across countries
Helps identify spread and concentration
📊 Bar Chart

Shows top 10 most populated countries
Enables easy comparison
📷 Output

Histogram

Shows most countries fall under lower to mid population range
Few countries have extremely high population
Bar Chart

Highlights top populated countries clearly
Countries like India and China dominate
💡 Key Insights

Population distribution is highly skewed
Majority of countries have smaller populations
Only a few countries contribute to a large share of global population
▶️ How to Run the Project

Install required libraries:
pip install pandas matplotlib seaborn

Run the Python script:
python task1.py

Output graphs will be saved in the project folder
📈 Future Improvements

Add interactive visualizations
Compare multiple years
Perform deeper statistical analysis
🙌 Conclusion

This project helped in understanding how to:

Work with real-world datasets
Clean and process data
Create meaningful visualizations


🚢 Task 2: Titanic Dataset - Data Cleaning & Exploratory Data Analysis (EDA)

📌 Project Overview

This project focuses on performing data cleaning and exploratory data analysis (EDA) on the Titanic dataset. The goal is to understand patterns, relationships, and key factors that influenced passenger survival.

🎯 Objectives

Clean and preprocess raw data
Handle missing values and inconsistencies
Explore relationships between variables
Visualize patterns and trends using graphs
Extract meaningful insights from the dataset
📂 Dataset

Dataset used: Titanic - Training Dataset
File: "train.csv"
Source: Kaggle / Provided dataset
🛠️ Technologies Used

Python 🐍
Pandas
Matplotlib
Seaborn
🧹 Data Cleaning Steps

Filled missing values in "Age" using median
Filled missing values in "Embarked" using mode
Dropped "Cabin" column due to excessive missing values
Checked and confirmed no remaining null values
📊 Exploratory Data Analysis (EDA)

✔️ Visualizations Created:

Survival Count
Survival by Gender
Age Distribution
Survival by Passenger Class
Correlation Heatmap
🔍 Key Insights

👩 Female passengers had a significantly higher survival rate than males
🏆 Passengers in 1st class had better survival chances
👶 Younger passengers had relatively higher survival probability
💰 Socio-economic status (class) played an important role in survival
📊 Some features showed moderate correlation with survival
▶️ How to Run the Project

Step 1: Install Dependencies

pip install pandas matplotlib seaborn

Step 2: Run the Script

python main.py

📁 Output

Graphs are saved as ".png" files in the project folder
Insights are displayed in the terminal
🚀 Future Improvements

Add feature engineering (e.g., FamilySize)
Build a machine learning model for prediction
Perform deeper statistical analysis
📌 Conclusion

This project demonstrates the importance of data cleaning and visualization in understanding datasets and extracting meaningful insights.

🙌 Author 
Arsheen Shaikh
---
