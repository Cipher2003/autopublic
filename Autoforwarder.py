from telethon import TelegramClient
import asyncio
import random
import time

# Your API ID and Hash (use your provided values)
api_id = 22681300  # Provided API ID
api_hash = '8ee9f50de39c4491738d535b2645c2eb'  # Provided API Hash

# Define your phone number
phone_number = '+919890932292'  # Provided phone number

# Source channels (you can add more if needed)
source_channels = [-1002008845219, -1001122719303]

# Destination channel ID
destination_channel = -4779805716  # Destination channel ID: Des content

# Create the client
client = TelegramClient('auto_forwarder_session', api_id, api_hash)

async def forward_messages_from_channel(source_channel):
    """Forward the last 50 messages from the source channel to the destination with random batch split."""
    print(f"Checking messages from source channel {source_channel}...")

    # Fetch the last 50 messages from the source channel
    messages = []
    async for message in client.iter_messages(source_channel, limit=50):
        messages.append(message)
    
    # Split messages into two batches with random splits (20-30 each)
    batch1_size = random.randint(20, 30)
    batch2_size = 50 - batch1_size

    # Get the first batch of messages
    batch1 = messages[:batch1_size]
    # Get the second batch of messages
    batch2 = messages[batch1_size:]

    # Forward the first batch
    print(f"Forwarding batch 1 with {batch1_size} messages...")
    for message in batch1:
        await message.forward_to(destination_channel)

    # Random delay between batches
    batch_delay = random.randint(3, 6)
    print(f"Waiting for {batch_delay} seconds after forwarding batch 1...")
    time.sleep(batch_delay)

    # Forward the second batch
    print(f"Forwarding batch 2 with {batch2_size} messages...")
    for message in batch2:
        await message.forward_to(destination_channel)

    # Random delay between batches
    batch_delay = random.randint(3, 6)
    print(f"Waiting for {batch_delay} seconds after forwarding batch 2...")
    time.sleep(batch_delay)

async def main():
    await client.start(phone_number)  # Start the client using phone number
    for source_channel in source_channels:
        await forward_messages_from_channel(source_channel)  # Forward messages from each source to destination
    await client.disconnect()  # Disconnect after operation

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
