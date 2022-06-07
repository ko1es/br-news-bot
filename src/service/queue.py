from settings import CONFIG
from aio_pika import Message, connect


async def recieve_message_from_queue() -> None:

    connection = await connect(CONFIG.rabbitmq.get_connection_url())

    async with connection:
        # Creating a channel
        channel = await connection.channel()

        # Declaring queue
        queue = await channel.declare_queue(CONFIG.rabbitmq.default_queue_name)

        # Start listening the queue with name 'hello'
        await queue.consume(on_message, no_ack=True)

        print(" [*] Waiting for messages. To exit press CTRL+C")
        await asyncio.Future()
