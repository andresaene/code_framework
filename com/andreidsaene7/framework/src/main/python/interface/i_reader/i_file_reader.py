# com/andreidsaene7/framework/common/interfaces/i_reader/i_file_reader.py
from abc import ABC, abstractmethod
import pandas as pd


class IFileReader(ABC):
    @abstractmethod
    def read(self, file_path: str) -> pd.DataFrame:
        pass
