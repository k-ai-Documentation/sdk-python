from modules.KMAduit import KMAudit
from modules.KaiStudioCredentials import KaiStudioCredentials
from modules.ManageInstance import ManageInstance
from modules.Search import Search
from modules.SemanticGraph import SemanticGraph
from modules.Core import Core


class KaiStudio:
    __credentials: KaiStudioCredentials
    __search: Search
    __manageInstance: ManageInstance
    __km_audit: KMAudit
    __semantic_graph: SemanticGraph
    __core: Core

    def __init__(self, credentials: KaiStudioCredentials):
        self.__credentials = credentials

        if self.__credentials.organizationId and self.__credentials.instanceId and self.__credentials.apiKey:
            headers = {
                'organization-id': self.__credentials.organizationId,
                'instance-id': self.__credentials.instanceId,
                'api-key': self.__credentials.apiKey
            }

            base_url = f"https://{self.__credentials.organizationId}.kai-studio.ai/{self.__credentials.instanceId}/"

            if self.__credentials.host:
                base_url = self.__credentials.host
                if self.__credentials.apiKey:
                    headers = {
                        'api-key': self.__credentials.apiKey
                    }
            self.__core = Core(headers, base_url)
            self.__search = Search(headers, base_url)
            self.__manageInstance = ManageInstance(headers, base_url)
            self.__km_audit = KMAudit(headers, base_url)
            self.__semantic_graph = SemanticGraph(headers, base_url)

    def get_credentials(self) -> KaiStudioCredentials:
        return self.__credentials

    def search(self) -> Search:
        return self.__search

    def manage_instance(self) -> ManageInstance:
        return self.__manageInstance

    def km_audit(self) -> KMAudit:
        return self.__km_audit

    def semantic_graph(self) -> SemanticGraph:
        return self.__semantic_graph

    def core(self) -> Core:
        return self.__core
