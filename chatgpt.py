
#-----------CREDITS -----------
# telegram : @itz_legend_coder
# github : noob-mukesh
from pyrogram import Client, filters,enums,idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.enums import ChatAction, ParseMode
import openai
from pyrogram.types import CallbackQuery
from config import *
import os,sys,re,requests
import asyncio,time
from random import choice

from datetime import datetime
import logging

FORMAT = "[LEGEND-MUKESH] %(message)s"
logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


StartTime = time.time()
Mukesh = Client(
    "chat-gpt" ,
    api_id = API_ID,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)

    
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="𓆩⌁ 𝘼𝙙𝙙 𝙈𝙚 𝙄𝙣 𝙔𝙤𝙪𝙧 𝙂𝙧𝙤𝙪𝙥 ⌁𓆪",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="𓆩⌁ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 ⌁𓆪", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', url=f"{SOURCE}")]])
HELP_READ = "𝙃𝙀𝙔 𝙃𝙀𝙍𝙀 𝙄𝙎 𝙃𝙀𝙇𝙋 𝙈𝙀𝙉𝙐\n\n𝙐𝙎𝘼𝙂𝙀 - /𝙘𝙝𝙖𝙩𝙜𝙥𝙩 ┌𝙌𝙪𝙚𝙧𝙮┐\n\n𝙀𝙭𝙥 - /𝙘𝙝𝙖𝙩𝙜𝙥𝙩 𝙃𝙤𝙬 𝙏𝙤 𝙈𝙖𝙠𝙚 𝘼 𝙎𝙞𝙢𝙥𝙡𝙚 𝙋𝙖𝙥𝙚𝙧 𝘽𝙤𝙖𝙩  \n\n 𝘼𝙡𝙞𝙫𝙚 - 𝘾𝙝𝙚𝙘𝙠 𝘽𝙤𝙩 𝙄𝙨 𝙒𝙤𝙧𝙠𝙞𝙣𝙜 𝙊𝙧 𝙉𝙤𝙩\n\n(𝘾𝙤𝙢𝙢𝙖𝙣𝙙) - /𝙥𝙞𝙣𝙜 , /𝙖𝙡𝙞𝙫𝙚\n\n𝙋𝙤𝙬𝙚𝙧𝙚𝙙 𝘽𝙮 :- @𝙏𝙝𝙚𝙑𝙚𝙥𝙚𝙓"

