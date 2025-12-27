import os
import asyncio
from pyrogram import Client, filters, idle
from aiohttp import web

# --- CONFIGURATION ---
API_ID = 22177421  # Yahan apna Sahi ID daalo
API_HASH = "e515bbf4a302d7c7335f689a52b196a5"
BOT_TOKEN = "8195696690:AAHQ_VB48ntWzxsawK3-D2Rri_46U-Lse4s"
SESSION_STRING = "BQFSZo0AFqXwDChae7..." # Yahan apna lamba session string daalo

# Clients
bot = Client("MyBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, in_memory=True, ipv6=False)
userbot = Client("MyUser", api_id=API_ID, api_hash=API_HASH, session_string=SESSION_STRING, in_memory=True, ipv6=False)

# --- WEB SERVER (Koyeb Health Check) ---
routes = web.RouteTableDef()
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response({"status": "alive"})

async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app

# --- STARTUP ---
if __name__ == "__main__":
    # Koyeb PORT variable deta hai
    PORT = int(os.environ.get("PORT", 8000))
    
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bot.start())
    loop.run_until_complete(userbot.start())
    
    # Start Server
    app = web.Application()
    app.add_routes(routes)
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    loop.run_until_complete(site.start())
    
    print(f"🚀 Bot Running on Port {PORT}")
    loop.run_forever()
