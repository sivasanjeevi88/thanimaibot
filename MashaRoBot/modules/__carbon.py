from pyrogram import filters

from MashaRoBot.events import register
from MashaRoBot.utils.errors import capture_err
from MashaRoBot.modules.sql.carbonfunc import make_carbon


@register(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "`Reply to a text message to make carbon.`"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "**Reply to a text message to make carbon.**"
        )
    m = await message.reply_text("**Makeing Carbon...**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading...`")
    await pbot.send_document(message.chat.id, carbon)
    await m.delete()
    carbon.close()

#ZeusXRobot
