from copy import deepcopy

from lianjia.structures import Ershouf


class Base(object):

    def json(self):
        """object to json"""
        d = deepcopy(self.__dict__)
        for k, v in d.items():
            if not v:
                continue
            if isinstance(v, Ershouf):
                d[k] = v.json()
        return d










