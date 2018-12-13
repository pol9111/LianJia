from copy import deepcopy

class Base(object):

    def json(self):
        """object to json"""
        d = deepcopy(self.__dict__)
        print(d)
        for k, v in d.items():
            print(k, v)
            if not v:
                continue
            if isinstance(v, Ershouf):
                d[k] = v.json()
        return d

class Ershouf(Base):

    def __init__(self, **kwargs):
        """init ershouf object"""
        super().__init__()
        self.house_code = 'aaahouse_code'
        self.house_area = ''
        self.title = 'aaatitle'


a = Ershouf()
b = a.json()
print(b)
