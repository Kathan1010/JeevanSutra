from fpdf import FPDF
import os

pdf = FPDF()
pdf.add_page()

pdf.set_font("Helvetica", "B", 16)
pdf.cell(0, 10, "Sanjeevani Hospital - Laboratory & Vitals Report", ln=True, align="C")
pdf.ln(5)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Patient Information", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, "Name: Sam", ln=True)
pdf.cell(0, 8, "Patient ID: sam-987654321", ln=True)
pdf.cell(0, 8, "Location: ICU-S1", ln=True)
pdf.ln(5)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Vital Signs", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, "Heart Rate: 115 bpm", ln=True)
pdf.cell(0, 8, "Systolic BP: 85 mmHg", ln=True)
pdf.cell(0, 8, "Diastolic BP: 50 mmHg", ln=True)
pdf.cell(0, 8, "Respiratory Rate: 28 breaths/min", ln=True)
pdf.cell(0, 8, "SpO2: 88 %", ln=True)
pdf.cell(0, 8, "FiO2: 0.6", ln=True)
pdf.cell(0, 8, "Temperature: 39.1 °C", ln=True)
pdf.ln(5)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Laboratory Results", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.cell(0, 8, "Potassium: 5.8 mmol/L", ln=True)
pdf.cell(0, 8, "Sodium: 135 mmol/L", ln=True)
pdf.cell(0, 8, "Creatinine: 2.1 mg/dL", ln=True)
pdf.cell(0, 8, "Bilirubin: 3.5 mg/dL", ln=True)
pdf.cell(0, 8, "Platelets: 85 x10^3/uL", ln=True)
pdf.cell(0, 8, "WBC: 18.2 x10^3/uL", ln=True)
pdf.cell(0, 8, "Lactate: 4.5 mmol/L", ln=True)
pdf.ln(5)

pdf.set_font("Helvetica", "B", 12)
pdf.cell(0, 10, "Clinical Notes", ln=True)
pdf.set_font("Helvetica", "", 11)
pdf.multi_cell(0, 8, "Patient Sam presents with acute distress. Blood culture is pending but suspect MRSA. Patient is on high vasopressor support. GCS 13. High risk of sepsis.")

output_path = "sam_lab_report.pdf"
pdf.output(output_path)
print(f"Generated {output_path}")
