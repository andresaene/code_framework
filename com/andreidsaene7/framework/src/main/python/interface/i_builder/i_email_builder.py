# com/andreidsaene7/framework/src/main/python/interface/i_builder/i_email_builder/i_email_builder.py

from abc import ABC, abstractmethod
from typing import List
from com.andreidsaene7.framework.src.main.python.common.core.model.email import Email


class IEmailBuilder(ABC):
    @abstractmethod
    def with_subject(self, subject: str):
        pass

    @abstractmethod
    def with_body(self, body: str):
        pass

    @abstractmethod
    def with_to(self, to: List[str]):
        pass

    @abstractmethod
    def with_cc(self, cc: List[str]):
        pass

    @abstractmethod
    def with_attachments(self, attachments: List[str]):
        pass

    @abstractmethod
    def build(self) -> Email:
        pass
