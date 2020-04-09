import yaml

def load_config(path):
    '''returns hosts list'''
    with (open(path)) as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        if 'full_url' in config:
            return [config['full_url']]
        else:
            return ['%s:%s' % (config['host'], config['port'])]
