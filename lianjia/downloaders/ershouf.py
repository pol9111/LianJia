from lianjia.downloaders import Downloader
from lianjia.handlers import Handler
from lianjia.structures import Ershouf


class ErshoufDownloader(Downloader):

    async def process_item(self, url):
        """process item"""
        print('Processing', url, '...')
        for handler in self.handlers:
            if isinstance(handler, Handler):
                await handler.process(url)