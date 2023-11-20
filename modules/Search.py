from typing import List

import httpx

from modules.KaiStudioCredentials import KaiStudioCredentials


class DocumentResult:
    id: str
    name: str
    url: str
    rate: float

    def __init__(self, id: str, name: str, url: str, rate: float):
        self.id = id
        self.name = name
        self.url = url
        self.rate = rate


class SearchResult:
    query: str
    answer: str
    confidentRate: float
    gotAnswer: bool
    documents: List[DocumentResult]
    followingQuestions: List[str]

    def __init__(self, query: str, answer: str, confidentRate: float, gotAnswer: bool, documents: List[DocumentResult],
                 followingQuestions: List[str]):
        self.query = query
        self.answer = answer
        self.rate = confidentRate
        self.gotAnswer = gotAnswer
        self.documents = documents
        self.followingQuestions = followingQuestions


class Search:
    __credentials: KaiStudioCredentials

    def __init__(self, credentials):
        self.__credentials = credentials
        self.__baseurl = f"https://{self.__credentials.organizationId}.kai-studio.ai/{self.__credentials.instanceId}/"
        self.__headers = {
            'api-key': self.__credentials.apiKey
        }

    # return SearchResult
    async def query(self, query, user) -> SearchResult:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/query", headers=self.__headers, json={
                    "query": query,
                    "user": user
                })
                return SearchResult(**response.json()["response"]) if response.status_code == 200 else response.text

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

    async def count_done_requests(self) -> int:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/stats/count-search", headers=self.__headers)

                return response.json()['response'] if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def count_answered_done_requests(self) -> int:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/stats/count-answered-search",
                                             headers=self.__headers)

                return response.json()['response'] if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def generate_following_question(self, previousAnswer: str, comment: str) -> int:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/generate-following-question",
                                             headers=self.__headers,
                                             json={
                                                 "previousAnswer": previousAnswer,
                                                 "comment": comment
                                             })

                return response.json()['response'] if response.status_code == 200 else response.text

            except Exception as err:
                print(err)
