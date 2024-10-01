import asyncio

from index import KaiStudio
from index import KaiStudioCredentials

credentials = KaiStudioCredentials(organizationId="your organization id",
                                   instanceId="your instance id",
                                   apiKey="your api key")

manage_instance = KaiStudio(credentials).manage_instance()
search = KaiStudio(credentials).search()
km_audit = KaiStudio(credentials).km_audit()
semantic_graph = KaiStudio(credentials).semantic_graph()
core = KaiStudio(credentials).core()


async def sync_mode():
    # CORE
    print("COUNT DOCUMENTS")
    print(await core.count_documents())

    print("COUNT INDEXABLE DOCUMENTS")
    print(await core.count_indexable_documents())

    print("COUNT INDEXED DOCUMENTS")    
    print(await core.count_indexed_documents())

    print("COUNT DETECTED DOCUMENTS")
    print(await core.count_detected_documents())

    # print("DOWNLOAD FILE")
    print(await core.download_file("file_id"))

    print("DIFFERENTIAL INDEXATION")
    print(await core.differential_indexation())

    print("GET SCENARIOS")
    print(await core.get_scenarios())

    # print("GET LOGS")
    print(await core.get_logs("type", 0, 10))

    # print("REINIT_ALL")
    print(await core.reinit_all())

    # AUDIT
    # print("GET ALL TASK LINKED TO A DOCUMENT")
    print(await km_audit.get_all_tasks_linked_to_a_document("document_id"))

    print("GET CONFLICT INFORMATION")
    print(await km_audit.get_conflict_information(20, 0))

    print("GET DUPLICATED INFORMATION")
    print(await km_audit.get_duplicated_information(20, 0))

    print("SET CONFLIT MANAGED")
    print(await km_audit.set_conflict_managed("information_id"))

    print("SET DUPLICATED MANAGED")
    print(await km_audit.set_duplicated_information_managed("information_id"))

    print("GET DOCUMENTS TO MANAGE")
    print(await km_audit.get_documents_to_manage(20, 0))

    print("GET MISSING SUBJECTS")
    print(await km_audit.get_missing_subjects(20, 0))

    # MANAGE INSTANCE
    print("GET GLOBAL HEALTH:")
    print(await manage_instance.get_global_health())

    print("GET VERSION:")
    print(await manage_instance.version())

    print("API IS ALIVE:")
    print(await manage_instance.is_api_alive())

    # SEARCH
    print("SEARCH QUERY:")
    # query: 'query to search on the semantic index',
    # user: '(optional) user identifier to log for this query',
    # impersonate: 'name a profile to imitate the style of answer. eg: Knowledge manager or Sales man',
    # multiDocuments: 'true if you want to search across multiple documents, false if you want to retrieve an answer following only one document',
    # needFollowingQuestions: 'true if you want to the API purpose multiple next questions, else false'
    print(await search.query("what is the history of France TV?", "userid", "", False, False))

    print("GET DOC SIGNATURE:")
    print(await search.get_doc_signature("document_id"))
    
    print("GET DOCS BY IDS:")
    print(await search.get_doc_ids(["document_id1","document_id2"]))

    print("GET LIST SEARCH:")
    print(await search.get_list_search(0, 10))

    print("COUNT DONE REQUESTS:")
    print(await search.count_done_requests())

    print("COUNT ANSWERED DONE REQUESTS:")
    print(await search.count_answered_done_requests())

    print("GET BACK REQUESTS MADE TO THE API")
    print(await search.get_requests_to_api(10, 0))

    print("IDENTIFY SPECIFIC DOCUMENT:")
    # input: an array on a conversation of the user and the assistant, each row of the array follow the structure { from: 'user' | 'assistant', message: string }
    print(await search.identify_specific_document([{"user":"user message", "assistant": "assistant message"}]))

    # SEMANTIC GRAPH
    print("GET NODES:")
    print(await semantic_graph.get_nodes(10, 0))

    print("GET LINKED NODES:")
    print(await semantic_graph.get_linked_nodes("node_id"))

    print("GET NODE BY LABEL:")
    print(await semantic_graph.get_node_by_label("node_label"))

    print("DETECT APPROXIMAL NODES:")
    print(await semantic_graph.detect_approximal_nodes("query"))



async def async_mode():
    tasks = [
        core.count_documents(),
        core.count_indexable_documents(),
        core.count_indexed_documents(),
        core.count_detected_documents()
    ]
    result_list = await asyncio.gather(*tasks, return_exceptions=False)
    print(result_list)


if __name__ == "__main__":
    asyncio.run(async_mode())

    asyncio.run(sync_mode())
