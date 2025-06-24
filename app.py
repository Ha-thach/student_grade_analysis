import streamlit as st
import pandas as pd
from analyze_grade import calculate_average, percentage_distribution
import matplotlib.pyplot as plt


st.title("Phân Tích Điểm Số Học Sinh")

text = ("Ứng dụng này cho phép bạn phân tích điểm số của học sinh trong lớp từ danh sách điểm của lớp (Excel).")

st.write(text)

uploaded_file = st.file_uploader("Chọn file Excel (có cột 'Điểm số')")

if uploaded_file:
    df = pd.read_excel("class_grade.xlsx")
    scores = df["Điểm số"].dropna().astype(float).tolist()
    st.write(f'Tổng số học sinh: {len(scores)}')
    st.write(f'Điểm trung bình: {calculate_average(scores)}')

    st.write("Biểu đồ phân tích điểm số:")

    dict= percentage_distribution(scores)
    labels = list(dict.keys())
    values = list(dict.values())

    fig, ax = plt.subplots(figsize =(6,6))
    ax.pie(
        values, 
        labels = labels, autopct='%1.1f%%', startangle=90)
    st.pyplot(fig)

    