import requests
from urllib.parse import urlencode

class graphapi:
    """Graph API class
    """
    def __init__(self):
        self.url = "https://graph.facebook.com"
    
    def set_version(self, version):
        """Set api version
        
        Arguments:
            version {String} -- Api version. Sample: v3.3
        """
        self.version = version
    
    def set_access_token(self, access_token):
        """Set Access token
        
        Arguments:
            access_token {String} -- Access Token
        """
        self.access_token = access_token
    
    
class api(graphapi):
    """Api manager class
    
    Arguments:
        graphapi {Class} -- Inheriting graphapi class
    """

    def __init__(self):
        graphapi.__init__(self)
    
    def generateurl(self, link):
        url = self.url + "/" + self.version + "/" + link        
        return url

    def get(self, link, params={}):
        """Get request to api
        
        Arguments:
            link {String} -- Link into the graph api
            params {Dictionary} -- list of get parameters
        """

        params["access_token"] = self.access_token

        url = self.generateurl(link)

        response = requests.get(url=url, params=params)

        return response.json()

    def delete(self, link, params={}):
        """Delete request to api
        
        Arguments:
            link {String} -- Link into the graph api
        """

        params["access_token"] = self.access_token

        url = self.generateurl(link)

        response = requests.delete(url=url, params=params)

        return response.json()