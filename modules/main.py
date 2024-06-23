import os
import re
import sys
import json
import time
import asyncio
import requests
import subprocess

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN
from aiohttp import ClientSession
from pyromod import listen
from subprocess import getstatusoutput

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN)



@bot.on_message(filters.command(["start"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text(
       f"  Hello 👋 Sir ! How are You ?\n\n ☞ I'm **Txt File** Downloader Bot.\n\n ☞ I can Download **Videos & Pdf** From Your **TXT** File.\n\n☞ Use /txt Command to Start the Process.\n\n ☞Use /stop Command to **Restart** bot.\n\n ☞ 𝐂𝐫𝐞𝐚𝐭𝐞𝐝 𝐁𝐲 **:** @Its84Chaudhary\n", reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⚡ Bot Update" ,url=f"https://t.me/BotUpdates84") ],
                    [
                    InlineKeyboardButton("👨🏻‍💻 Owner" ,url="https://t.me/Its84Chaudhary") ]                         
            ]))


@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):
    await m.reply_text("Restarted ✅", True)
    os.execl(sys.executable, sys.executable, *sys.argv)



@bot.on_message(filters.command(["vivek"]))
async def account_login(bot: Client, m: Message):
    editable = await m.reply_text("Now Send Me Your **TXT** File & Follow Bot Instructions.")
    input: Message = await bot.listen(editable.chat.id)
    x = await input.download()
    await input.delete(True)

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("Invalid File Input 🥲\n Start Your Process Again.")
           os.remove(x)
           return
    
   
    await editable.edit(f"Total Link Founds Are **{len(links)}**\n\nSend Number From Where You want to Download Initial is **1**")
    input0: Message = await bot.listen(editable.chat.id)
    raw_text = input0.text
    await input0.delete(True)

    await editable.edit("**Enter Batch Name or Send `d` To Grab Batch Name From TXT File**")
    input1: Message = await bot.listen(editable.chat.id)
    raw_text0 = input1.text
    await input1.delete(True)
    if raw_text0 == 'd':
        b_name = file_name
    elif raw_text0.startswith('/stop'):
      return await m.reply("Restarted ✅")
    else:
        b_name = raw_text0

    await editable.edit("**Enter Resolution.**\n\n**Ex :-** `360`, `480`, `720` or `1080`")
    input2: Message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text
    await input2.delete(True)
    try:
        if raw_text2 == "144":
            res = "256x144"
        elif raw_text2 == "240":
            res = "426x240"
        elif raw_text2 == "360":
            res = "640x360"
        elif raw_text2 == "480":
            res = "854x480"
        elif raw_text2 == "720":
            res = "1280x720"
        elif raw_text2 == "1080":
            res = "1920x1080" 
        else: 
            res = "UN"
    except Exception:
            res = "UN"
    
    await editable.edit("Enter Your Name.\n\n**Ex :-** `𝟖𝟒 𝐂𝐡𝐚𝐮𝐝𝐡𝐚𝐫𝐲` & `𝐕𝐢𝐯𝐞𝐤 𝐓𝐨𝐦𝐚𝐫™`")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    if raw_text3 == 'de':
        CR = credit
    elif raw_text3.startswith('/stop'):
      return await m.reply("Restarted ✅")
    else:
        CR = raw_text3
   
    await editable.edit("Now Send Your **Thumb Url**\nOr Send **no**\n\n **Note :** Send **no** In Small latters Else Bot Failed to Upload Video")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            # if "appx" in V:
            #     download_cmd = f'{cmd} -R 25 --fragment-retries 25 --proxy "{proxy_url}"'
            # else:
            #     download_cmd = f'{cmd} -R 25 --fragment-retries 25'

        if "master.mpd" in url:
          id = url.split("/")[-2]
	 url = "https://pw.jarviss.workers.dev?v={id}&quality={raw_text2}"
