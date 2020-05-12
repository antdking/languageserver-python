from enum import Enum


class DiagnosticSeverity(int, Enum):
    Error = 1
    Warning = 2
    Information = 3
    Hint = 4


class DiagnosticTag(int, Enum):
    Unnecessary = 1
    Deprecated = 2


class MarkupKind(str, Enum):
    PlainText = "plaintext"
    Markdown = "markdown"


class CompletionTriggerKind(int, Enum):
    Invoked = 1
    TriggerCharacter = 2
    TriggerForIncompleteCompletions = 3


class Trace(str, Enum):
    Off = "off"
    Messages = "messages"
    Verbose = "verbose"


class MessageType(int, Enum):
    Error = 1
    Warning = 2
    Info = 3
    Log = 4


class FileChangeType(int, Enum):
    Created = 1
    Changed = 2
    Deleted = 3


class SymbolKind(int, Enum):
    File = 1
    Module = 2
    Namespace = 3
    Package = 4
    Class = 5
    Method = 6
    Property = 7
    Field = 8
    Constructor = 9
    Enum = 10
    Interface = 11
    Function = 12
    Variable = 13
    Constant = 14
    String = 15
    Number = 16
    Boolean = 17
    Array = 18
    Object = 19
    Key = 20
    Null = 21
    EnumMember = 22
    Struct = 23
    Event = 24
    Operator = 25
    TypeParameter = 26


class InsertTextFormat(int, Enum):
    PlainText = 1
    Snippet = 2


class CompletionItemTag(int, Enum):
    Deprecated = 1


class CompletionItemKind(int, Enum):
    Text = 1
    Method = 2
    Function = 3
    Constructor = 4
    Field = 5
    Variable = 6
    Class = 7
    Interface = 8
    Module = 9
    Property = 10
    Unit = 11
    Value = 12
    Enum = 13
    Keyword = 14
    Snippet = 15
    Color = 16
    File = 17
    Reference = 18
    Folder = 19
    EnumMember = 20
    Constant = 21
    Struct = 22
    Event = 23
    Operator = 24
    TypeParameter = 25
