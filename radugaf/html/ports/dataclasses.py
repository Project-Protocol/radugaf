from dataclasses import dataclass
from typing import List


@dataclass
class DivStyles:
    display: str
    background: str
    margin: str
    margin_bottom: str
    width: str
    height: str
    box_shadow: str = None

    def to_css(self) -> str:
        css = ''
        for key, value in self.__dict__.items():
            key = key.replace('_', '-') if '_' in key else key
            css += f'{key}: {value};'

        return css


@dataclass
class BodyStyles:
    background: str

    def to_css(self) -> str:
        css = ''
        for key, value in self.__dict__.items():
            css += f'{key}: {value};'

        return css


@dataclass
class MetaTags:
    author: str = None
    charset: str = None
    viewport: str = None
    description: str = None
    keywords: List[str] = None

    def to_css(self) -> str:
        css = ''
        for key, value in self.__dict__.items():
            key = key.replace('_', '-') if '_' in key else key
            css += f'{key}: {value};'

        return css
