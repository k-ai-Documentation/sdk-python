import httpx


class Core:

    def __init__(self, headers, base_url):
        self.__baseurl = base_url
        self.__headers = headers

    async def count_documents(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/orchestrator/stats/count-documents", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)
