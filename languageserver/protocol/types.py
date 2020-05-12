from typing import Any, Dict, List, Union

from typing_extensions import Literal, TypedDict

from .flags import (
    CompletionItemKind,
    CompletionItemTag,
    CompletionTriggerKind,
    DiagnosticSeverity,
    DiagnosticTag,
    FileChangeType,
    InsertTextFormat,
    MarkupKind,
    SymbolKind,
)

DocumentUri = str
DocumentSelector = List["DocumentFilter"]

ProgressToken = Union[int, str]


class Position(TypedDict):
    """
    Position in a text document expressed as zero-based line and zero-based character offset.
    A position is between two characters like an 'insert' cursor in a editor.
    Special values like for example -1 to denote the end of a line are not supported.
    """

    line: int
    character: int


class Range(TypedDict):
    """
    A range in a text document expressed as (zero-based) start and end positions. A range is comparable to a selection in an editor. Therefore the end position is exclusive. If you want to specify a range that contains a line including the line ending character(s) then use an end position denoting the start of the next line. For example:
    """

    start: Position
    end: Position


class Location(TypedDict):
    """
    Represents a location inside a resource, such as a line inside a text file.
    """

    uri: DocumentUri
    range: Range


class _LocationLink__Optional(TypedDict, total=False):
    originSelectionRange: Range


class LocationLink(_LocationLink__Optional):
    """
    Represents a link between a source and a target location.
    """

    targetUri: DocumentUri
    targetRange: Range
    targetSelectionRange: Range


class DiagnosticRelatedInformation(TypedDict):
    location: Location
    message: str


class _Diagnostic__Optional(TypedDict, total=False):
    severity: DiagnosticSeverity
    code: Union[int, str]
    source: str
    tags: List[DiagnosticTag]
    relatedInformation: List[DiagnosticRelatedInformation]


class Diagnostic(_Diagnostic__Optional):
    """
    Represents a diagnostic, such as a compiler error or warning. Diagnostic objects are only valid in the scope of a resource.
    """

    range: Range
    message: str


class _Command__Optional(TypedDict, total=False):
    arguments: List[Any]


class Command(TypedDict):
    """
    Represents a reference to a command.
    Provides a title which will be used to represent a command in the UI.
    Commands are identified by a string identifier.
    The recommended way to handle commands is to implement their execution
    on the server side if the client and server provides the corresponding
    capabilities.
    Alternatively the tool extension code could handle the command.
    The protocol currently doesn't specify a set of well-known commands.
    """

    title: str
    command: str


"""
The above is equivalent to:
```ts
interface Command {
    title: string;
    command: string;
    arguments?: any[];
}
```
"""


class TextEdit(TypedDict):
    range: Range
    newText: str


class TextDocumentEdit(TypedDict):
    textDocument: "VersionedTextDocumentIdentifier"
    edits: List[TextEdit]


class _CreateFileOptions__Optional(TypedDict, total=False):
    overwrite: bool
    ignoreIfExists: bool


class CreateFileOptions(_CreateFileOptions__Optional):
    pass


class _CreateFile__Optional(TypedDict, total=False):
    options: CreateFileOptions


class CreateFile(_CreateFile__Optional):
    kind: Literal["create"]
    uri: DocumentUri


class _RenameFileOptions__Optional(TypedDict, total=False):
    overwrite: bool
    ignoreIfExists: bool


class RenameFileOptions(_RenameFileOptions__Optional):
    pass


class _RenameFile__Optional(TypedDict, total=False):
    options: RenameFileOptions


class RenameFile(_RenameFile__Optional):
    kind: Literal["rename"]
    oldUri: DocumentUri
    newUri: DocumentUri


class _DeleteFileOptions__Optional(TypedDict, total=False):
    overwrite: bool
    ignoreIfExists: bool


class DeleteFileOptions(_DeleteFileOptions__Optional):
    pass


class _DeleteFile__Optional(TypedDict, total=False):
    options: DeleteFileOptions


class DeleteFile(_DeleteFile__Optional):
    kind: Literal["delete"]
    uri: DocumentUri


class _WorkspaceEdit__Optional(TypedDict, total=False):
    changes: Dict[DocumentUri, List[TextEdit]]

    # This is dependent on the client capabilities.
    # the field should not exist if `workspace.workspaceEdit.documentChanges` is falsy
    # Create/Rename/Delete are supported if declared in `workspace.workspaceEdit.resourceOperations`.
    documentChanges: Union[
        List[TextDocumentEdit],
        List[Union[TextDocumentEdit, CreateFile, RenameFile, DeleteFile]],
    ]


