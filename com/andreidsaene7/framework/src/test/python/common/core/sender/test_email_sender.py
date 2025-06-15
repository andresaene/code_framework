import sys
sys.path.append(r".")
import pytest
from unittest.mock import patch, MagicMock
from com.andreidsaene7.framework.src.main.python.common.core.model.email import Email
from com.andreidsaene7.framework.src.main.python.common.core.sender.email_sender import OutlookEmailSender


@pytest.fixture
def sample_email():
    return Email(
        subject="Relatório",
        body="Segue o relatório",
        to=["andre@empresa.co.mz"],
        cc=["gestor@empresa.co.mz"],
        attachments=["relatorio.xlsx"]
    )


@patch("com.andreidsaene7.framework.src.main.python.common.core.sender.email_sender.win32com.client.Dispatch")
def test_send_email_success(mock_dispatch, sample_email):
    mock_outlook = MagicMock()
    mock_mail = MagicMock()
    mock_dispatch.return_value = mock_outlook
    mock_outlook.CreateItem.return_value = mock_mail

    sender = OutlookEmailSender()
    sender.send_email(sample_email)

    mock_dispatch.assert_called_with("Outlook.Application")
    mock_mail.Subject = sample_email.subject
    mock_mail.Body = sample_email.body
    mock_mail.To = ";".join(sample_email.to)
    mock_mail.CC = ";".join(sample_email.cc)
    mock_mail.Attachments.Add.assert_called_with("relatorio.xlsx")
    mock_mail.Send.assert_called_once()
