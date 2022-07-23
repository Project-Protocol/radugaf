from abc import ABC, abstractmethod


class IMetaData(ABC):
    @abstractmethod
    def determine_which_meta_tags_to_generate(self):
        raise NotImplementedError()

    @abstractmethod
    def build_meta_tags(self):
        raise NotImplementedError()
