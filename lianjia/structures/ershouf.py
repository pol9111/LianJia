from lianjia.structures import Base

class Ershouf(Base):

    def __init__(self, **kwargs):
        """init ershouf object"""
        super().__init__()
        self.house_code = kwargs.get('house_code')
        self.house_area = kwargs.get('house_area')
        self.title = kwargs.get('title')
        self.frame_type = kwargs.get('frame_type')
        self.floor_level = kwargs.get('floor_level')
        self.floor_total = kwargs.get('floor_total')
        self.orientation = kwargs.get('orientation')
        self.building_type = kwargs.get('building_type')
        self.decoration_type = kwargs.get('decoration_type')
        self.building_year = kwargs.get('building_year')
        self.deal_property = kwargs.get('deal_property')
        self.list_time = kwargs.get('list_time')
        self.house_type = kwargs.get('house_type')
        self.elevator = kwargs.get('elevator')
        self.total_price = kwargs.get('total_price')
        self.list_price = kwargs.get('list_price')
        self.unit_price = kwargs.get('unit_price')
        self.resblock_name = kwargs.get('resblock_name')
        self.resblock_id = kwargs.get('resblock_id')
        self.view_url = kwargs.get('view_url') # murl
        self.is_yezhu = kwargs.get('is_yezhu')
        self.subway = kwargs.get('subway') # line_name
        self.tags = kwargs.get('tags') # . title

    def __repr__(self):
        """ershouf to str"""
        return "<二手房: <%s, %s>>" % (self.house_code, self.title if self.title else "")










