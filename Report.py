import csv
from fpdf import FPDF

# Read data from CSV file
def read_data(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            data.append(row)
    return data

# Analyze data
def analyze_data(data):
    total_sales = sum(int(row[1]) for row in data)
    total_revenue = sum(int(row[2]) for row in data)
    average_sales = total_sales / len(data)
    average_revenue = total_revenue / len(data)
    return total_sales, total_revenue, average_sales, average_revenue

# Generate PDF report
def generate_report(data, total_sales, total_revenue, average_sales, average_revenue):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    pdf.cell(200, 10, txt="Automated Report", ln=True, align='C')
    pdf.set_font("Arial", size=10)
    pdf.cell(30, 10, txt="Date", border=1, align='C')
    pdf.cell(50, 10, txt="Sales", border=1, align='C')
    pdf.cell(50, 10, txt="Revenue", border=1, align='C')
    pdf.ln(10)
    for row in data:
        pdf.cell(30, 10, txt=row[0], border=1, align='C')
        pdf.cell(50, 10, txt=row[1], border=1, align='C')
        pdf.cell(50, 10, txt=row[2], border=1, align='C')
        pdf.ln(10)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Sales: {total_sales}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Total Revenue: {total_revenue}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Average Sales: {average_sales:.2f}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Average Revenue: {average_revenue:.2f}", ln=True, align='L')
    pdf.output("report.pdf")

# Usage
filename = 'data.csv'  # Replace with your CSV file
data = read_data(filename)
total_sales, total_revenue, average_sales, average_revenue = analyze_data(data)
generate_report(data, total_sales, total_revenue, average_sales, average_revenue)

