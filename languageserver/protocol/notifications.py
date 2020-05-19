from typing import Any, ClassVar, Generic, TypeVar

from .params import (
    DidChangeConfigurationParams,
    DidChangeWatchedFilesParams,
    DidChangeWorkspaceFoldersParams,
    ExitParams,
    InitializedParams,
    LogMessageParams,
    ShowMessageParams,
    WorkDoneProgressCancelParams,
)

T_Params = TypeVar("T_Params")
TODO = Any


class Notification(Generic[T_Params]):
    method: ClassVar[str]

    params: T_Params


class Initialized(Notification[InitializedParams]):
    method = "initialized"


class Exit(Notification[ExitParams]):
    method = "exit"


class ShowMessage(Notification[ShowMessageParams]):
    method = "window/showMessage"


class LogMessage(Notification[LogMessageParams]):
    method = "window/logMessage"


class WorkDoneProgressCancel(Notification[WorkDoneProgressCancelParams]):
    method = "window/workDoneProgress/cancel"


class TelemetryEvent(Notification[Any]):
    method = "telemetry/event"


class DidChangeWorkspaceFolders(Notification[DidChangeWorkspaceFoldersParams]):
    method = "workspace/didChangeWorkspaceFolders"


class DidChangeConfiguration(Notification[DidChangeConfigurationParams]):
    method = "workspace/didChangeConfiguration"


class DidChangeWatchedFiles(Notification[DidChangeWatchedFilesParams]):
    method = "workspace/didChangeWatchedFiles"


class DidOpenTextDocument(Notification[TODO]):
    method = "textDocument/didOpen"


class DidChangeTextDocument(Notification[TODO]):
    method = "textDocument/didChange"


class WillSaveTextDocument(Notification[TODO]):
    method = "textDocument/willSave"


class DidSaveTextDocument(Notification[TODO]):
    method = "textDocument/didSave"


class DidCloseTextDocument(Notification[TODO]):
    method = "textDocument/didClose"


class PublishDiagnostics(Notification[TODO]):
    method = "textDocument/publishDiagnostics"