HELP_BACK = [
    [
        InlineKeyboardButton(text="𓆩⌁ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 ⌁𓆪", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(text="𝘽𝙖𝙘𝙠", callback_data="HELP_BACK"),
    ],
]


  
#         start
@Mukesh.on_message(filters.command(["start", f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
    accha = await m.reply_text(text='𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜')
    await asyncio.sleep(0.2)
    await accha.edit_text('𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜.')
    await asyncio.sleep(0.2)
    await accha.edit_text('𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜..')
    await asyncio.sleep(0.2)
    await accha.edit_text('𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜...')
    await asyncio.sleep(0.2)
    await accha.edit_text('𝙎𝙩𝙖𝙧𝙩𝙞𝙣𝙜....')
    await asyncio.sleep(0.2)
    await accha.edit_text('𝙎𝙩𝙖𝙧𝙩𝙚𝙙')
    await accha.delete()

    await m.reply_photo(
        photo=START_IMG,
        caption=START,
        reply_markup=InlineKeyboardMarkup(MAIN),
    )

    await asyncio.sleep(0.3)


        
#  callback 
@Mukesh.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    
@Mukesh.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def restart(client, message):
    hmm = await message.reply_text(
                        text = HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Mukesh.on_message(filters.command(['source', 'repo'], prefixes=["","+", ".", "/", "-", "?", "$"]))
async def source(bot, m):
    
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
#  alive
@Mukesh.on_message(filters.command(["ping", "alive"], prefixes=["", "+", "/", "-", "?", "$", "&", "."]))
async def ping(client, message: Message):
    start = datetime.now()
    t = "𝙋𝙞𝙣𝙜"
    txxt = await message.reply(t)
    await asyncio.sleep(0.25)
    await txxt.edit_text("𝙋𝙞𝙣𝙜..𝘾𝙤𝙢𝙞𝙣𝙜")
    await asyncio.sleep(0.35)
    await txxt.edit_text("𝙋𝙞𝙣𝙜...𝙒𝙖𝙞𝙩")
    await asyncio.sleep(0.35)
    await txxt.edit_text("𝙋𝙞𝙣𝙜....𝘾𝙖𝙡𝙘𝙪𝙡𝙖𝙩𝙚𝙙")
    await asyncio.sleep(0.35)
    await txxt.edit_text("𝙎𝙝𝙤𝙬𝙞𝙣𝙜..... 𝙍𝙚𝙨𝙪𝙡𝙩𝙨")
    await txxt.delete()
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%Y-%m-%d")
    
    # Respond with the ping message including time and date
    response = f"Pong! Current time: {current_time}, Current date: {current_date}"
    message.reply_text(response)
#  main   
openai.api_key = OPENAI_KEY
@Mukesh.on_message(filters.command(["chatgpt","ai","ask"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"]))
async def chat(bot, message):
    
    try:
        start_time = time.time()
        await bot.send_chat_action(message.chat.id, ChatAction.TYPING)
        if len(message.command) < 2:
            await message.reply_text(
            "Example:**\n\n`/chatgpt Where is TajMahal?`")
        else:

            a = message.text.split(' ', 1)[1]
            MODEL = "gpt-3.5-turbo"
            resp = openai.ChatCompletion.create(model=MODEL,messages=[{"role": "user", "content": a}],
    temperature=0.2,
)

            x=resp['choices'][0]["message"]["content"]
            end_time = time.time()
            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"
            await message.reply_text(f"{message.from_user.first_name} ᴀꜱᴋᴇᴅ:\n\n {a} \n\n {BOT_NAME} ᴀɴꜱᴡᴇʀᴇᴅ:-\n\n {x}\n\n✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ  {telegram_ping} \n\n🎉ᴘᴏᴡᴇʀᴇᴅ ʙʏ @{BOT_USERNAME} ", parse_mode=ParseMode.MARKDOWN,reply_markup=InlineKeyboardMarkup(X))     
    except Exception as e:
        await message.reply_text(f"**ᴇʀʀᴏʀ:    {e} ")

@Mukesh.on_message(filters.command(["image","photo","img","generate"],  prefixes=["","+", ".", "/", "-", "?", "$","#","&"] ))

async def chat(bot, message):

    try:



        start_time = time.time()

        await bot.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)

        if len(message.command) < 2:

            await message.reply_text(

            "**Example:**\n\n`/generate a white siamese cat`")

        else:

            a = message.text.split(' ', 1)[1]

            response= openai.Image.create(prompt=a ,n=1,size="1024x1024")

            image_url = response['data'][0]['url']

            end_time = time.time()

            telegram_ping = str(round((end_time - start_time) * 1000, 3)) + " ᴍs"

            await message.reply_photo(image_url,caption=f"✨ᴛɪᴍᴇ ᴛᴀᴋᴇɴ {telegram_ping} ",parse_mode=ParseMode.DISABLED,reply_markup=InlineKeyboardMarkup(X)) 

    except Exception as e:

            await message.reply_text(f"**ᴇʀʀᴏʀ: **  ` {e} `")

    

    



if __name__ == "__main__":
    print(f""" {BOT_NAME} ɪs ᴀʟɪᴠᴇ!
    """)
    try:
        Mukesh.start()
        
        
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    print(f"""JOIN  @MR_SUKKUN
GIVE STAR TO THE REPO 
 {BOT_NAME} ɪs ᴀʟɪᴠᴇ!  
    """)
    idle()
    Mukesh.stop()
    print("Bot stopped. Bye !")
#-----------CREDITS -----------
# telegram : @itz_legend_coder
# github : noob-mukesh
