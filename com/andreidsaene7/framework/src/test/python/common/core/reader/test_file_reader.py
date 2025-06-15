# com/andreidsaene7/framework/projecto1/src/test/core/reader/file_reader/test_file_reader.py
import sys
sys.path.append(r".")
import pytest
import pandas as pd
from com.andreidsaene7.framework.src.main.python.common.core.reader.excel_file_reader import ExcelFileReader


@pytest.fixture
def excel_reader():
    return ExcelFileReader()


def test_read_excel_file(tmp_path, excel_reader):
    file_path = tmp_path / "example.xlsx"
    expected_df = pd.DataFrame({"col1": [1, 2], "col2": ["a", "b"]})
    expected_df.to_excel(file_path, index=False)

    result_df = excel_reader.read(str(file_path))

    pd.testing.assert_frame_equal(result_df, expected_df)
