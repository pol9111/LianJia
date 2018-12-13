import aiohttp

from lianjia.handlers import Handler


class FetchHandler(Handler):

    async def _process(self, url, **kwargs):
        """start request"""
        print('Downloading', url, '...')
        kwargs.update({'ssl': False})
        kwargs.update({'timeout': 10})
        # complete kwargs
        async with aiohttp.ClientSession() as session:
            async with session.get(url, **kwargs) as resp:
                if resp.status == 200:
                    print('Request succeed', url)
                    # save to database
                else:
                    print('Request failed', url)

    async def process(self, url, **kwargs):
        """process obj"""
        return await self._process(url, **kwargs)



