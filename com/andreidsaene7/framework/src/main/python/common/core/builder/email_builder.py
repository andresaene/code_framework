

# com/andreidsaene7/framework/src/main/python/bot/core/builder/email_builder/email_builder.py

from typing import List
from com.andreidsaene7.framework.src.main.python.common.core.model.email import Email
from com.andreidsaene7.framework.src.main.python.interface.i_builder.i_email_builder import IEmailBuilder



class EmailBuilder(IEmailBuilder):
    def __init__(self):
        self._subject = ""
        self._body = ""
        self._to = []
        self._cc = []
        self._attachments = []

    def with_subject(self, subject: str):
        self._subject = subject
        return self

    def with_body(self, body: str):
        self._body = body
        return self

    def with_to(self, to: List[str]):
        self._to = to
        return self

    def with_cc(self, cc: List[str]):
        self._cc = cc
        return self

    def with_attachments(self, attachments: List[str]):
        self._attachments = attachments
        return self

    def build(self) -> Email:
        return Email(
            subject=self._subject,
            body=self._body,
            to=self._to,
            cc=self._cc,
            attachments=self._attachments
        )
