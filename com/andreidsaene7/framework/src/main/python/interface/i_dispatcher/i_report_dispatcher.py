# i_dispatcher.py
from abc import ABC, abstractmethod

class IDispatcher(ABC):
    @abstractmethod
    def execute(self):
        pass
