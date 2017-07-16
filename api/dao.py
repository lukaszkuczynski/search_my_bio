from abc import abstractmethod


class Dao:
    @abstractmethod
    def all_projects(self):
        pass

    @abstractmethod
    def hello(self):
        pass



class ElasticDao(Dao):
    pass