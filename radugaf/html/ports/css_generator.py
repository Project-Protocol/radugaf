from abc import ABC, abstractmethod

from domonic import style

class ICSSGenerator(ABC):
    
    @abstractmethod
    def body_styles(self) -> str:
        raise NotImplementedError()
    
    @abstractmethod
    def div_styles(self) -> str:
        raise NotImplementedError()

    @abstractmethod
    def build_styles(self) -> style:
        raise NotImplementedError()

