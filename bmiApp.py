import streamlit as st

st.markdown("# :red[🏋️เเอปพลิเคชันคำนวนค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลน้ำหนักเเละส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ (กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ (เซนติเมตร):")

if st.button("คำนวนค่า BMI  "):
   # เเปลงส่วนสูงจาก cm เป็น เมตร เเล้วคำนวน BMI
   height_m = height_cm / 100
   bmi = weight / (height_m ** 2)

   st.write("---")
   st.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")

if bmi < 18.5:
    st.warning(" คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0:
    st.success(" คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
elif 23.0 <= bmi < 25.0:
    st.info(" คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
else:
    st.error(" คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพเเละออกกำลังกาย ")

st.divider()
st.write("นางสาว ศรุตา จันทร์ยอด เลขที่20 ม.4/7")  
