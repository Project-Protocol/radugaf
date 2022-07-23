from domonic import style
from radugaf.html import ports


class CSSGenerator(ports.ICSSGenerator):
    def __init__(self, body_css: ports.BodyStyles, div_css: ports.DivStyles):
        self.body_css = body_css
        self.div_css = div_css

    def body_styles(self) -> str:
        return f'body {{{self.body_css.to_css()}}}'

    def div_styles(self) -> str:
        return f'.page {{{self.div_css.to_css()}}}'

    def build_styles(self) -> style:
        return style(f'{self.body_styles()} {self.div_styles()}')

