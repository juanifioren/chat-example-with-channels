from channels.testing import WebsocketCommunicator
import pytest

from chat.routing import application


@pytest.mark.asyncio
async def test_chat_consumer_connection():
    communicator = WebsocketCommunicator(application, '/ws/chat/foo-bar/')
    connected, subprotocol = await communicator.connect()
    assert connected
    await communicator.disconnect()
