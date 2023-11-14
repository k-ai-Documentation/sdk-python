import httpx

from modules.KaiStudioCredentials import KaiStudioCredentials


class ManageInstance:
    __credentials: KaiStudioCredentials

    def __init__(self, credentials: KaiStudioCredentials):
        self.__credentials = credentials
        self.__baseurl = f"https://{self.__credentials.organizationId}.kai-studio.ai/{self.__credentials.instanceId}/"
        self.__imaUrl = "https://ima.kai-studio.ai/"

    async def get_global_health(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.get(self.__baseurl + "global/health",
                                            headers={"api-key": self.__credentials.apiKey})
                return response.text
            except Exception as err:
                print(err)

    async def is_api_alive(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.get(self.__baseurl + "health", headers={"api-key": self.__credentials.apiKey})
                return response.text
            except Exception as err:
                print(err)

    async def generate_new_api_key(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "generate-new-apikey", headers=headers)
                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def update_name(self, name: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "update-name", headers=headers, json={
                    "name": name
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def deploy(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "deploy", headers=headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def delete(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "delete", headers=headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def add_kb(self, kb_type, options):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "add-kb", headers=headers, json={
                    'type': kb_type,
                    'options': options
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def update_kb(self, kb_id, options):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "update-kb", headers=headers, json={
                    'id': kb_id,
                    'options': options
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def remove_kb(self, kb_id):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__imaUrl + "update-kb", headers=headers, json={
                    'id': kb_id
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)
