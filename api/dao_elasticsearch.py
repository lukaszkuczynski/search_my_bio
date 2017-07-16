from api.dao import Dao
from elasticsearch import Elasticsearch


class ElasticDao(Dao):

    def __init__(self, config):
        self.host = config['host']
        self.port = config['port']
        self.index_pattern = config['index_pattern']
        self.es = Elasticsearch(hosts=['%s:%s' % (self.host, self.port)])

    def is_alive(self):
        health = self.es.cat.health()
        return (health is not None)

    def is_cluster_configured(self):
        return self.is_index_present(self) and self.is_type_present(self)

    def is_index_present(self):
        index_present = self.es.indices.exists('searchmybio*')
        return index_present