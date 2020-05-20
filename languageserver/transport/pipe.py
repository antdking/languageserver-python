import asyncio
from typing import AsyncGenerator


class PipeTransport:
    reader: asyncio.StreamReader
    writer: asyncio.StreamWriter

    def __init__(
        self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter
    ) -> None:
        self.reader = reader
        self.writer = writer

    @classmethod
    async def open(cls, pipe_name: str) -> "PipeTransport":
        # Only supports unix sockets for now. add support for Windows later.

        reader, writer = await asyncio.open_unix_connection(pipe_name)
        return cls(reader, writer)

    async def listen(self) -> AsyncGenerator[bytes, None]:
        while True:
            data = await self.reader.read()
            yield data

    def write(self, data: bytes) -> None:
        self.writer.write(data)
