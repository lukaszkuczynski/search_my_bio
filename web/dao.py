from abc import abstractmethod, ABCMeta


class Dao:
    __metaclass__ = ABCMeta

    @abstractmethod
    def all_projects(self):
        pass

    @abstractmethod
    def is_alive(self):
        pass




