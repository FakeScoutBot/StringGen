from pyrogram import filters
from pyrogram.types import Message

from StringGen import Anony
from StringGen.utils import add_served_user, keyboard

# Path to your bot's welcome video
WELCOME_VIDEO = "https://files.catbox.moe/z9ap9u.mp4"  # Adjust filename to match your video file

@Anony.on_message(filters.command("start") & filters.private & filters.incoming)
async def f_start(_, message: Message):
    # Send the video with caption
    await message.reply_video(
        video=WELCOME_VIDEO,
        caption=f"ʜᴇʏ {message.from_user.first_name},\n\n๏ ᴛʜɪs ɪs {Anony.mention},\nsᴛʀɪɴɢ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ, ᴡʀɪᴛᴛᴇɴ ɪɴ ᴩʏᴛʜᴏɴ ᴡɪᴛʜ ᴛʜᴇ ʜᴇʟᴩ ᴏғ ᴩʏʀᴏɢʀᴀᴍ.",
        reply_markup=keyboard,
        width=640,
        height=360,
        supports_streaming=True
    )
    await add_served_user(message.from_user.id)