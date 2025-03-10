import streamlit as st
import pandas as pd
import textwrap
import base64
import mysql.connector
import matplotlib.pyplot as plt
import plotly.express as px

# Function to connect to MySQL database
def get_db_connection():
    return mysql.connector.connect(
        host="database-2.ctc8c66sc4zs.ap-south-1.rds.amazonaws.com",  # Update with your AWS RDS endpoint
        user="admin",
        password="pocketpocket",
        database="AWSSQL",
        port=3306
    )


# Set up background image
def set_bg_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url(data:image/png;base64,{encoded_string});
        background-size: cover;
        background-repeat: no-repeat;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
set_bg_image("E:\\DSDemo\\Demoprojects\\abstract-dark-background-with-flowing-colouful-waves_1048-13124.avif")


# Function to execute a query and return the result as a pandas DataFrame
def run_query(query):
    conn = get_db_connection()
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"Error executing query: {e}")
        return None
    finally:
        conn.close()

# Streamlit UI
st.title("San Francisco Salaries Dashboard")

# Query selection
query_options = [
    "Top 10 highest salaries",
    "Average salary by job title",
    "All employees ordered by their total pay benefits in descending order",
    "List job titles with an average base pay ≥ $100K, ordered by pay (highest first)",
    "Total compensation per year",
    "Employees with highest overtime percentage"
]
selected_query = st.selectbox("Select a query to visualize:", query_options)

# SQL Queries
queries = {
    "Top 10 highest salaries": 
        "SELECT EmployeeName, JobTitle, TotalPay FROM Salaries1 ORDER BY TotalPay DESC LIMIT 10;",
    "Average salary by job title": 
        "SELECT JobTitle, AVG(TotalPay) AS AvgSalary FROM Salaries1 GROUP BY JobTitle ORDER BY AvgSalary DESC;",
    "All employees ordered by their total pay benefits in descending order": 
        "select EmployeeName,TotalPayBenefits from Salaries1 order by TotalPayBenefits desc;",
    "List job titles with an average base pay ≥ $100K, ordered by pay (highest first)":
        "select JobTitle,avg(BasePay) as Avg_BasePay from Salaries1 group by JobTitle having Avg_BasePay >= 100000 order by Avg_BasePay desc",
    "Total compensation per year": 
        "SELECT Year, SUM(TotalPayBenefits) AS TotalCompensation FROM Salaries1 GROUP BY Year ORDER BY Year;",
    "Employees with highest overtime percentage": 
        "SELECT EmployeeName, (OvertimePay / TotalPay) * 100 AS OvertimePercentage FROM Salaries1 ORDER BY OvertimePercentage DESC LIMIT 10;"
}

# Execute selected query
if selected_query:
    query = queries[selected_query]
    data = run_query(query)
    if data is not None and not data.empty:
        st.dataframe(data)

        # Visualizations
        if selected_query == "Top 10 highest salaries":
            plt.figure(figsize=(10, 6))
            plt.bar(data["EmployeeName"], data["TotalPay"], color='skyblue')
            plt.xticks(rotation=45)
            plt.title("Top 10 Highest Salaries")
            plt.xlabel("Employee Name")
            plt.ylabel("Total Salary")
            st.pyplot(plt)
        
        elif selected_query == "Average salary by job title":
            fig = px.bar(data, x="JobTitle", y="AvgSalary", title="Average Salary by Job Title", color="AvgSalary")
            st.plotly_chart(fig)
        
        elif selected_query == "List job titles with an average base pay ≥ $100K, ordered by pay (highest first)":
            data["JobTitle"] = data["JobTitle"].apply(lambda x: "\n".join(textwrap.wrap(x, width=25)))
            plt.figure(figsize=(12, 6))  
            plt.bar(data["JobTitle"], data["Avg_BasePay"], color='skyblue')
            plt.ylabel("Average Base Pay ($1000s)")
            plt.xlabel("Job Titles")
            plt.title("Job Titles with Average Base Pay ≥ $100K", fontsize=14)
            plt.xticks(rotation=45, ha="right", fontsize=10)
            plt.yticks(fontsize=10)
            st.pyplot(plt)

        elif selected_query == "Total compensation per year":
            plt.figure(figsize=(10, 6))
            plt.plot(data["Year"], data["TotalCompensation"], marker='o', color='blue')
            plt.title("Total Compensation Per Year")
            plt.xlabel("Year")
            plt.ylabel("Total Compensation")
            st.pyplot(plt)
        
        elif selected_query == "Employees with highest overtime percentage":
            fig = px.bar(data, x="EmployeeName", y="OvertimePercentage", title="Employees with Highest Overtime Percentage", color="OvertimePercentage")
            st.plotly_chart(fig)
    else:
        st.warning("No data available for this query.")

st.text("Thank you for using the dashboard!")

