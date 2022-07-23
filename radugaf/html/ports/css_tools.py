from abc import ABC, abstractmethod


class ICSSTools(ABC):
    @abstractmethod
    def is_hex_code_valid(self, hex_code: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def hex_color(self, code: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def is_rgb_color_valid(self, rgb_color: str) -> str:
        raise NotImplementedError()

    @abstractmethod
    def rgb_color(self, red: int, green: int, blue: int) -> str:
        raise NotImplementedError()
