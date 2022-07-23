import re

from radugaf.html import ports


class CSSTools(ports.ICSSTools):
    def is_hex_code_valid(self, hex_code: str) -> str:
        if not hex_code:
            return 'No hex_code provided'

        if not re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', hex_code):
            return 'Problem with your hex code'

        return hex_code

    def hex_color(self, code: str) -> str:
        return self.is_hex_code_valid(''.join(('#' if not code.startswith('#') else '', f'{code}')))

    def is_rgb_color_valid(self, rgb_color: str) -> str:
        if not rgb_color:
            return 'No rgb_color provided'

        if not re.match(r'^rgb\((\d{1,3}),\s*(\d{1,3}),\s*(\d{1,3})\)$', rgb_color):
            return 'Problem with your rgb color syntax'

        # Deconstruct the rgb color into its components
        red, green, blue = re.findall(r'\d+', rgb_color)

        if int(red) > 255 or int(red) < 0:
            return 'Red component is out of range'

        if int(green) > 255 or int(green) < 0:
            return 'Green component is out of range'

        if int(blue) > 255 or int(blue) < 0:
            return 'Blue component is out of range'

        return rgb_color

    def rgb_color(self, red: int, green: int, blue: int) -> str:
        return self.is_rgb_color_valid(f'rgb({red}, {green}, {blue})')
