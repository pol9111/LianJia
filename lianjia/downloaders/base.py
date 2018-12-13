import asyncio
import math

from tqdm import tqdm


class Downloader(object):

    def __init__(self, handlers=[], batch=10):
        self.handlers = handlers
        self.batch = batch

    def add_handler(self, handler):
        """add one handler"""
        self.handlers.append(handler)

    def set_handlers(self, handlers):
        """set handlers"""
        self.handlers = handlers

    def get_handlers(self):
        """get handlers of downloader"""
        return self.handlers

    def update_progress(self, _):
        """update progress bar"""
        self.bar.update(1)

    async def process_item(self, url):
        """process item"""
        raise NotImplementedError

    def process_items(self, urls):
        """process item"""
        with tqdm(total=len(urls)) as self.bar:
            loop = asyncio.get_event_loop()
            total_step = int(math.ceil(len(urls) / self.batch))
            for step in range(total_step):
                start, end = step * self.batch, (step+1) * self.batch
                print('Processing %d-%d of files' % (start + 1, end))
                urls_batch = urls[start: end]
                tasks = [asyncio.ensure_future(self.process_item(url)) for url in urls_batch]
                for task in tasks:
                    task.add_done_callback(self.update_progress)
                loop.run_until_complete(asyncio.wait(tasks))

    def download(self, inputs):
        """download"""
        if isinstance(inputs, list):
            temps = []
            for url in inputs:
                # print('Processing', url, '...')
                temps.append(url)
                if len(temps) == self.batch:
                    self.process_items(temps)
                    temps = []
        else:
            inputs = inputs if isinstance(inputs, list) else [inputs]
            self.process_items(inputs)

