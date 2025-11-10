import streamlit as st

st.set_page_config(
    page_title="ZAIDYN ETL Test Case Generator",
    page_icon="🧩",
    layout="centered"
)

# Header
st.markdown(
    "<h1 style='text-align: center; color: #2b7cff;'>ZAIDYN ETL Test Case Generator</h1>",
    unsafe_allow_html=True
)

st.write("---")

col1, col2 = st.columns(2)

# Upload section
with col1:
    st.subheader("Upload ETL Script")
    uploaded_script = st.file_uploader(
        "Choose your ETL Script file (.py or .sql)",
        type=["py", "sql"],
        label_visibility="collapsed"
    )

    if uploaded_script:
        st.success(f"✅ Script '{uploaded_script.name}' uploaded successfully!")

with col2:
    st.subheader("Upload Schema File")
    uploaded_schema = st.file_uploader(
        "Choose your Schema file (.csv, .xlsx, or .json)",
        type=["csv", "xlsx", "json"],
        label_visibility="collapsed"
    )

    if uploaded_schema:
        st.success(f"✅ Schema '{uploaded_schema.name}' uploaded successfully!")

st.write("---")

# Logs section
st.subheader("Logs")
log_box = st.empty()

if uploaded_script and uploaded_schema:
    with st.spinner("🔍 Processing files..."):
        import time
        for i in range(5):
            log_box.text(f"Processing step {i+1}/5...\n")
            time.sleep(1)
        st.success("✅ Test Case Generation Completed!")

    st.download_button(
        label="⬇️ Download Generated Test Cases",
        data="Sample test case content (replace with real logic)",
        file_name="generated_test_cases.txt",
        mime="text/plain"
    )
else:
    st.info("Upload both Script and Schema to generate test cases.")