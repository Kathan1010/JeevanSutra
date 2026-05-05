import os
import sys

# Add backend to path so we can import utils
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))

from utils.pdf_export import generate_report_pdf

patient_sam = {
    "name": "Sam",
    "patient_id": "sam-987654321",
    "bed_number": "ICU-S1",
    "status": "admitted"
}

report_sam = {
    "rule_facts": {
        "sofa": {
            "total": 6,
            "sepsis_criteria_met": True,
            "organ_scores": {
                "respiration": 2,
                "coagulation": 1,
                "liver": 0,
                "cardiovascular": 2,
                "cns": 0,
                "renal": 1
            },
            "organ_failures": ["cardiovascular"]
        },
        "qsofa": {
            "total": 2,
            "high_risk": True
        },
        "sirs": {
            "total": 3
        },
        "aki": {
            "stage": 1,
            "trigger": "creatinine",
            "details": "Creatinine increased above baseline"
        },
        "vwrs": {
            "overall": "Not Ready",
            "score": 2,
            "blocking_reasons": ["High Vasopressor Support", "High FiO2"]
        },
        "amr": [
            {
                "organism": "MRSA",
                "severity": "High",
                "resistant_to": ["Methicillin", "Oxacillin"],
                "recommended": ["Vancomycin", "Linezolid"]
            }
        ],
        "outliers": []
    },
    "ai_narrative": "Patient Sam is currently admitted to the ICU and presents with signs of sepsis. The SOFA score is elevated primarily due to respiratory and cardiovascular components. MRSA has been detected, requiring Vancomycin or Linezolid. The patient is currently not ready for ventilator weaning due to high vasopressor requirements.",
    "diagnosis_blocked": False,
    "rule_version": "v2.1.0"
}

# Generate the PDF bytes
pdf_bytes = generate_report_pdf(report_sam, patient_sam)

# Save the PDF to the root directory
output_path = os.path.join(os.path.dirname(__file__), "..", "sam_report.pdf")
with open(output_path, "wb") as f:
    f.write(pdf_bytes)

print(f"PDF report generated successfully at: {output_path}")
