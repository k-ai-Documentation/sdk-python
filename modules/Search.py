from typing import List

import httpx


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
    reason: str
    documents: List[DocumentResult]
    followingQuestions: List[str]

    def __init__(self, query: str, answer: str, confidentRate: float, gotAnswer: bool, reason: str,
                 documents: List[DocumentResult],
                 followingQuestions: List[str]):
        self.query = query
        self.answer = answer
        self.rate = confidentRate
        self.reason = reason
        self.gotAnswer = gotAnswer
        self.documents = documents
        self.followingQuestions = followingQuestions


class Search:

    def __init__(self, headers, base_url):
        self.__baseurl = base_url
        self.__headers = headers

    # return SearchResult
    async def query(self, query, user, impersonate, multiDocuments, needFollowingQuestions) -> SearchResult:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/query", headers=self.__headers, json={
                    "query": query,
                    "user": user,
                    "impersonate": impersonate,
                    "multiDocuments": multiDocuments,
                    "needFollowingQuestions": needFollowingQuestions,
                })
                return SearchResult(**response.json()["response"]) if response.status_code == 200 else response.text

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

    async def identify_specific_document(self, conversation) -> int:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/search/identify-specific-document",
                                             headers=self.__headers,
                                             json={"conversation": conversation})

                return response.json()['response'] if response.status_code == 200 else response.text

            except Exception as err:
                print(err)