class WorkspaceEdit(_WorkspaceEdit__Optional):
    pass


class TextDocumentIdentifier(TypedDict):
    uri: DocumentUri


class TextDocumentItem(TypedDict):
    uri: DocumentUri
    languageId: str
    version: int
    text: str


class VersionedTextDocumentIdentifier(TextDocumentIdentifier):
    version: Union[int, None]


class TextDocumentPositionParams(TypedDict):
    textDocument: TextDocumentIdentifier
    position: Position


class _DocumentFilter__Optional(TypedDict, total=False):
    language: str
    scheme: str  # usually `file` or `untitled`
    pattern: str  # glob pattern


class DocumentFilter(_DocumentFilter__Optional):
    pass


class _StaticRegistrationOptions__Optional(TypedDict, total=False):
    """
    Static registration options can be used to register a feature in the initialize result with a given server control ID to be able to un-register the feature later on.
    """

    id: str


class StaticRegistrationOptions(_StaticRegistrationOptions__Optional):
    pass


class TextDocumentRegistrationOptions(TypedDict):
    documentSelector: Union[DocumentSelector, None]


class MarkupContent(TypedDict):
    kind: MarkupKind
    value: str


class _WorkDoneProgressBegin__Optional(TypedDict, total=False):
    cancellable: bool
    message: str
    percentage: int


class WorkDoneProgressBegin(_WorkDoneProgressBegin__Optional):
    kind: Literal["begin"]
    title: str


class _WorkDoneProgressReport__Optional(TypedDict, total=False):
    cancellable: bool
    message: str
    percentage: int


class WorkDoneProgressReport(_WorkDoneProgressReport__Optional):
    kind: Literal["report"]


class _WorkDoneProgressEnd__Optional(TypedDict, total=False):
    message: str


class WorkDoneProgressEnd(_WorkDoneProgressEnd__Optional):
    kind: Literal["end"]


class _WorkDoneProgressOptions__Optional(TypedDict, total=False):
    workDoneProgress: bool


class WorkDoneProgressOptions(_WorkDoneProgressOptions__Optional):
    """
    Options to signal work done progress support in server capabilities.
    """


class _PartialResultParams__Optional(TypedDict, total=False):
    partialResultToken: ProgressToken


class PartialResultParams(_PartialResultParams__Optional):
    """A parameter literal used to pass a partial result token."""


class ClientCapabilities(TypedDict):
    # this is a big one, too lazy to define it right now
    pass


class ServerCapabilities(TypedDict):
    # this is a big one, too lazy to define it right now
    pass


class MessageActionItem(TypedDict):
    title: str


class WorkspaceFolder(TypedDict):
    uri: DocumentUri
    name: str


class _Registration__Optional(TypedDict, total=False):
    registerOptions: Any


class Registration(_Registration__Optional):
    id: str
    method: str


class Unregistration(TypedDict):
    id: str
    method: str


class WorkspaceFoldersChangeEvent(TypedDict):
    added: List[WorkspaceFolder]
    removed: List[WorkspaceFolder]


class _ConfigurationItem__Optional(TypedDict, total=False):
    scopeUri: DocumentUri
    section: str


class ConfigurationItem(_ConfigurationItem__Optional):
    pass


class FileEvent(TypedDict):
    type: FileChangeType
    uri: DocumentUri


class _SymbolInformation__Optional(TypedDict, total=False):
    deprecated: bool
    containerName: str


class SymbolInformation(_SymbolInformation__Optional):
    name: str
    kind: SymbolKind
    location: Location


class _CompletionContext__Optional(TypedDict, total=False):
    triggerCharacter: str


class CompletionContext(_CompletionContext__Optional):
    triggerKind: CompletionTriggerKind


class _CompletionItem__Optional(TypedDict, total=False):
    kind: CompletionItemKind
    tags: List[CompletionItemTag]
    detail: str
    documentation: Union[str, MarkupContent]
    deprecated: bool
    preselect: bool
    sortText: str
    filterText: str
    insertText: str
    insertTextFormat: InsertTextFormat
    additionalTextEdits: List[TextEdit]
    commitCharacters: List[str]
    command: Command
    data: Any


class CompletionItem(_CompletionItem__Optional):
    label: str
    textEdit: TextEdit


class CompletionList(TypedDict):
    isIncomplete: bool
    items: List[CompletionItem]


class _Hover__Optional(TypedDict, total=False):
    range: Range


class _MarkedString(TypedDict):
    language: str
    value: str


MarkedString = Union[str, _MarkedString]


class Hover(_Hover__Optional):
    contents: Union[MarkedString, List[MarkedString], MarkupContent]
