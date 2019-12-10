from openpyxl import Workbook 
#import openpyxl 

#create a workbook variable 
workbook = Workbook()
#setting the sheet to the active sheet
sheet = workbook.active

#adding hello world
sheet["A1"] = "hello"
sheet["B1"] = "world!"

#saving the workbook 
workbook.save(filename="hello_world.xlsx")
