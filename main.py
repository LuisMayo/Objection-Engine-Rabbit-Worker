import asyncio

from aio_pika import connect_robust
from aio_pika.patterns import RPC
from objection_engine import render_comment_list
import os
import tempfile

tmpdir = tempfile.mkdtemp()
def render_internal(output_filename: str, **kwargs):
    final_file = tmpdir + '/' + output_filename
    render_comment_list(output_filename=final_file, **kwargs)
    return final_file


async def main() -> None:
    connection = await connect_robust(
        f"amqp://{os.getenv('OE_RABBIT_CONNECTION', 'guest:guest@127.0.0.1')}/",
        client_properties={"connection_name": "callee"},
    )

    # Creating channel
    channel = await connection.channel()

    rpc = await RPC.create(channel)
    await rpc.register("oe_render", render_internal)

    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(main())