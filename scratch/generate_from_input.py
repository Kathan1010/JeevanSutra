import os
import sys
import json
import argparse

# Add backend to path so we can import utils
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "backend"))
from utils.pdf_export import generate_report_pdf

def generate_from_json(json_path: str, output_path: str):
    if not os.path.exists(json_path):
        print(f"Error: Could not find input file '{json_path}'")
        return

    with open(json_path, "r") as f:
        data = json.load(f)
    
    patient = data.get("patient", {})
    report = data.get("report", {})
    
    # Generate the PDF bytes
    pdf_bytes = generate_report_pdf(report, patient)
    
    # Save the PDF
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)
    
    print(f"PDF report generated successfully at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate PDF report from a JSON input file")
    parser.add_argument("input_json", help="Path to the JSON input file")
    parser.add_argument("--output", "-o", default="generated_report.pdf", help="Path for the output PDF file")
    
    args = parser.parse_args()
    generate_from_json(args.input_json, args.output)
