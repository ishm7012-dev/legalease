import streamlit as st
import requests

# Step 1: Streamlit Page Configuration
st.set_page_config(page_title="LegalEase", layout="centered")

# Initialize session state for storing the generated document across re-renders
if "generated_text" not in st.session_state:
    st.session_state.generated_text = ""

# Helper formatting functions (replace with your custom module imports if defined elsewhere)
def sanitize_text(text):
    return text.strip() if text else ""

def format_html_preview(text):
    return f"<div style='background-color: #f8f9fa; padding: 15px; border-radius: 8px; border: 1px solid #ddd; color: #212529;'>{text.replace('\n', '<br>')}</div>"

def format_docx(text, doc_type="document"):
    return text.encode('utf-8')

def format_pdf(text, doc_type="document"):
    return text.encode('utf-8')


# Step 2: Title and Header
st.markdown(
    "<h2 style='text-align: center;'>AI Legal Document Generator</h2>",
    unsafe_allow_html=True
)

# Step 3: User Inputs
document_type = st.text_input("Document Type", placeholder="e.g., Non-Disclosure Agreement")
parties = st.text_area("Parties Involved", placeholder="e.g., Company A and John Doe")
terms = st.text_area("Terms & Conditions (Use semicolons for bullet points)")
dates = st.text_input("Effective Date", placeholder="e.g., 2026-10-01")

# Step 4: Generate Document Button
if st.button("🚀 Generate Document"):
    if not document_type or not parties:
        st.warning("Please fill in at least the Document Type and Parties Involved.")
    else:
        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        }
        
        with st.spinner("Generating document via FastAPI & Gemini AI..."):
            try:
                response = requests.post("http://localhost:8000/generate", json=payload)
                if response.status_code == 200:
                    raw_text = response.json().get("document", "")
                    st.session_state.generated_text = sanitize_text(raw_text)
                    st.success("Document generated successfully!")
                else:
                    err_detail = response.json().get("detail", response.text)
                    st.error(f"Server Error ({response.status_code}): {response.text}")
            except Exception as e:
                st.error(f"Could not connect to FastAPI backend at http://localhost:8000. Make sure your Uvicorn server is running! Error: {e}")

# Step 5: Render Previews and Downloads only when text exists
if st.session_state.generated_text:
    st.markdown("---")
    st.subheader("Document Preview")
    
    # HTML Preview
    styled_html = format_html_preview(st.session_state.generated_text)
    st.markdown(styled_html, unsafe_allow_html=True)
    st.write("")

    # Editable Document Preview
    edited_text = st.text_area("Edit Document Below:", st.session_state.generated_text, height=300)
    st.session_state.generated_text = edited_text

    st.subheader("Export Options")
    file_prefix = document_type.replace(' ', '_').lower() if document_type else "legal"

    # Download Buttons
    st.download_button(
        label="📄 Download as .TXT",
        data=st.session_state.generated_text,
        file_name=f"{file_prefix}_document.txt",
        mime="text/plain"
    )
    
    st.download_button(
        label="📝 Download as .DOCX",
        data=format_docx(st.session_state.generated_text, document_type),
        file_name=f"{file_prefix}_document.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    
    st.download_button(
        label="📕 Download as .PDF",
        data=format_pdf(st.session_state.generated_text, document_type),
        file_name=f"{file_prefix}_document.pdf",
        mime="application/pdf"
    )