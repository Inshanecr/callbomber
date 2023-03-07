from pyrogram import Client

# Authenticate and create client object
api_id = 9339443
api_hash = 'ffc626f37ccd0c0290fc0624321fd77c'
client = Client('my_session', api_id, api_hash)
from i import *
# Upload file to channel
channel_username = 'resqqxw'
count = 0
with client:
  for i in a :
   try:
         
         client.send_video(channel_username, i,caption=f"""  
✞𝙋𝙊𝙍𝙉 𝙔𝙊𝙐𝙍 𝙄𝙎 𝙍𝙀𝘼𝘿𝙔✞

𝙈𝙔𝙋𝙑 : @looQaatvw
𝙎𝙋𝙊𝙉𝙎𝙊𝙍 : @Molfee   
{count}
         """)
         
         count +=1
   except Exception as e:
        print(e)