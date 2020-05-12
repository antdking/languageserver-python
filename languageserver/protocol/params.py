from typing import Any, Dict, List, Union

from typing_extensions import TypedDict

from .flags import MessageType, Trace
from .types import (
    ClientCapabilities,
    CompletionContext,
    CompletionItem,
    ConfigurationItem,
    DocumentUri,
    FileEvent,
    MessageActionItem,
    Position,
    ProgressToken,
    Registration,
    TextDocumentIdentifier,
    Unregistration,
    WorkspaceEdit,
    WorkspaceFolder,
    WorkspaceFoldersChangeEvent,
)


class WorkDoneProgressParams(TypedDict, total=False):
    workDoneToken: ProgressToken


class PartialResultParams(TypedDict, total=False):
    partialResultToken: ProgressToken


class _InitializeParams__Optional(WorkDoneProgressParams, total=False):
    clientInfo: Dict[str, Any]  # lazy
    rootPath: Union[str, None]
    initializationOptions: Any
    trace: Trace
    workspaceFolders: Union[List[WorkspaceFolder], None]


class InitializeParams(_InitializeParams__Optional):
    processId: Union[int, None]
    rootUri: Union[DocumentUri, None]
    capabilities: ClientCapabilities


class InitializedParams(TypedDict):
    pass


class ShutdownParams(TypedDict):
    pass  # This might actually be null..


class ExitParams(TypedDict):
    pass  # This might actually be null..


class ShowMessageParams(TypedDict):
    type: MessageType
    message: str


class _ShowMessageRequestParams__Optional(TypedDict, total=False):
    actions: List[MessageActionItem]


class ShowMessageRequestParams(_ShowMessageRequestParams__Optional):
    type: MessageType
    message: str


class LogMessageParams(TypedDict):
    type: MessageType
    message: str


class WorkDoneProgressCreateParams(TypedDict):
    token: ProgressToken


class WorkDoneProgressCancelParams(TypedDict):
    token: ProgressToken


class RegistrationParams(TypedDict):
    registrations: List[Registration]


class UnregistrationParams(TypedDict):
    # purposeful typo!
    unregisterations: List[Unregistration]


WorkspaceFoldersParams = Union[None]


class DidChangeWorkspaceFoldersParams(TypedDict):
    event: WorkspaceFoldersChangeEvent


class DidChangeConfigurationParams(TypedDict):
    settings: Any


class ConfigurationParams(TypedDict):
    items: List[ConfigurationItem]


class DidChangeWatchedFilesParams(TypedDict):
    changes: List[FileEvent]


class WorkspaceSymbolParams(WorkDoneProgressParams, PartialResultParams):
    query: str


class _ExecuteCommandParams__Optional(WorkDoneProgressParams, total=False):
    arguments: List[Any]


class ExecuteCommandParams(_ExecuteCommandParams__Optional):
    command: str


class _ApplyWorkspaceEditParams__Optional(TypedDict, total=False):
    label: str


class ApplyWorkspaceEditParams(_ApplyWorkspaceEditParams__Optional):
    edit: WorkspaceEdit


class TextDocumentPositionParams(TypedDict):
    textDocument: TextDocumentIdentifier
    position: Position


class CompletionParams(
    TextDocumentPositionParams, WorkDoneProgressParams, PartialResultParams, total=False
):
    context: CompletionContext


CompletionItemResolveParams = CompletionItem


class HoverParams(TextDocumentPositionParams, WorkDoneProgressParams):
    pass
