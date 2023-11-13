import httpx

from modules.KaiStudioCredentials import KaiStudioCredentials


client = httpx.AsyncClient()


class KaiStudioFileSignature:
    name: bool
    reason: str


class KaiStudioFileUploadResponse:
    result: str
    metadata: str


class FileInstance:
    __credentials: KaiStudioCredentials

    def __init__(self, credentials: KaiStudioCredentials):
        self.__credentials = credentials
        self.__baseurl = "https://fma.kai-studio.ai/"

    async def list_files(self):
        async with client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }
                response = await client.post(self.__baseurl + "list-files", headers=headers)
                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def upload_files(self, files):
        async with client:
            try:
                if len(files) == 0:
                    return []

                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }

                response = await client.post(self.__baseurl + "upload-file", files=files, headers=headers)

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)

    async def delete_files(self, fileName: str):
        async with client:
            try:
                headers = {
                    'organization-id': self.__credentials.organizationId,
                    'instance-id': self.__credentials.instanceId,
                    'api-key': self.__credentials.apiKey
                }

                response = await client.post(self.__baseurl + "delete-file", headers=headers, json={
                    "file": fileName
                })

                return response.json() if response.status_code == 200 else response.text

            except Exception as err:
                print(err)
