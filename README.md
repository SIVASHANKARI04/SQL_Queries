
Live App Link: https://stunning-lamp-7vjqr6vw6wwfx765-8501.app.github.dev/

# San Francisco Salaries Dashboard

## 🚀 Overview

The **San Francisco Salaries Dashboard** is an interactive web application built with **Streamlit** that provides insights into salary trends, job roles, and compensation distribution in San Francisco. The dashboard is powered by **AWS RDS MySQL**, allowing real-time data analysis and visualization.

## 🎯 Features

- 📌 Query selection to explore different salary-related insights
- 📊 Data visualizations using **Matplotlib** and **Plotly**
- ☁️ **AWS RDS MySQL integration** for dynamic data retrieval
- 🎨 Custom background for an engaging UI

## 🛠 Tech Stack

- **Python** (Pandas, MySQL Connector)
- **Streamlit** (Interactive Dashboard)
- **Matplotlib & Plotly** (Data Visualization)
- **AWS RDS** (Database Storage)

## 📌 How to Run

### Prerequisites:
1. Install Python (>=3.8)
2. Install required dependencies:
   ```bash
   pip install streamlit pandas mysql-connector-python matplotlib plotly
   ```

### Run the Application:
```bash
streamlit run app.py
```

## 📊 Queries Implemented

- Top 10 highest salaries
- Average salary by job title
- Employees ordered by total pay benefits
- Job titles with an average base pay ≥ $100K
- Total compensation per year
- Employees with highest overtime percentage

## 🌍 Deployment

- Hosted on **AWS EC2**
- Uses **AWS RDS** for database management



