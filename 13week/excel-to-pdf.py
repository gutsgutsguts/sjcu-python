import win32com.client

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

wb = excel.Workbooks.Open(r'C:\sjcu_jsh\\sjcu-python\\grade.xlsx')
ws = wb.Sheets('New-Sheet')
ws.Select()

ws.ExportAsFixedFormat(0, r'C:\\sjcu_jsh\\sjcu-python\\grade.pdf')

wb.Close()
excel.Quit()