from abc import ABC, abstractmethod


class IGenerator(ABC):
    
    @abstractmethod
    def dummy_function(self):
        raise NotImplementedError()

