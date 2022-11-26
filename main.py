import asyncio

from aio_pika import connect_robust
from aio_pika.patterns import RPC
from objection_engine import render_comment_list
import os


async def main() -> None:
    connection = await connect_robust(
        f"amqp://{os.getenv('OE_RABBIT_CONNECTION', 'guest:guest@127.0.0.1')}/",
        client_properties={"connection_name": "callee"},
    )

    # Creating channel
    channel = await connection.channel()

    rpc = await RPC.create(channel)
    await rpc.register("render", render_comment_list)

    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())