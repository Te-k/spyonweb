import requests
from urllib.parse import urljoin

class SpyOnWebInvalidToken(Exception):
    def __init__(self):
        Exception.__init__(self,"Invalid token to SpyOnWeb")

class SpyOnWebNotFound(Exception):
    def __init__(self):
        Exception.__init__(self,"The requested value was not found on SpyOnWeb")

class SpyOnWebError(Exception):
    def __init__(self, message):
        self.message = message
        Exception.__init__(self, message)

class SpyOnWeb(object):
    def __init__(self, token):
        self.token = token
        self.baseurl = 'https://api.spyonweb.com/'

    def _get(self, url, params={}):
        """
        Send request to the SpyOnWeb server to the given URL with valid token
        """
        params['access_token'] = self.token
        r = requests.get(urljoin(self.baseurl, url), params=params)
        if r.json()['status'] == 'error':
            if r.json()['message'] == 'unauthorized':
                raise SpyOnWebInvalidToken()
            else:
                raise SpyOnWebError(r.json()['message'])
        else:
            return r.json()

    def summary(self, domain):
        """
        Get number of domain sharing Google Adsense, Analytics,
        IP address and nameserer with the given domain
        """
        r = self._get(urljoin('/v1/summary/', domain))
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']['summary'][domain]['items']

    def domain(self, domain):
        """
        Get domains related to a domain, limited to 100 domains
        """
        r = self._get(urljoin('/v1/domain/', domain))
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']

    def adsense(self, adsenseid, limit=None, start=None):
        """
        Return domains related to a adsense id
        """
        if limit is None and start is None:
            r = self._get(urljoin('/v1/adsense/', adsenseid))
        else:
            r = self._get(
                urljoin('/v1/adsense/', adsenseid),
                {'limit': limit, 'start': start}
            )
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']['adsense'][adsenseid]

    def analytics(self, analyticid, limit=None, start=None):
        """
        Return domains related to a Google Analytics id
        """
        if limit is None and start is None:
            r = self._get(urljoin('/v1/analytics/', analyticid))
        else:
            r = self._get(
                urljoin('/v1/analytics/', analyticid),
                {'limit': limit, 'start': start}
            )
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']['analytics'][analyticid]

    def ip(self, addr, limit=None, start=None):
        if limit is None and start is None:
            r = self._get(urljoin('/v1/ip/', addr))
        else:
            r = self._get(
                urljoin('/v1/ip/', addr),
                {'limit': limit, 'start': start}
            )
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']['ip'][addr]

    def nameserver_domain(self, domain, limit=None, start=None):
        if limit is None and start is None:
            r = self._get(urljoin('/v1/dns_domain/', domain))
        else:
            r = self._get(
                urljoin('/v1/dns_domain/', domain),
                {'limit': limit, 'start': start}
            )
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']['dns_domain'][domain]

    def nameserver_ip(self, addr, limit=None, start=None):
        if limit is None and start is None:
            r = self._get(urljoin('/v1/ip_dns/', addr))
        else:
            r = self._get(
                urljoin('/v1/ip_dns/', addr),
                {'limit': limit, 'start': start}
            )
        if r['status'] == 'not_found':
            raise SpyOnWebNotFound
        else:
            return r['result']['ip_dns'][addr]
