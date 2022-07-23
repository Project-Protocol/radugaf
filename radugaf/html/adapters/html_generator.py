from domonic import body, div, footer, head, html, style, meta
from radugaf.html import ports


class HTMLGenerator(ports.IHTMLGenerator):
    def __init__(self):
        pass

    def build_head(self, style: style, meta_tags: meta) -> head:
        return head(style, meta_tags)

    def build_body(self) -> body:
        return body('Body')

    def build_footer(self) -> footer:
        return footer('Footer')

    def build_document(self, header: head, body: body, footer: footer) -> html:
        return html(header, body, footer)
