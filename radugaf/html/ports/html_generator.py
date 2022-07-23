from abc import ABC, abstractmethod

from domonic import head


class IHTMLGenerator(ABC):
    @abstractmethod
    def build_head(self, meta_tags: str) -> head:
        raise NotImplementedError()

    @abstractmethod
    def build_document(self, meta_tags: str) -> str:
        raise NotImplementedError()
