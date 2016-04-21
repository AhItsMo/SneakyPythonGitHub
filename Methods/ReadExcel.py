import xlrd

class read_excel():

    def get_data_from_excel("D:\Automation"):
        # create an empty ist to get data
        rows = []
        # open excel workbook
        book = xlrd.open_workbook("D:\Automation")
        # get excel sheet
        sheet = book.sheet_by_name("sheet1")
        for row_index in range(1,sheet.nrows):
            rows.append(list(sheet.row_values(row_index, 0 , sheet.ncols)))
        return rows