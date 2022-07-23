from typing import List

from domonic import meta
from radugaf.html import ports


# It takes in a MetaTags object and returns a string of meta tags
class MetaData(ports.IMetaData):
    def __init__(self, meta_data: ports.MetaTags) -> None:
        '''This function takes in a meta_data object and assigns it to the meta_data attribute of the class

        Parameters
        ----------
        meta_data : ports.MetaTags
            This is a dictionary of metadata that is associated with the data.

        '''
        self.meta_data = meta_data

    def determine_which_meta_tags_to_generate(self) -> List[meta]:
        '''> This function determines which meta tags to generate based on the meta data that was passed in

        Returns
        -------
            A list of meta tags.

        '''
        meta_tags_to_generate = []

        if self.meta_data.charset is not None:
            meta_tags_to_generate.append(meta(charset=f'{self.meta_data.charset}'))

        if self.meta_data.viewport is not None:
            meta_tags_to_generate.append(meta(name='viewport', content=f'{self.meta_data.viewport}'))

        if self.meta_data.description is not None:
            meta_tags_to_generate.append(meta(name='description', content=f'{self.meta_data.description}'))

        if self.meta_data.keywords is not None:
            meta_tags_to_generate.append(meta(name='keywords', content=f'{self.meta_data.keywords}'))

        if self.meta_data.author is not None:
            meta_tags_to_generate.append(meta(name='author', content=f'{self.meta_data.author}'))

        return meta_tags_to_generate

    def build_meta_tags(self) -> str:
        """
        It takes a list of meta tags, converts them to strings, and then joins them together with
        newlines
        :return: A string of meta tags.
        """
        str_metas = []
        for meta_tag in self.determine_which_meta_tags_to_generate():
            str_metas.append(str(meta_tag))

        return '\n'.join(str_metas)
