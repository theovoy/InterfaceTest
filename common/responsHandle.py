import json

class ResponseHandle:
    def __init__(self, response):
        self.response = json.loads(response)