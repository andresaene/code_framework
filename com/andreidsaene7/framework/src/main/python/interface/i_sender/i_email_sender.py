from abc import ABC, abstractmethod
from com.andreidsaene7.framework.src.main.python.common.core.model.email import Email

class IEmailSender(ABC):
    @abstractmethod
    def send_email(self, email: Email) -> None:
        pass
