import xlrd

class Reader:
    def __init__(self):
        self.data = {}
        file_name = "C:/Users/Oliver Marie/OneDrive/Documents/STAT 400/Project 1 Data.xlsx"
        try :
            book = xlrd.open_workbook(file_name)
        except :
            file_name = "C:/Users/Oliver Marie/Documents/Projects/STAT-Project-1/Project 1 Data.xlsx"
            book = xlrd.open_workbook(file_name)

        self.sheet = book.sheet_by_name("2.20.Framingham")
        self.num_rows = self.sheet.nrows
        self.num_cols = self.sheet.ncols

    def get_data (self):
        self.parse()
        return self.data.copy()

    def parse (self):
        sex_Col = 0
        sbp_Col = 1
        dpb_Col = 2
        scl_Col = 3
        chdfate_Col = 4
        followup_Col = 5
        age_Col = 6
        bmi_Col = 7
        month_Col = 8
        id_Col = 9

        for i in range (1,self.num_rows):
            row = self.sheet.row_values(i)
            id = row[id_Col]

            self.data [id] = {
                'sex': row[sex_Col],
                'sbp': row[sbp_Col],
                'dpb': row[dpb_Col],
                'scl': row[scl_Col],
                'chdfate': row[chdfate_Col],
                'followup_Col': row[followup_Col],
                'age': row[age_Col],
                'bmi': row[bmi_Col],
                'month': row[month_Col],
            }
