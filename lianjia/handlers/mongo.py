from motor.motor_asyncio import AsyncIOMotorClient
from lianjia.handlers import Handler
from lianjia.structures.ershouf import Ershouf


class MongoHandler(Handler):

    def __init__(self, conn_uri=None, db='lianjia'):
        """init mongo object"""
        super().__init__()
        if not conn_uri:
            conn_uri = '127.0.0.1'
        self.client = AsyncIOMotorClient(conn_uri)
        self.db = self.client[db]

    async def process(self, obj, **kwargs):
        """save data to mongo"""
        collection_name = 'default'
        if isinstance(obj, Ershouf):
            collection_name = 'ershouf'
        collection = self.db[collection_name]
        print('Saving', obj, 'to mongodb..')
        if await collection.insert_one(obj.json()):
            print('Saved', obj, 'to mongodb successfully')
        else:
            print('Error occurred while saving', obj)