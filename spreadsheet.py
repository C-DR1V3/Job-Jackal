from openpyxl import Workbook

class SpreadSheet:
    filepath = ""
    def __init__(self, filepath):
        self.filepath = filepath
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet["A1"] = "Title"
        self.sheet["B1"] = "Company"
        self.sheet["C1"] = "Location"
        self.sheet["D1"] = "Wage"
        self.sheet["E1"] = "URL"


    def PopulateNewRow(self,rownum, title, company, location, wage, url):
        a = "A" + str(rownum)
        b = "B" + str(rownum)
        c = "C" + str(rownum)
        d = "D" + str(rownum)
        e = "E" + str(rownum)

        self.sheet[a] = title
        self.sheet[b] = company
        self.sheet[c] = location
        self.sheet[d] = wage
        self.sheet[e] = url

    def ApplyAutomaticColumnWidth(self):
        for col in self.sheet.columns:
            max_length = 0
            column = col[0].column_letter  # Get the column name
            for cell in col:
                try:  # Necessary to avoid error on empty cells
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            self.sheet.column_dimensions[column].width = adjusted_width

    def Save_Workbook(self):
        self.workbook.save(self.filepath)