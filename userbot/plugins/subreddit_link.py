from pyrogram import Filters, Message
from userbot import UserBot
from userbot.plugins.help import add_command_help

the_regex = "^r\/([^\s\/])+"


# Generate full Reddit link with subreddit
@UserBot.on_message(Filters.regex(the_regex) & Filters.me)
async def subreddit_link(bot: UserBot, message: Message):
    html = "<a href='{link}'>{string}</a>"
    await message.edit(
        html.format(link="https://reddit.com/" + message.text, string=message.text),
        disable_web_page_preview=True,
        parse_mode="html"
    )


# Command help section
add_command_help(
    'reddit', [
        ['r/telegram', 'As long as your message starts with r/, it will automatically generate a subreddit link and '
                       'hyperlink your message.'],
    ]
)
