import tempfile

import streamlit as st

from utils.pdf_reader import read_pdf
from extractors.inspection_extractor import extract_observations
from extractors.thermal_extractor import extract_thermal_issues
from generators.ddr_generator import generate_ddr


st.set_page_config(page_title="DDR Generator", layout="wide")

st.title("Detailed Diagnostic Report (DDR) Generator")
st.write(
    "Upload the inspection report and thermal images PDF to generate a Detailed Diagnostic Report."
)


def _save_uploaded_pdf(uploaded_file) -> str:
    """Save a Streamlit uploaded file to a temporary PDF path and return the path."""
    suffix = ".pdf"
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.read())
        return tmp.name


col1, col2 = st.columns(2)

with col1:
    inspection_file = st.file_uploader(
        "Inspection Report PDF", type=["pdf"], key="inspection_uploader"
    )

with col2:
    thermal_file = st.file_uploader(
        "Thermal Images PDF", type=["pdf"], key="thermal_uploader"
    )

generate_clicked = st.button("Generate DDR Report")

if generate_clicked:
    if not inspection_file or not thermal_file:
        st.error("Please upload both the inspection report and thermal images PDF.")
    else:
        with st.spinner("Reading PDFs and generating DDR report..."):
            inspection_path = _save_uploaded_pdf(inspection_file)
            thermal_path = _save_uploaded_pdf(thermal_file)

            inspection_text = read_pdf(inspection_path)
            thermal_text = read_pdf(thermal_path)

            observations = extract_observations(inspection_text)
            thermal = extract_thermal_issues(thermal_text)

            ddr = generate_ddr(observations, thermal)

        st.success("DDR Report generated successfully.")

        st.subheader("Generated DDR Report")
        st.markdown(ddr)

        st.download_button(
            label="Download DDR Report as .txt",
            data=ddr,
            file_name="Final_DDR_Report.txt",
            mime="text/plain",
        )

