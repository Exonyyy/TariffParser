from parser import Parser
from config import url, needed_section, excel_name
from utilities import ConvertTable, ExcelWriter

if __name__ == "__main__":
    p = Parser(url)
    data = p.parse(needed_section)

    converted_data = ConvertTable(data).convert_all()
    data_save = ExcelWriter(converted_data)
    data_save.save_to_excel(excel_name)
