import requests


class BaseHttp(object):
    host = 'http://localhost'

    # 统一http发送方式
    def sendHttp(self, path, method='post', **kwargs):
        url = '{}{}'.format(self.host, path)
        result = requests.request(method=method, url=url, **kwargs)
        return result
