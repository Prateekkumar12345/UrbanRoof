from utils.pdf_reader import read_pdf
from extractors.inspection_extractor import extract_observations
from extractors.thermal_extractor import extract_thermal_issues
from generators.ddr_generator import generate_ddr
import os

inspection_path = "Sample Report.pdf"
thermal_path = "Thermal Images.pdf"


print("Reading inspection report...")
inspection_text = read_pdf(inspection_path)

print("Reading thermal report...")
thermal_text = read_pdf(thermal_path)


print("Extracting inspection observations...")
observations = extract_observations(inspection_text)


print("Extracting thermal findings...")
thermal = extract_thermal_issues(thermal_text)


print("Generating DDR report...")
ddr = generate_ddr(observations, thermal)




os.makedirs("output", exist_ok=True)

with open("output/Final_DDR_Report.txt", "w", encoding="utf-8") as f:
    f.write(ddr)


print("DDR Report Generated Successfully")