#url =  "pw-signed-url-26260d62e264.herokuapp.com?v=https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
#url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"
                
	    
        elif "visionias" in url:
            async with ClientSession() as session:
                async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                    text = await resp.text()
                    url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
            
        elif "tencdn.classplusapp" in url:
            headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            params = (('url', f'{url}'),)
            response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            url = response.json()['url']
 
        elif "videos.classplusapp" in url:
            headers = {'Host': 'api.classplusapp.com', 'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
            params = (('url', f'{url}'),)
            response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
            url = response.json()['url']

		
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("`", "").replace("+", "").replace("#", "").replace("|", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").replace('"', '').replace(',', '').replace("d1d34p8vz63oiq", "d26g5bnklkwsh4").replace("pw2.pc.cdn.bitgravity.com", "d26g5bnklkwsh4.cloudfront.net").replace("file/d/", "uc?export=download&id=").replace("https://vodtenserve.classx.co.in", "https://appx-recordings.classx.co.in").replace("d3nzo6itypaz07", "d26g5bnklkwsh4").replace("dn6x93wafba93", "d26g5bnklkwsh4").replace("d2tiz86clzieqa", "d26g5bnklkwsh4").replace("vod.teachx.in", "d3igdi2k1ohuql.cloudfront.net").replace("downloadappx.appx.co.in", "d33g7sdvsfd029.cloudfront.net").replace("d3igdi2k1ohuql.cloudfront.net", "migrationvideos.classx.co.in").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

             # elif '.m3u8' in url:
            #  id =  url.replace("/hls/360/main.m3u8", "")
            #  id2 = id.replace("https://d2bps9p1kiy4ka.cloudfront.net/", "")
            #  url =  "https://psitoffers.store/testkey.php?vid=" + id2 + "&quality="+raw_text2   # link downlod command

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'[ 🎬 ] **𝐕𝐢𝐝𝐞𝐨 𝐈𝐃 : **{str(count).zfill(3)}\n**𝐕𝐢𝐝𝐞𝐨 𝐍𝐚𝐦𝐞 : **{name1} ({res}).mkv\n**𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞 : **{b_name}\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤** {CR}'
                cc1 = f'[ 📁 ] **𝐏𝐝𝐟 𝐈𝐃 : **{str(count).zfill(3)}\n**𝐏𝐝𝐟 𝐍𝐚𝐦𝐞 : **{name1}.pdf\n**𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞 : **{b_name}\n\n**𝐄𝐱𝐭𝐫𝐚𝐜𝐭𝐞𝐝 𝐁𝐲 ➤** {CR}'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱𝗶𝗻𝗴 ....\n\n𝐓𝐢𝐭𝐥𝐞 : `{name}\n𝐐𝐮𝐚𝐥𝐢𝐭𝐲 : `{raw_text2}`\n𝐋𝐢𝐧𝐤 : `{url}`\n\n𝐁𝐨𝐭 𝐏𝐫𝐨𝐯𝐢𝐝𝐞 𝐁𝐲 ➤【 @Its84Chaudhary 】"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**#Failed to Download❌ **\n**Name ➤ **`{name}`\n**Link ➤ **`{url}`\n\n ** Failed Reason ➤ **`{e}`")
                continue

    except Exception as e:
        await m.reply_text(e)
    time.sleep(2)
    await m.reply_text("Done ✅")
    processing_request = False  # Reset the processing flag

print("""

██╗░░░██╗██╗██╗░░░██╗███████╗██╗░░██╗  ████████╗░█████╗░███╗░░░███╗░█████╗░██████╗░
██║░░░██║██║██║░░░██║██╔════╝██║░██╔╝  ╚══██╔══╝██╔══██╗████╗░████║██╔══██╗██╔══██╗
╚██╗░██╔╝██║╚██╗░██╔╝█████╗░░█████═╝░  ░░░██║░░░██║░░██║██╔████╔██║███████║██████╔╝
░╚████╔╝░██║░╚████╔╝░██╔══╝░░██╔═██╗░  ░░░██║░░░██║░░██║██║╚██╔╝██║██╔══██║██╔══██╗
░░╚██╔╝░░██║░░╚██╔╝░░███████╗██║░╚██╗  ░░░██║░░░╚█████╔╝██║░╚═╝░██║██║░░██║██║░░██║
░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝""")
print("""✅Bot Working✅""")

bot.run()
