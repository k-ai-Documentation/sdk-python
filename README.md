# sdk-python

## Introduction
SDK python enables developers to efficiently manage files, instance, perform searches, handle thematic content, and conduct audits. This toolkit is designed to streamline the integration of complex functionalities into python-based projects.

## Installation
To integrate the SDK into your project, include the SDK files in your project directory. 

## Quick start
There are two type of versions: SaaS version and Premise version.

#### SaaS version

SaaS version means you are using the service provided by Kai with cloud service. In this case, you will need 3 keys (organizationId, instanceId, apiKey) to initialize kaiStudio.

Here's a simple example to get you started with the SDK:

```
from index import KaiStudio
from index import KaiStudioCredentials

credentials = KaiStudioCredentials({organizationId="your organization id",
                                   instanceId="your instance id",
                                   apiKey="your api key"})
search = KaiStudio(credentials).search()
print("SEARCH QUERY:")
print(await search.query("what is the history of France TV?", "userid"))

```
#### Premise version

Premise version means you are using the service in your local server in your enterprise. In this case, you will need host and api key (optional) to initialize kaiStudio.

Here's a simple example to get you started with the SDK:

```
from index import KaiStudio
from index import KaiStudioCredentials

//apiKey is optionnal
credentials = KaiStudioCredentials({host="your server host", apiKey="your api key"})
search = KaiStudio(credentials).search()
print("SEARCH QUERY:")
print(await search.query("what is the history of France TV?", "userid"))

```

## Usage Guide
### Core
[Core.py](modules/Core.py) provides methods for core functionalities.
- count_documents
- count_indexable_documents
- count_indexed_documents
- count_detected_documents
- download_file
- differential_indexation
- get_scenarios
- get_logs
- reinit_all

For example:
```py
core = KaiStudio(credentials).core()
print("COUNT DOCUMENTS")
print(await core.count_documents())
```

### Auditing
[KMAudit.py](modules/KMAudit.py) provides methods for auditing.
- get_all_tasks_linked_to_a_document
- get_conflict_information
- get_duplicated_information
- set_conflict_managed
- set_duplicated_information_managed
- get_documents_to_manage
- get_missing_subjects

For example:
```py
km_audit = KaiStudio(credentials).km_audit()
print(await km_audit.get_conflict_information(20, 0))
```

### ManageInstance
[ManageInstance.py](modules/ManageInstance.py) provides methods for managing instance.
- get_global_health
- is_api_alive
- version

For example:
```py
manage_instance = KaiStudio(credentials).manage_instance()
print("GET GLOBAL HEALTH:")
print(await manage_instance.get_global_health())
```

### SemanticGraph
[SemanticGraph.py](modules/SemanticGraph.py) provides methods for managing semantic graph.
- get_nodes
- get_linked_nodes
- get_node_by_label
- detect_approximal_nodes

For example:
```py
semantic_graph = KaiStudio(credentials).semantic_graph()
print(semantic_graph.getNodes(10,0))
```

### Search
[Search.py](modules/Search.py) provides methods for searching.
- query
- get_doc_signature
- get_doc_ids
- get_list_search
- count_done_requests
- count_answered_done_requests
- get_requests_to_api
- identify_specific_document

```py
search = KaiStudio(credentials).search()
print("RELATED FILES")
print(await search.get_list_search(0, 10))
```


<u>**For more examples, you can check the [example.py](example.py) file.**</u>

## Contributing
bxu@k-ai.ai

rmei@k-ai.ai

sngo@k-ai.ai

