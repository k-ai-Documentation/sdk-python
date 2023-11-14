import asyncio

from index import KaiStudio
from index import KaiStudioCredentials


class Credentials(KaiStudioCredentials):
    def __init__(self, organizationId, instanceId, apiKey):
        self.organizationId = organizationId
        self.instanceId = instanceId
        self.apiKey = apiKey


async def main():
    credentials = Credentials("163084b1-5e4c-49c5-b7ec-e41ccca65642",
                              "b6b33cc0-8fe4-4829-bf27-2df41d3f74a9",
                              "yBHhI6yW9vYG+4bi4VwanQVvyk6UYuDtWcZSn1oHT9Q=")
    file_instance = KaiStudio(credentials).file_instance()
    manage_instance = KaiStudio(credentials).manage_instance()
    search = KaiStudio(credentials).search()

    # FILE INSTANCE
    print("UPLOAD FILE:")
    files = {"files": open("files/kai-studio v1.1.pdf", "rb")}
    print(await file_instance.upload_files(files))

    print("LIST FILES:")
    print(await file_instance.list_files())

    print("DELETE FILE:")
    print(await file_instance.delete_files("kai-studio v1.1.pdf"))

    # MANAGE INSTANCE
    print("GET GLOBAL HEALTH:")
    print(await manage_instance.get_global_health())

    print("API IS ALIVE:")
    print(await manage_instance.is_api_alive())

    # SEARCH
    print("SEARCH QUERY:")
    print(await search.query("what is the history of France TV?", "userid"))

    print("RELATED FILES")
    print(await search.query("France TV", "userid"))

    print("GET DOC SIGNATURE:")
    print(await search.get_doc_signature("Azure Blob Storage::b6b33cc0-8fe4-4829-bf27-2df41d3f74a9::Contacter "
                                         "FranceTV.docx"))
    print("GET DOCS BY IDS:")
    print(await search.get_doc_ids(["Azure Blob Storage::b6b33cc0-8fe4-4829-bf27-2df41d3f74a9::Contacter FranceTV.docx",
                                    "Azure Blob Storage::b6b33cc0-8fe4-4829-bf27-2df41d3f74a9::Histoire FTV.docx"]))

    print("COUNT DONE REQUESTS:")
    print(await search.count_done_requests())

    print("COUNT ANSWERED DONE REQUESTS:")
    print(await search.count_answered_done_requests())


if __name__ == "__main__":
    asyncio.run(main())
