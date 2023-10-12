import openpyxl
from tempfile import NamedTemporaryFile
from win32com import client
import os
import pandas as pd
from win32com import client
from tqdm import tqdm

excel = client.Dispatch("Excel.Application")
# Open Microsoft Excel

def convert_to_pdf(input_file,output_file):
    # Read Excel File
    sheets = excel.Workbooks.Open(input_file)
    work_sheets = sheets.Worksheets[0]
    
    # Convert into PDF File
    work_sheets.ExportAsFixedFormat(0, output_file)
    sheets.Close(True) 
    print(f"Saved the pdf receipt to {output_file}")

# Open the Excel workbook
workbook = openpyxl.load_workbook('./templates/Invoice.xlsx')
df = pd.read_csv("templates/isCusatian.csv")
# Select the worksheet
worksheet = workbook['Template']

# Update cells
for index,row in tqdm(df.iterrows(),total=df.shape[0]):

    serial_number = "0000"+str(row['id'])
    worksheet['B19'] = row['Prefix']+". "+row['Name'].title()
    worksheet['B20'] = row['Insitution/Company']
    worksheet['G12'] = serial_number #INVOICE NUMBER

    if row['isCusatian'] is True:
        # cgst = 0
        sgst = "Rs. 114.41"
        cost = "Rs. 1271.19"
        total = "Rs. 1500.00"
        roundoff = "Rs. -0.01"
        output_path = f"Output/Cusatian/{row['Name'].title()}.xlsx"
        output_file = f"Output/Cusatian/{row['Name'].title()}.pdf"
    elif row['isCusatian'] is False:
        sgst = "Rs. 305.1"
        cost = "Rs. 3390.0"
        total = "Rs. 4000.0"
        roundoff = "Rs. -0.2"
        output_path = f"Output/Non_Cusatian/{row['Name'].title()}.xlsx"
        output_file = f"Output/Non_Cusatian/{row['Name'].title()}.pdf"

    worksheet['G26'] = cost
    worksheet['H26'] = cost
    worksheet['H29'] = cost
    worksheet['H30'] = sgst
    worksheet['H31'] = sgst
    worksheet['H32'] = roundoff
    worksheet['H33'] = total

    workbook.save(output_path)
    convert_to_pdf(os.path.abspath(output_path),os.path.abspath(output_file))
    os.remove(os.path.abspath(output_path))


# Save the workbook

  
