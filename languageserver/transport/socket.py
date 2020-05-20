import asyncio
from typing import AsyncGenerator, Type, TypeVar

T = TypeVar("T", bound="SocketTransport")


class SocketTransport:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter

    def __init__(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        self.reader = reader
        self.writer = writer

    @classmethod
    async def open(cls: Type[T], port: int) -> T:
        reader, writer = await asyncio.open_connection("127.0.0.1", port)
        return cls(reader, writer)

    async def listen(self) -> AsyncGenerator[bytes, None]:
        while True:
            data = await self.reader.read()
            yield data

    def write(self, data: bytes) -> None:
        self.writer.write(data)
