import sys
sys.path.append(r".")

import win32com.client
from com.andreidsaene7.framework.src.main.python.interface.i_sender.i_email_sender import IEmailSender
from com.andreidsaene7.framework.src.main.python.common.core.model.email import Email


class OutlookEmailSender(IEmailSender):
    def send_email(self, email: Email) -> None:
        outlook = win32com.client.Dispatch("Outlook.Application")
        mail = outlook.CreateItem(0)

        mail.Subject = email.subject
        mail.Body = email.body
        mail.To = ";".join(email.to)
        mail.CC = ";".join(email.cc)

        for attachment in email.attachments:
            mail.Attachments.Add(attachment)

        mail.Send()
