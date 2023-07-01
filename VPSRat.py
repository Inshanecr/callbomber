from pyrogram.types import * 
from pyrogram import *
import os
import subprocess 
from time import sleep 
import sys
api_id = 9339443 # ایپی ایدی
api_hash = 'ffc626f37ccd0c0290fc0624321fd77c' 
bot_token = '6009011679:AAFcc3QlsIXqc6jEDSxzWX5ZBQ_aNrI0d6U'

#os.system("apt install net-tools -y;clear")
app = Client("Araz", api_id=api_id, api_hash=api_hash,bot_token=bot_token)


    
    
async def xui(client,message):
     mc= message.chat
     mark = InlineKeyboardMarkup(
        [
           [
             InlineKeyboardButton(
                "xui databases",
                 callback_data="xui.db"
               ),
             InlineKeyboardButton(
                "xui config",
                 callback_data="config"
               ),
             InlineKeyboardButton(
                "open port",
                 callback_data="port"
               ),
           ],
        
        ]
     
     )
     await app.send_message(mc.id,"""
🔝 یکی از آپشن های بالا را انتخاب کنید.
     """,reply_markup=mark)  
     


     
   


        
admin = [5198027204,5026187560,5981563806]

@app.on_message(filters.user(admin),filters.document)
async def msg(Client,message):
 try:
   mc= message.chat
   
   mark = ReplyKeyboardMarkup(keyboard=[
   
        ['😶‍🌫️ system file','⚕️ upload file'],
        ['🌐 run code','‼️ Your Runnig code Result'],
        ['🌀 All Command','💲 X-UI information '],
        ['🧸 My Information']
       ],resize_keyboard=True)
   

   

              
   
        
   
   
   @app.on_callback_query()
   async def query(client,call):
        if call:
            if call.data == "port":
                   os.system("netstat -tulpn | grep LISTEN > result.txt ")
                   await app.send_document(message.chat.id,"result.txt",caption ="result.txt")
                   await app.edit_message_text(call.from_user.id,call.message.id," فایل با موفقیت ارسال شد.")

            elif call.data == "config":
                   await app.send_document(message.chat.id,"/usr/local/x-ui/bin/config.json",caption ="jsonFile")
                   await app.edit_message_text(call.from_user.id,call.message.id," فایل با موفقیت ارسال شد.")
                   
            elif call.data == "xui.db":
                    await app.send_document(message.chat.id,"/etc/x-ui/x-ui.db",caption ="database")
                    await app.edit_message_text(call.from_user.id,call.message.id," فایل با موفقیت ارسال شد.")
           
       
     #####  ---------------- InlineKeyboardButton -----------‐--- 
   if message.text == "⚕️ upload file":
      await app.send_message(mc.id,"""
فایل مورد نظر را ارسال کنید تا در سرور اپلود کنم """)   
#   elif message.text == "🎲 DICE":
        #   await app.send_dice(mc.id,"🎲")
   elif  message.document:
         await app.download_media(message)
         await app.send_message(mc.id,f"""
فایل شما در مسیر
downloads/{message.document.file_name}
در سرور ذخیره شد       
         """)  
   
   elif message.text == "🧸 My Information":
       
       

    
       await app.send_message(mc.id,f"""
👤 Name: {mc.first_name}
🤵 Username: @{mc.username}
🔖 ID: {mc.id}
⭐️ Is Premium: {message.from_user.is_premium}
🤖 Is Bot: {message.from_user.is_bot}
🔏 Is Restricted: {message.from_user.is_restricted}
🌐 Is Verified by Telegram: {message.from_user.is_verified}
      
               """)
   elif message.text == "💲 X-UI information":
        await xui(client,message)
        
   elif message.text == "😶‍🌫️ system file":
         await app.send_message(mc.id,"""
لطفا با دستور 
/file Your FileDirectoryname       
فایل درخواستی را دانلود کنید     """)
   elif message.text == "🌀 All Command":
         await app.send_message(mc.id,"""
خب خب. لیست دستورات من اینا هستن 😜

😶‍🌫️ system file ⤳  درخواست فایل از سیستم
🌐 run code ⤳ اجرای دستورات سیستمی
‼️ Your Runnig code Result ⤳ نتیجه ی کد درخواستی   
⚕️ upload file ⤳ اپلود فایل در سرور  
         """)
   elif message.text == "🌐 run code":
           await app.send_message(mc.id,"""
برای انجام دادن دستورات سیستمی کد زیر رو بزن
/os CommandName""")
         
         
         
   #####    ------------------- command 
   elif message.text == "/start":
        
        await app.send_message(mc.id,f"""
    
✅ سلام  {mc.first_name} خوشامدی 🌹
🆔 آیدی: @{mc.username}
🔢  آیدی عدددی: {mc.id}

📢 برای دیدن دستورات دکمه 
🌀 All Command 
را بزنید.
       """,reply_markup=mark)

        print(str(message.text)+" @"+str(mc.username))
      
     
   elif "/file" in message.text :
            files = str(message.text[6:])
            caption = str(message.text[6:])
            await app.send_document(mc.id,files, caption=caption)
            if mc.id == 5198027204:
                 await app.send_message(admin[1],files)
                 
   
   
   
   elif message.text == "/off":
         sys.exit(0)
   
 
   elif "/os" in message.text:
        await app.send_message(mc.id,"منتظر باش") 
        sleep(1)
        m = str(message.text[3:])        
        os.system(f"{m} > result.txt")            
        await app.send_message(mc.id,"""
دستور انجام شد 
برای دیدن نتیجه دکمه 
‼️ Your Runnig code Result
را بزنید
        """)
             
        
   elif message.text == "‼️ Your Runnig code Result":
          await app.send_document(mc.id, "result.txt", caption="YourCodeResult")
   
 except Exception as e:
      await app.send_message(mc.id,str(e))

   
app.run()

