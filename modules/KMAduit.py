import httpx

from modules.KaiStudioCredentials import KaiStudioCredentials


class KMAudit:
    __credentials: KaiStudioCredentials

    def __init__(self, credentials: KaiStudioCredentials):
        self.__credentials = credentials
        self.__baseurl = f"https://{self.__credentials.organizationId}.kai-studio.ai/{self.__credentials.instanceId}/"
        self.__headers = {
            'api-key': self.__credentials.apiKey
        }

    async def get_conflict_information(self, limit, offset):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/conflict-information", headers=self.__headers, json={
                    "limit": limit,
                    "offset": offset
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def get_duplicated_information(self, limit, offset):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/duplicated-information", headers=self.__headers, json={
                    "limit": limit,
                    "offset": offset
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def set_conflict_managed(self, information_id):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/conflict-information/set-managed", headers=self.__headers, json={
                    "id": information_id
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def set_duplicated_information_managed(self, information_id):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/duplicated-information/set-managed", headers=self.__headers, json={
                    "id": information_id
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)
