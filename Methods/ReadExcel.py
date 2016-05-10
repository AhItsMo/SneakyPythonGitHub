import xlrd


class read_excel:

    def get_data_from_excel(sheet_name):
        # create an empty ist to get data
        rows = []
        # open excel workbook and get excel sheet
        book = xlrd.open_workbook("SneakyPythonGitHubTestData.xlsx")
        sheet = book.sheet_by_name(sheet_name)
        for row_index in range(1, sheet.nrows):
            rows.append(list(sheet.row_values(row_index, 0, sheet.ncols)))
        return rows
