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
