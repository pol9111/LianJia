import lianjia
from lianjia.estates import generate_ershouf_url

# define handler
mongo_handler = lianjia.handlers.MongoHandler(conn_uri='mongodb://Bridi:anNBU7MD@localhost:27017/')
# define downloader and specify handler
downloader = lianjia.downloaders.ErshoufDownloader([mongo_handler])

ershouf_urls = generate_ershouf_url('350200', 20)
downloader.download(ershouf_urls)



