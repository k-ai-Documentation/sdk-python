# sdk-python

## Introduction
SDK python enables developers to efficiently manage files, instance, perform searches, handle thematic content, and conduct audits. This toolkit is designed to streamline the integration of complex functionalities into python-based projects.

## Installation
To integrate the SDK into your project, include the SDK files in your project directory. 

## Quick start
Here's a simple example to get you started with the SDK. This example demonstrates how to instantiate a new search and perform basic operations:
```
from index import KaiStudio
from index import KaiStudioCredentials

credentials = KaiStudioCredentials(organizationId="your organization id",
                                   instanceId="your instance id",
                                   apiKey="your api key")
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
[ManageInstance.ts](modules/ManageInstance.ts) provides methods for managing instance.
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
[Thematic.ts](modules/Thematic.ts) provides methods for managing thematic content.
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
[SemanticGraph.ts](modules/SemanticGraph.ts) provides methods for managing semantic graph.
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
[Search.ts](modules/Search.ts) provides methods for searching.
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

