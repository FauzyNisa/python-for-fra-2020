# %conda update -n base -c defaults conda

# %conda install -c conda-forge aiohttp  pysocks geopy googletrans cchardet nest-asyncio

# %pip install twint

import twint
# https://github.com/twintproject/twint/wiki/Basic-usage
# http://docs.tweepy.org/en/latest/getting_started.html#introduction
import nest_asyncio
# mencegah event loop -> kernel nya selalu jalan di jupyter kernelnya pake event loop
# twint -> code nya tu tipe ayang ngejalanin terus sampe limit
# mencegah bentrok event loop si twint kernel jupyter

nest_asyncio.apply()
twi = twint.Config()

twi.Search = 'ASEAN'
twi.Lang = "en"
twi.Store_json = True
twi.Output = "hasil/ASEAN(en).js"
twi.Limit = 100 #kelipatan 20
twint.run.Search(twi)