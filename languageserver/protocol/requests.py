from typing import Any, ClassVar, Generic, TypeVar

from .params import (
    ApplyWorkspaceEditParams,
    CompletionItemResolveParams,
    CompletionParams,
    ConfigurationParams,
    ExecuteCommandParams,
    HoverParams,
    InitializeParams,
    RegistrationParams,
    ShowMessageRequestParams,
    ShutdownParams,
    UnregistrationParams,
    WorkDoneProgressCreateParams,
    WorkspaceFoldersParams,
    WorkspaceSymbolParams,
)
from .results import (
    ApplyWorkspaceEditResult,
    CompletionItemResolveResult,
    CompletionResult,
    ConfigurationResult,
    ExecuteCommandResult,
    HoverResult,
    InitializeResult,
    RegisterCapabilityResult,
    ShowMessageResult,
    ShutdownResult,
    UnRegisterCapabilityResult,
    WorkDoneProgressCreateResult,
    WorkSpaceFoldersResult,
    WorkspaceSymbolResult,
)

T_Params = TypeVar("T_Params")
T_Result = TypeVar("T_Result")
TODO = Any


class Request(Generic[T_Params, T_Result]):
    method: ClassVar[str]

    params: T_Params


class Initialize(Request[InitializeParams, InitializeResult]):
    method = "initialize"


class Shutdown(Request[ShutdownParams, ShutdownResult]):
    method = "shutdown"


class ShowMessage(Request[ShowMessageRequestParams, ShowMessageResult]):
    method = "window/showMessageRequest"


class WorkDoneProgressCreate(
    Request[WorkDoneProgressCreateParams, WorkDoneProgressCreateResult]
):
    method = "window/workDoneProgress/create"


class RegisterCapability(Request[RegistrationParams, RegisterCapabilityResult]):
    method = "client/registerCapability"


class UnRegisterCapability(Request[UnregistrationParams, UnRegisterCapabilityResult]):
    method = "client/unregisterCapability"


class WorkspaceFolders(Request[WorkspaceFoldersParams, WorkSpaceFoldersResult]):
    method = "workspace/workspaceFolders"


class Configuration(Request[ConfigurationParams, ConfigurationResult]):
    method = "workspace/configuration"


class WorkspaceSymbol(Request[WorkspaceSymbolParams, WorkspaceSymbolResult]):
    method = "workspace/symbol"


class ExecuteCommand(Request[ExecuteCommandParams, ExecuteCommandResult]):
    method = "workspace/executeCommand"


class ApplyWorkspaceEdit(Request[ApplyWorkspaceEditParams, ApplyWorkspaceEditResult]):
    method = "workspace/applyEdit"


class WillSaveTextDocument(Request[TODO, TODO]):
    method = "textDocument/willSaveWaitUntil"


class Completion(Request[CompletionParams, CompletionResult]):
    method = "textDocument/completion"


class CompletionItemResolve(
    Request[CompletionItemResolveParams, CompletionItemResolveResult]
):
    method = "completionItem/resolve"


class Hover(Request[HoverParams, HoverResult]):
    method = "textDocument/hover"
