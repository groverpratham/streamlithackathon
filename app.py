import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="ETL Test Case Generator",
    page_icon="🧩",
    layout="wide"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    logo = Image.open("etl_logo.png")
    st.image(logo, width=80, output_format="PNG", use_container_width=False)
    st.markdown("<div class='sidebar-title'>ETL Test Case Generator</div>", unsafe_allow_html=True)

# Top Header Bar
st.markdown("<div class='top-header'>ETL Test Case Generator</div>", unsafe_allow_html=True)

# Two Upload Sections
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
    st.subheader("Upload ETL Script")
    uploaded_script = st.file_uploader("Choose ETL Script (.py / .sql)", type=["py", "sql"])
    if uploaded_script:
        st.success(f"✅ Script '{uploaded_script.name}' uploaded!")
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='upload-box'>", unsafe_allow_html=True)
    st.subheader("Upload Schema File")
    uploaded_schema = st.file_uploader("Choose Schema (.csv / .xlsx / .json)", type=["csv", "xlsx", "json"])
    if uploaded_schema:
        st.success(f"✅ Schema '{uploaded_schema.name}' uploaded!")
    st.markdown("</div>", unsafe_allow_html=True)

st.write("")

# Logs + Processing Simulation
st.subheader("Logs")
log_box = st.empty()

if uploaded_script and uploaded_schema:
    with st.spinner("Processing..."):
        import time
        for i in range(5):
            log_box.text(f"Step {i+1}/5 running...")
            time.sleep(1)
        st.success("✅ Test Case Generation Completed!")

    st.download_button(
        label="⬇️ Download Test Cases",
        data="Sample test cases",
        file_name="generated_test_cases.txt",
        mime="text/plain"
    )
else:
    st.info("Upload both files to start.")
