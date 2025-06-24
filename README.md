# Student Grade Analysis App

A simple and interactive web application built with **Streamlit** to analyze and visualize student grades from an Excel file.

## Demo

Try the app live here: **[Student Grade Analysis App](#)** *(replace with actual link when deployed)*

## Features

- Upload an Excel file containing student scores.
- Calculate and display:
  - Total number of students
  - Average score
  - Score distribution (shown as a pie chart)
- Easy-to-use, interactive interface.

## Project Structure

```
student_grade_analysis/
│
├── analyze_grade.py        # Functions for computing average and distribution
├── app.py                  # Main Streamlit application
├── class_grade.xlsx        # Example Excel file with student scores
├── requirements.txt        # List of required Python packages
└── README.md               # Project documentation
```

## Requirements

- Python 3.10 or higher
- streamlit
- pandas
- matplotlib

## How to Install and Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ha-thach/student_grade_analysis.git
   cd student_grade_analysis
   ```

2. (Optional) Create and activate a virtual environment

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Launch the app:
   ```bash
   streamlit run app.py
   ```
## About

This project is designed to help educators or analysts quickly evaluate student performance using Excel-based grade sheets. It provides a simple visual and numerical summary of student grades using Python and Streamlit.

## Resources

- Sample data file: `class_grade.xlsx`
- Streamlit documentation: https://docs.streamlit.io/
- AIO Guildline Documentation 