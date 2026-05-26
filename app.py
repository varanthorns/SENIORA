import streamlit as st

# 1. ตั้งค่าเปิดโหมดจอกว้าง และเปลี่ยนชื่อแท็บเว็บให้เข้ากับแอปใหม่
st.set_page_config(layout="wide", page_title="Seniora Value AI", page_icon="🤖")

# 2. ใช้ CSS บังคับลบขอบขาวรอบๆ ของ Streamlit ออกทั้งหมด (บน ซ้าย ขวา ล่าง)
st.markdown("""
    <style>
    /* ลบ padding ช่องว่างของกล่องเนื้อหาหลัก */
    .main .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }
    
    /* ซ่อนแถบด้านบนสุดของ Streamlit */
    header {
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* ซ่อน Footer ด้านล่าง */
    footer {
        visibility: hidden !important;
        height: 0px !important;
    }
    
    /* เคลียร์ระยะขอบตัวแอป */
    .stApp {
        margin: 0px !important;
        padding: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ใส่ลิงก์ของ Lovable อันใหม่
url = "https://seniora-value-ai.lovable.app"

# 4. ใช้ HTML iframe ดึงหน้าเว็บมาแสดง โดยตั้งความสูงไว้ที่ 100vh (เต็มความสูงหน้าจอ)
iframe_html = f"""
    <iframe src="{url}" style="width:100%; height:100vh; border:none; margin:0; padding:0; overflow:hidden;"></iframe>
"""

# 5. แสดงผลหน้าเว็บ
st.markdown(iframe_html, unsafe_allow_html=True)
