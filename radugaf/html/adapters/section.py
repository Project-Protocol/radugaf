from domonic import body, div, h1, head, hr, html, style


class Section:
    """
    A section is composed from multiple components.
    """

    # TODO: Will be added in future iterations
    def build_qr_code(self):
        pass

    # TODO: Find a proper package to handle image processing
    def place_logo(self):
        pass

    def add_identifier(self):
        """
        The identifier is composed from the following components:
        - Document type symbol
        - Divider between document type symbol & document reference number
        - Reference number (e.g. 'ref.123456.01')
        """
        pass


class Component:
    def __init__(self):
        pass

    def build_square(self):
        styles = style(
            """
            .square-identifier {
              display: flex;
              align-items: center;
              justify-content: center;
              
              font-size: 50vw; /* Use vw, vh, vmin, vmax as needed */
              width: 0.3em; /* Relates to vw/vh font size */
              height: 0.3em; /* Use any other number to change aspect ratio */
              
              box-sizing: border-box;
              overflow: hidden;
              background: #9895FF;
              border-radius: 10px;
            }

            .square-identifier .symbol-identifier {
              font-size: 2rem;
              color: #ffffff;
              text-align: center;
            }
            """
        )
        return body(head(styles), div(_class='square-identifier').html(div(h1('F'), _class='symbol-identifier')))
