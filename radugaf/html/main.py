# TODO: Features to add
# - [ ] Development mode (where the document is presented as a A4 page)
# - [ ] Document frame (a border that sorrounds the A4 page)
# - [ ] Section arhitecture
# - [ ] Sections can have types: header, footer
# - [ ] Each section is composed of components
# - [ ] Components can have purposes: header, footer (they act as constraints)

from __future__ import annotations

from dataclasses import dataclass
from inspect import signature
from typing import Dict, List, Union

from dataclass_wizard import JSONFileWizard, YAMLWizard
from domonic import style


def camel_to_dashed(text: str) -> str:
    return ''.join(['-' + c.lower() if c.isupper() else c for c in text]).lstrip('-')


def underscore_to_camel(text: str) -> str:
    return ''.join([c.upper() if c == '_' else c for c in text]).lstrip('_')


@dataclass
class DocumentProvider(YAMLWizard):
    document_provider_fields: DocumentProviderFields


@dataclass
class DocumentProviderFields(YAMLWizard, JSONFileWizard):
    title: str
    address: str
    phone: str
    email: str
    is_vat_payer: bool
    identification_id: str
    identification_number: str

    # If the document provider is paying VAT then prepend the idfentification_id with 'RO'
    def get_identification_id(self) -> str:
        return "RO" + self.identification_id if self.is_vat_payer else self.identification_id

    def get_css_class_names(self) -> Dict[str, str]:
        css_class_names = dict()
        for key, _ in self.__dict__.items():
            css_class_names[key] = camel_to_dashed(self.__class__.__name__) + '-' + underscore_to_camel(key)

        return css_class_names


class StyleAttributes:
    '''
    Usage:

    params = {'user_id': 1, 'body': 'foo', 'bar': 'baz', 'amount': 10}
    styles = StyleAttributes.from_kwargs(**params)
    print(styles.user_id)
    '''

    @classmethod
    def from_kwargs(cls, **kwargs) -> StyleAttributes:
        # Fetch the constructor's signature
        cls_fields = {field for field in signature(cls).parameters}

        # Split the kwargs into native ones and new ones
        native_args, new_args = {}, {}
        for name, val in kwargs.items():
            if name in cls_fields:
                native_args[name] = val
            else:
                new_args[name] = val

        # Use the native ones to create the class
        ret = cls(**native_args)

        # Now add the new ones by hand
        for new_name, new_val in new_args.items():
            setattr(ret, new_name, new_val)

        return ret

    @classmethod
    def convert_class_to_dict(cls, obj: StyleAttributes) -> Dict[str, Union[str, int, float]]:
        return {key: getattr(obj, key) for key in obj.__dict__}

    def to_dict(self) -> Dict[str, Union[str, int, float]]:
        return StyleAttributes.convert_class_to_dict(self)


class Tools:
    def __init__(self, path: str) -> None:
        self.path = path

    @property
    def data_from_yaml_file(self) -> DocumentProviderFields:
        return DocumentProviderFields.from_yaml_file(self.path)

    @property
    def data_from_json_file(self) -> DocumentProviderFields:
        return DocumentProviderFields.from_json_file(self.path)


class CSSGenerator(Tools):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def get_css_class_names(self) -> Dict[str, str]:
        return self.data_from_yaml_file.get_css_class_names()

    def build_css(self, styling: str) -> style:
        css = ''
        for _, value in self.get_css_class_names().items():
            css += '.' + value + ' {'
            css += styling  # Custom CSS goes here
            css += '}'
            css += '\n'

        return style(css)

    def build_styling(self):
        pass


class Component(Tools):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def build_components(self) -> List[Dict[str, str]]:
        """
        Returns a big ass dictionary with all the information about the component
        [
            {
                title: example_of_component_title,
                return_type: div
                content: <div>Some nested divs</div>
                styling: Some styling here.
            },
            {
                title: example_of_component_title,
                return_type: div
                content: <div>Some nested divs</div>
                styling: Some styling here.
            }
        ]
        """
        # return div(_class='document-provider-title').html(self.data_from_yaml.title)
        return self.data_from_yaml.get_css_class_names()


def generate():
    # params = {'user_id': 1, 'body': 'foo', 'bar': 'baz', 'amount': 10}
    # styles = StyleAttributes.from_kwargs(**params)
    # print(styles.to_dict())

    fields = DocumentProvider.from_yaml_file('invoice.yaml')
    print(fields)


if __name__ == "__main__":
    generate()
