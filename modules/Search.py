from typing import List

import httpx

from modules.KaiStudioCredentials import KaiStudioCredentials


class DocumentResult:
    id: str
    name: str
    url: str


class SearchResult:
    query: str
    answer: str
    confidentRate: float
    gotAnswer: bool
    documents: List[DocumentResult]


class Search:
    __credentials: KaiStudioCredentials

    def __init__(self, credentials):
        self.__credentials = credentials
        self.__baseurl = f"https://{self.__credentials.organizationId}.kai-studio.ai/{self.__credentials.instanceId}/"
        self.__headers = {
            'api-key': self.__credentials.apiKey
        }

    # return SearchResult
    async def query(self, query, user):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/query", headers=self.__headers, json={
                    "query": query,
                    "user": user
                })
                return response.text

            except Exception as err:
                print(err)

    async def get_related_documents(self, query):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/related-documents", headers=self.__headers,
                                             json={
                                                 "query": query
                                             })

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def get_doc_signature(self, docId):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/doc/" + docId, headers=self.__headers)

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def get_doc_ids(self, docIds):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/docs", headers=self.__headers, json={
                    "docsIds": docIds
                })

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def count_done_requests(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/stats/count-search", headers=self.__headers)

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def count_answered_done_requests(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/stats/count-answered-search",
                                             headers=self.__headers)

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def generate_following_question(self, previousAnswer: str, comment: str):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/generate-following-question",
                                             headers=self.__headers,
                                             json={
                                                 "previousAnswer": previousAnswer,
                                                 "comment": comment
                                             })

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)
