import chainlit as cl


@cl.on_message
async def main(message: str):
    # Your custom logic goes here...

    # Send a response back to the user
    con="Nothing"
    if message=="hi":
      con="hello"
    await cl.Message(
        content=f'{con}',
    ).send()