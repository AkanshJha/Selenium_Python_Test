import openpyxl as xl

file_path = "../TestFiles - Excel/WriteExcel.xlsx"

workbook = xl.load_workbook(file_path)

sheet = workbook.active

for r in range(1, 6):
    for c in range(1,4):
        sheet.cell(row=r, column=c).value = str(r+c)+" value"


workbook.save(file_path)