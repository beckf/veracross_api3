import requests
import math
import time
from urllib import parse


class Veracross:
    def __init__(self, school_route, client_id, client_secret, scopes):
        self.school_route = school_route
        self.base_url = f"https://api.veracross.com/{school_route}/v3"
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
