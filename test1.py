import requests
import re
import json

headers= {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Upgrade-Insecure-Requests': '1',
    # 'Host': 'bj.meituan.com',
    # 'Cookie': '__mta=149183113.1557128366839.1557129204322.1557129908423.9; uuid=c24b8a409ecbb89047c2.1533608653.0.0.0; oc=LQm2trDKume8xgOOlA3ZzFEXSI2oN-knJr6B3BxylFRjXsTwBEtQ_mRBuP0jZ_zzqr338Wrio-V7w4x8HHhvQlKLqXeCGnFG7z31BI1cpqS4GixZV35JGBrjMf1yHjNSsTLPiTxh1DhI3fnYvivV3cHuvmwYODosSqfkGzDqR2w; _lxsdk_cuid=1651232f287c8-05fb816f428c24-54103515-144000-1651232f287c8; __utma=211559370.570425447.1533608654.1533608654.1533608654.1; __utmv=211559370.|1=city=suzhou=1; ci=1; rvct=1%2C80; _lxsdk_s=16a8c1542cb-358-d49-82%7C%7C18'

}

url = 'https://i.meituan.com/'

response = requests.get(url)

print(response.content.decode('utf-8'))

