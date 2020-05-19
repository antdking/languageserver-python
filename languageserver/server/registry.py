from functools import wraps
from inspect import iscoroutinefunction
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Callable,
    Dict,
    Type,
    TypeVar,
    Union,
    cast,
)

if TYPE_CHECKING:
    from languageserver.protocol.requests import Request
    from languageserver.protocol.notifications import Notification


T_Arg = TypeVar("T_Arg")
T_Ret = TypeVar("T_Ret")


RegisterableFunc = Callable[[T_Arg], T_Ret]
RegisterableAsync = Callable[[T_Arg], Awaitable[T_Ret]]

Registerable = Union[
    RegisterableFunc[T_Arg, T_Ret], RegisterableAsync[T_Arg, T_Ret],
]


class MethodNotFound(Exception):
    pass


def _ensure_async(func: Registerable[T_Arg, T_Ret]) -> RegisterableAsync[T_Arg, T_Ret]:
    if iscoroutinefunction(func):
        return cast(RegisterableAsync[T_Arg, T_Ret], func)

    @wraps(func)
    async def inner(message: T_Arg) -> T_Ret:
        f = cast(RegisterableFunc[T_Arg, T_Ret], func)
        return f(message)

    return inner


MakesAsync = Callable[[Registerable[T_Arg, T_Ret]], RegisterableAsync[T_Arg, T_Ret]]

RegisterTarget = Union[
    "Request[T_Arg, T_Ret]", "Notification[T_Arg]",
]

T_Store = Dict[Type[RegisterTarget[T_Arg, T_Ret]], RegisterableAsync[T_Arg, T_Ret]]


class Registry:
    _registered: T_Store[Any, Any]

    def __init__(self) -> None:
        self._registered = {}

    def register(
        self, request_type: "Type[RegisterTarget[T_Arg, T_Ret]]",
    ) -> MakesAsync[T_Arg, T_Ret]:
        def inner(func: Registerable[T_Arg, T_Ret]) -> RegisterableAsync[T_Arg, T_Ret]:
            f = _ensure_async(func)
            store = cast(T_Store[T_Arg, T_Ret], self._registered)
            store[request_type] = f
            return f

        return inner

    async def dispatch(self, request: "RegisterTarget[T_Arg, T_Ret]") -> T_Ret:
        request_type = type(request)
        store = cast(T_Store[T_Arg, T_Ret], self._registered)
        try:
            func = store[request_type]
        except KeyError:
            raise MethodNotFound

        return await func(request.params)
