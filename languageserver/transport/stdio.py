import asyncio
import sys
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
    async def open(cls) -> "PipeTransport":
        loop = asyncio.get_event_loop()

        reader = asyncio.StreamReader()
        reader_protocol = asyncio.StreamReaderProtocol(reader)

        reader_transport, _ = await loop.connect_read_pipe(
            lambda: reader_protocol, sys.stdin
        )

        write_transport, write_protocol = await loop.connect_write_pipe(
            asyncio.Protocol, sys.stdout
        )
        writer = asyncio.StreamWriter(write_transport, write_protocol, None, loop)

        return cls(reader, writer)

    async def listen(self) -> AsyncGenerator[bytes, None]:
        while True:
            data = await self.reader.read()
            yield data

    def write(self, data: bytes) -> None:
        self.writer.write(data)
