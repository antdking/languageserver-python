from typing import Any, Dict, List, Union

from typing_extensions import TypedDict

from .types import (
    CompletionItem,
    CompletionList,
    Hover,
    MessageActionItem,
    ServerCapabilities,
    SymbolInformation,
    WorkspaceFolder,
)


class _InitializeResult__Optional(TypedDict, total=False):
    serverInfo: Dict[str, Any]  # lazy


class InitializeResult(_InitializeResult__Optional):
    capabilities: ServerCapabilities


ShutdownResult = Union[None]


ShowMessageResult = Union[MessageActionItem, None]


class WorkDoneProgressCreateResult(TypedDict):
    pass  # this might be null


WorkSpaceFoldersResult = Union[List[WorkspaceFolder], None]


WorkspaceSymbolResult = Union[List[SymbolInformation], None]


ExecuteCommandResult = Union[Any, None]


class _ApplyWorkspaceEditResult__Optional(TypedDict, total=False):
    failureReason: str


class ApplyWorkspaceEditResult(_ApplyWorkspaceEditResult__Optional):
    applied: bool


CompletionResult = Union[List[CompletionItem], CompletionList, None]
CompletionItemResolveResult = CompletionItem

HoverResult = Union[Hover, None]

RegisterCapabilityResult = Union[None]
UnRegisterCapabilityResult = Union[None]
ConfigurationResult = List[Any]
