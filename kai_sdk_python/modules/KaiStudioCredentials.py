class KaiStudioCredentials:
    organizationId: str
    instanceId: str
    apiKey: str
    host: str

    def __init__(self, apiKey, organizationId="", instanceId="", host=""):
        self.organizationId = organizationId
        self.instanceId = instanceId
        self.apiKey = apiKey
        self.host = host
