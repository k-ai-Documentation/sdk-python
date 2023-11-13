import asyncio
import time

from index import KaiStudio
from index import KaiStudioCredentials


class Credentials(KaiStudioCredentials):
    def __init__(self, organizationId, instanceId, apiKey):
        self.organizationId = organizationId
        self.instanceId = instanceId
        self.apiKey = apiKey


async def main():
    credentials = Credentials("163084b1-5e4c-49c5-b7ec-e41ccca65642",
                              "deab809d-b5a5-4354-8875-1a02fc692cf7",
                              "e5u9aCVqC0I/kMHPRTRBMPGN7JDsOP+u+qKOnG1s/G4=")
    file_instance = KaiStudio(credentials).file_instance()
    manage_instance = KaiStudio(credentials).manage_instance()
    task_list = []
    task = asyncio.create_task(file_instance.list_files())
    task_list.append(task)
    task = asyncio.create_task(manage_instance.get_global_health())
    task_list.append(task)
    await asyncio.gather(*task_list)

if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'RUN TIME：{end - start}')
