import os
import sys
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

# 1. ตั้งค่า Page Configuration เป็น Wide Layout
st.set_page_config(
    page_title="Community Voice Dashboard | เสียงจากชุมชน",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. ปรับแต่ง CSS เพื่อให้ Dashboard แสดงผลเต็มพื้นที่หน้าจอและลดขอบที่ไม่จำเป็น
st.markdown(
    """
    <style>
        /* ซ่อน Streamlit Header, Footer, Menu, Toolbar และ Status Widget */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        footer {
            display: none !important;
        }
        #MainMenu {
            display: none !important;
        }
        div[data-testid="stToolbar"] {
            display: none !important;
        }
        div[data-testid="stDecoration"] {
            display: none !important;
        }
        div[data-testid="stStatusWidget"] {
            display: none !important;
        }

        /* ซ่อนการแจ้งเตือน Floating Badges / Skills Prompt ของ Streamlit */
        div[data-testid="stNotification"],
        div[data-testid="stToast"],
        .stToast,
        div[data-testid="stFloatingElement"],
        div[class*="Toast"],
        div[class*="viewerBadge"],
        div[class*="floatingContainer"],
        div[role="alert"] {
            display: none !important;
        }

        /* ปรับ Main Block Container ให้ไม่มี Padding/Margin และใช้พื้นที่เต็ม 100% */
        .main .block-container {
            padding: 0 !important;
            margin: 0 !important;
            max-width: 100% !important;
            height: 100vh !important;
        }

        /* กำหนดให้ Viewport สูงเต็มจอ */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stMainBlockContainer"], .main {
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        /* ขยาย iframe ของ HTML Dashboard ให้เต็มหน้าจอ 100% ไร้ขอบ */
        iframe {
            width: 100% !important;
            height: 100vh !important;
            border: none !important;
            display: block !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def print_startup_link():
    """แสดงลิงก์ที่คลิกเปิดได้ใน Terminal เมื่อเซิร์ฟเวอร์เริ่มทำงาน"""
    if "port_announced" not in st.session_state:
        st.session_state.port_announced = True
        try:
            port = st.config.get_option("server.port") or 8501
            url = f"http://localhost:{port}"
            message = (
                "\n"
                + "=" * 60
                + "\n"
                + "Community Voice Dashboard is ready!\n"
                + f"URL: {url}\n"
                + "=" * 60
                + "\n"
            )
            if hasattr(sys.stdout, "reconfigure"):
                try:
                    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
                except Exception:
                    pass
            print(message, flush=True)
        except Exception:
            pass


def load_html() -> str:
    """อ่านเนื้อหาจาก index.html ปัจจุบัน"""
    html_path = Path(__file__).parent / "index.html"
    if not html_path.exists():
        st.error(f"ไม่พบไฟล์: {html_path.resolve()} กรุณาตรวจสอบตำแหน่งไฟล์")
        return ""
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()


def main():
    print_startup_link()
    dashboard_html = load_html()
    if dashboard_html:
        # แสดง Dashboard จาก index.html เดิมผ่าน components.html แบบเต็มจอ
        components.html(dashboard_html, height=1200, scrolling=True)


if __name__ == "__main__":
    main()
