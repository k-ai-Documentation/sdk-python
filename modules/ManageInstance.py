import httpx


class ManageInstance:
    def __init__(self, headers, base_url):
        self.__baseurl = base_url
        self.__headers = headers
        self.__imaUrl = "https://ima.kai-studio.ai/"

    async def get_global_health(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.get(self.__baseurl + "global/health", headers=self.__headers)
                return response.text
            except Exception as err:
                print(err)

    async def version(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.get(self.__baseurl + "version", headers=self.__headers)
                return response.text
            except Exception as err:
                print(err)

    async def is_api_alive(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.get(self.__baseurl + "health", headers=self.__headers)
                return response.text
            except Exception as err:
                print(err)

    async def generate_new_api_key(self) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "generate-new-apikey", headers=self.__headers)
                return response.json()['response'] if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def update_name(self, name: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "update-name", headers=self.__headers, json={
                    "name": name
                })
                return response.json()['response'] if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def deploy(self) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "deploy", headers=self.__headers)
                return response.json()['response'] if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def delete(self) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "delete", headers=self.__headers)
                return response.json()['response'] if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def add_kb(self, kb_type, options) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "add-kb", headers=self.__headers, json={
                    'type': kb_type,
                    'options': options
                })
                return response.json()['response'] if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def update_kb(self, kb_id, options) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "update-kb", headers=self.__headers, json={
                    'id': kb_id,
                    'options': options
                })
                return response.json()['response'] if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def remove_kb(self, kb_id) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__imaUrl + "update-kb", headers=self.__headers, json={
                    'id': kb_id
                })
                return response.json()['response'] if response.status_code == 200 else response.text
            except Exception as err:
                print(err)
