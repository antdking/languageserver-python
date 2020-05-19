from typing import TYPE_CHECKING, Optional, Type

from .registry import Registry

if TYPE_CHECKING:
    from .registry import T_Arg, T_Ret, MakesAsync, RegisterTarget
    from languageserver.protocol.requests import Request
    from languageserver.protocol.notifications import Notification


class Server:
    registry: Registry

    def __init__(self, registry: Optional[Registry] = None):
        self.registry = registry or Registry()

    def on(
        self, request_type: "Type[RegisterTarget[T_Arg, T_Ret]]",
    ) -> "MakesAsync[T_Arg, T_Ret]":
        return self.registry.register(request_type)

    async def send_request(self, request: "Request[T_Arg, T_Ret]") -> T_Ret:
        pass

    async def send_notification(self, notification: "Notification[T_Arg]") -> None:
        pass
