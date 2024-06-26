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
### File Management
[FileInstance.py](modules/FileInstance.py) provides methods for file management.
- listFiles
- downloadFile
- uploadFiles
- removeFile

For example:
```py
file_instance = KaiStudio(credentials).file_instance()
print("UPLOAD FILE:")
files = {"files": open("files/kai-studio v1.1.pdf", "rb")}
print(await file_instance.upload_files(files))
```

### Auditing
[KMAudit.py](modules/KMAudit.py) provides methods for auditing.
- getConflictInformation
- getDuplicatedInformation
- setConflictManaged
- setDuplicatedInformationManaged

For example:
```py
km_audit = KaiStudio(credentials).km_audit()
print(await km_audit.getConflictInformation(1O,0))
```
### ManageInstance
[ManageInstance.py](modules/ManageInstance.py) provides methods for managing instance.
- getGlobalHealth
- isApiAlive
- generateNewApiKey
- updateName
- deploy
- delete
- addKb
- setPlayground
- updateKb
- removeKb

For example:
```py
manage_instance = KaiStudio(credentials).manage_instance()
print("GET GLOBAL HEALTH:")
print(await manage_instance.get_global_health())
```

### Thematic
[Thematic.py](modules/Thematic.py) provides methods for managing thematic content.
- getTopic
- getKbs
- getDocuments
- addAuditQuestion
- updateAuditQuestion
- listAuditQuestions
- getTestRunningState
- runTest
- listTopics
- getSubtopic
- countTopics
- countSubtopics
- countDocuments
- countAuditQuestions
- countValidatedAuditQuestions

For example:
```py
thematic = KaiStudio(credentials).thematic()
print("GET DOCUMENTS")
print(await thematic.get_documents())
```

### SemanticGraph
[SemanticGraph.py](modules/SemanticGraph.py) provides methods for managing semantic graph.
- getNodes
- getLinkedNodes
- getNodeByLabel
- detectApproximalNodes

For example:
```py
semantic_graph = KaiStudio(credentials).semantic_graph()
print(semantic_graph.getNodes(10,0))
```

### Search
[Search.py](modules/Search.py) provides methods for searching.
- search
- getRelatedDocuments
- countAnalyzedDocuments
- getDocSignature
- getDocsIds
- countDoneRequests
- countAnsweredDoneRequests
- generateFollowingQuestion
- listQuestionsAsked
```py
search = KaiStudio(credentials).search()
print("RELATED FILES")
print(await search.get_related_documents("France TV"))
```


<u>**For more examples, you can check the [example.py](example.py) file.**</u>

## Contributing
bxu@k-ai.ai

rmei@k-ai.ai

sngo@k-ai.ai

