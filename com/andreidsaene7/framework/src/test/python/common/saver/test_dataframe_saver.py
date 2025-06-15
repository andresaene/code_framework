# test_dataframe_saver.py
import sys
sys.path.append(".")
import pandas as pd
from com.andreidsaene7.framework.src.main.python.common.saver.dataframe_saver import DataFrameSaver

def test_dataframe_saver_saves_excel_file(tmp_path):
    # Arrange
    df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    filename = "teste.xlsx"
    saver = DataFrameSaver(output_dir=str(tmp_path))

    # Act
    saver.save(df, filename)

    # Assert
    saved_file = tmp_path / filename
    assert saved_file.exists()

    # Verifica conteúdo básico
    loaded_df = pd.read_excel(saved_file)
    assert loaded_df.equals(df)
