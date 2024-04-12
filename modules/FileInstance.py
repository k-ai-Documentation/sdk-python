from typing import List

import httpx


class KaiStudioFileSignature:
    name: str
    metadata: str

    def __init__(self, name: str, metadata: str):
        self.name = name
        self.metadata = metadata


class KaiStudioFileUploadResponse:
    result: bool
    reason: str

    def __init__(self, result: bool, reason: str):
        self.result = result
        self.reason = reason


class FileInstance:

    def __init__(self, headers):
        self.__headers = headers
        self.__baseurl = "https://fma.kai-studio.ai/"

    async def list_files(self) -> List[KaiStudioFileSignature]:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "list-files", headers=self.__headers)
                file_list = []
                if response.status_code == 200:
                    for file in response.json()["response"]:
                        file_list.append(KaiStudioFileSignature(**file))
                return file_list if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def upload_files(self, files) -> List[KaiStudioFileUploadResponse]:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                if len(files) == 0:
                    return []

                self.__headers = self.__headers | {"Content-Type": "multipart/form-data"}
                response = await client.post(self.__baseurl + "upload-file", files=files, headers=self.__headers)
                file_list = []
                if response.status_code == 200:
                    for file in response.json()["response"]:
                        file_list.append(KaiStudioFileUploadResponse(**file))
                return file_list if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def delete_files(self, fileName: str) -> bool:
        async with httpx.AsyncClient(verify=False, timeout=None) as client:
            try:
                response = await client.post(self.__baseurl + "delete-file", headers=self.__headers, json={
                    "file": fileName
                })

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)
