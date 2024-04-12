import httpx


class Thematic:

    def __init__(self, headers, base_url):
        self.__baseurl = base_url
        self.__headers = headers

    async def get_topic(self, topic):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/topic", headers=self.__headers, json={
                    'topic': topic
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def get_kbs(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/kbs", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def get_documents(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/documents", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def add_audit_question(self, question, answer):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/add-audit-question", headers=self.__headers,
                                             json={
                                                 "question": question,
                                                 "answer": answer
                                             })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def update_audit_question(self, question_id, question, answer):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/update-audit-question", headers=self.__headers,
                                             json={
                                                 "id": question_id,
                                                 "question": question,
                                                 "answer": answer
                                             })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def list_audit_questions(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/list-audit-questions", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def get_test_running_state(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/test-running-state", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def run_test(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/run-test", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def list_topics(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/list/topics", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def get_subtopic(self, subtopic):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/subtopic", headers=self.__headers, json={
                    "subtopic": subtopic
                })
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def count_topics(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/stats/count-topics", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def count_subtopics(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/stats/count-subtopics", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def count_documents(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/stats/count-documents", headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def count_audit_questions(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/stats/count-audit-questions",
                                             headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)

    async def count_validated_audit_questions(self):
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "api/audit/stats/count-validated-audit-questions",
                                             headers=self.__headers)
                return response.json() if response.status_code == 200 else response.text
            except Exception as err:
                print(err)
