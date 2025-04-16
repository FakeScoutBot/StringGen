import time
from datetime import datetime

from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony

# Start time of the bot to calculate uptime
START_TIME = datetime.now()

@Anony.on_message(filters.command("ping") & filters.incoming)
async def ping_handler(_, message: Message):
    """
    Handler for /ping command.
    Displays bot response time and uptime.
    """
    # Record start time
    start_time = time.time()
    
    # Send initial message that will be updated
    initial_message = await message.reply_text("Pinging...")
    
    # Calculate ping time
    end_time = time.time()
    ping_time = round((end_time - start_time) * 1000)  # in milliseconds
    
    # Calculate uptime
    uptime = datetime.now() - START_TIME
    days = uptime.days
    hours, remainder = divmod(uptime.total_seconds() - days * 86400, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Format uptime string
    uptime_string = f"{days}d:{int(hours)}h:{int(minutes)}m:{int(seconds)}s"
    
    # Update the initial message with the simplified response
    await initial_message.edit_text(
        f"Pong !! {ping_time}ms\nUptime - {uptime_string}"
    )