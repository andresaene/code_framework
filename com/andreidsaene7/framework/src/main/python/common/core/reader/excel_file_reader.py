# com/andreidsaene7/framework/projecto1/src/main/core/reader/file_reader.py
import pandas as pd
from com.andreidsaene7.framework.src.main.python.interface.i_reader.i_file_reader import IFileReader


class ExcelFileReader(IFileReader):
    def read(self, file_path: str) -> pd.DataFrame:
        return pd.read_excel(file_path)
