from modules.Search import Search
from modules.FileInstance import FileInstance
from modules.ManageInstance import ManageInstance
from modules.KaiStudioCredentials import KaiStudioCredentials
from modules.AuditInstance import AuditInstance


class KaiStudio:
    __credentials: KaiStudioCredentials
    __search: Search
    __fileInstance: FileInstance
    __manageInstance: ManageInstance

    def __init__(self, credentials: KaiStudioCredentials):
        self.__credentials = credentials
        self.__search = Search(self.__credentials)
        self.__fileInstance = FileInstance(self.__credentials)
        self.__manageInstance = ManageInstance(self.__credentials)
        self.__auditInstance = AuditInstance(self.__credentials)

    def get_credentials(self) -> KaiStudioCredentials:
        return self.__credentials

    def search(self) -> Search:
        return self.__search

    def file_instance(self) -> FileInstance:
        return self.__fileInstance

    def manage_instance(self) -> ManageInstance:
        return self.__manageInstance

    def audit_instance(self) -> AuditInstance:
        return self.__auditInstance
