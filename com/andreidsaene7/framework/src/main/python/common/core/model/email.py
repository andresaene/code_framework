from typing import List

class Email:
    def __init__(self, subject: str, body: str, to: List[str], cc: List[str], attachments: List[str]):
        self.subject = subject
        self.body = body
        self.to = to
        self.cc = cc
        self.attachments = attachments
