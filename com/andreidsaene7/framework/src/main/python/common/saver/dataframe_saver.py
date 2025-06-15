import pandas as pd
import os
from com.andreidsaene7.framework.src.main.python.interface.i_saver.i_dataframe_saver import IDataFrameSaver

class DataFrameSaver(IDataFrameSaver):
    def __init__(self, output_dir: str):
        self.output_dir = output_dir

    def save(self, df: pd.DataFrame, filename: str):
        filepath = os.path.join(self.output_dir, filename)
        df.to_excel(filepath, index=False)
