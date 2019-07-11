import xlsxwriter
wb=xlsxwriter.Workbook("Numbers.xlsx")
sheet=wb.add_worksheet("Number")
row=0
col=0
for number in range(101):
    sheet.write(row,col,number)
    col=col+1
wb.close()