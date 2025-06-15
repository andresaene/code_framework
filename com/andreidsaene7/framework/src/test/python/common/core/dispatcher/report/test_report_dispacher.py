# test_dispatcher.py
import sys
sys.path.append(r".")

import pytest
from unittest.mock import MagicMock
from com.andreidsaene7.framework.src.main.python.common.core.dispatcher.report.report_dispatcher import Dispatcher

def test_dispatcher_reads_saves_and_sends_email():
    mock_reader1 = MagicMock()
    mock_reader1.read.return_value = ("df1", "file1.xlsx")

    mock_reader2 = MagicMock()
    mock_reader2.read.return_value = ("df2", "file2.xlsx")

    mock_saver = MagicMock()
    mock_sender = MagicMock()

    dispatcher = Dispatcher([mock_reader1, mock_reader2], mock_saver, mock_sender)
    dispatcher.execute()

    mock_reader1.read.assert_called_once()
    mock_reader2.read.assert_called_once()
    assert mock_saver.save.call_count == 2
    mock_sender.send.assert_called_once()
