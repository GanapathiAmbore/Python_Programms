import xlsxwriter
wb=xlsxwriter.Workbook("Sample.xlsx")
sheet=wb.add_worksheet("Python_programm")

sheet.write("A1","Hello")
sheet.write("B1","What i am doing i don't know")

wb.close()
