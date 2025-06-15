# i_dataframe_saver.py
from abc import ABC, abstractmethod
import pandas as pd

class IDataFrameSaver(ABC):
    @abstractmethod
    def save(self, df: pd.DataFrame, filename: str):
        pass
