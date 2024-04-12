import asyncio
import time

from index import KaiStudio
from index import KaiStudioCredentials

credentials = KaiStudioCredentials(organizationId="your organization id",
                                   instanceId="your instance id",
                                   apiKey="your api key")

file_instance = KaiStudio(credentials).file_instance()
manage_instance = KaiStudio(credentials).manage_instance()
search = KaiStudio(credentials).search()
thematic = KaiStudio(credentials).thematic()
km_audit = KaiStudio(credentials).km_audit()
semantic_graph = KaiStudio(credentials).semantic_graph()


async def sync_mode():
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
    print(await search.get_related_documents("France TV"))

    print("GET DOC SIGNATURE:")
    print(await search.get_doc_signature("Azure Blob Storage: blob storage id::Contacter "
                                         "FranceTV.docx"))
    print("GET DOCS BY IDS:")
    print(await search.get_doc_ids(["Azure Blob Storage::blob storage id::Contacter FranceTV.docx",
                                    "Azure Blob Storage::blob storage id::Histoire FTV.docx"]))

    print("COUNT DONE REQUESTS:")
    print(await search.count_done_requests())

    print("COUNT ANSWERED DONE REQUESTS:")
    print(await search.count_answered_done_requests())

    print("GET TOPIC")
    print(await thematic.get_topic("france.tv application"))

    print("GET KBS STATUS")
    print(await thematic.get_kbs())

    print("GET DOCUMENTS")
    print(await thematic.get_documents())

    print("LIST AUDIT QUESTIONS")
    print(await thematic.list_audit_questions())

    print("GET TEST RUNNING STATE")
    print(await thematic.get_test_running_state())

    print("LIST TOPICS")
    print(await thematic.list_topics())

    print("GET SUBTOPIC")
    print(await thematic.get_subtopic("visio-chat"))

    print("COUNT TOPICS")
    print(await thematic.count_topics())

    print("COUNT SUBTOPICS")
    print(await thematic.count_subtopics())

    print("COUNT DOCUMENTS")
    print(await thematic.count_documents())

    print("COUNT AUDIT QUESTIONS")
    print(await thematic.count_audit_questions())

    print("COUNT VALIDATED AUDIT QUESTIONS")
    print(await thematic.count_validated_audit_questions())


async def async_mode():
    files = {"files": open("files/kai-studio v1.1.pdf", "rb")}

    tasks = [file_instance.upload_files(files), file_instance.list_files(),
             file_instance.delete_files("kai-studio v1.1.pdf"), manage_instance.get_global_health(),
             manage_instance.is_api_alive(), search.query("what is the history of France TV?", "userid"),
             search.query("France TV", "userid"),
             search.get_doc_signature("Azure Blob Storage::blob storage id::Contacter "
                                      "FranceTV.docx"),
             search.get_doc_ids(["Azure Blob Storage::blob storage id::Contacter FranceTV.docx",
                                 "Azure Blob Storage::blob storage id::Histoire FTV.docx"]),
             search.count_done_requests(), search.count_answered_done_requests(),
             thematic.get_topic("france.tv application"),
             thematic.get_kbs(),
             thematic.get_documents(),
             thematic.list_audit_questions(),
             thematic.get_test_running_state(),
             thematic.list_topics(),
             thematic.get_subtopic("visio-chat"),
             thematic.count_topics(),
             thematic.count_subtopics(),
             thematic.count_documents(),
             thematic.count_audit_questions(),
             thematic.count_validated_audit_questions()]
    result_list = await asyncio.gather(*tasks, return_exceptions=False)
    print(result_list)


if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(async_mode())
    print("--- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    asyncio.run(sync_mode())
    print("--- %s seconds ---" % (time.time() - start_time))
