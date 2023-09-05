from pyrogram import Client, filters
from pyrogram.types import ForceReply
import sqlite3
import json
from datetime import datetime
from pytz import timezone
from urllib.parse import urlparse

async def send_prompt(client, chat_id):
    await client.send_message(chat_id, "Please send your config URI:", reply_markup=ForceReply(selective=True))

def human_readable_size(size, decimal_places=2):
    if size < 0:
        size = 0
    size = float(size)
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.{decimal_places}f} {unit}"


def fetch_inbounds_records(database_path, client_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT down, up, total, remark, expiry_time, settings FROM inbounds;")
        records = cursor.fetchall()
        for record in records:
            down, up, total, remark, expiry_time, settings_json = record
            settings = json.loads(settings_json)
            client_ids = [client.get('id') for client in settings.get('clients', [])]
            if client_id not in client_ids:
                continue

            tehran = timezone('Asia/Tehran')
            tehran_time = datetime.now(tehran).strftime('%Y-%m-%d %H:%M:%S')

            down, up, total = map(int, [down, up, total])

            if total == 0:
                remaining = "Unlimited"
            else:
                remaining = total - (down + up)
                remaining = human_readable_size(max(remaining, 0))

            days_left = ""
            if expiry_time == 0:
                expiry_time = "Indefinitely"
            else:
                expiry_datetime = datetime.fromtimestamp(expiry_time // 1000)
                expiry_time = expiry_datetime.strftime('%Y-%m-%d %H:%M:%S')
                days_left = (expiry_datetime - datetime.now()).days
                days_left = f"{days_left} days left" if days_left >= 0 else "Expired"

            response_text = (f"🔖 Remark: {remark}\n"
                             f"🔻 Download: {human_readable_size(down)}\n"
                             f"🔺 Upload: {human_readable_size(up)}\n"
                             f"📊️ Total: {human_readable_size(total)}\n"
                             f"🔋 Remaining: {remaining}\n"
                             f"🗓️ Expiry Time: {expiry_time}\n"
                             f"🔜 Days Left: {days_left}")
            print(f"{'-' * 30}\nFetched data for {remark} at: {tehran_time}\n{response_text}\n{'-' * 30}")

            return response_text

    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()


def extract_client_id_from_uri(uri):
    parsed_uri = urlparse(uri)
    client_id = parsed_uri.netloc.split('@')[0]
    return client_id

app = Client("my_bot", bot_token="BOT_TOKEN", api_id="API_ID", api_hash="API_HASH")

@app.on_message(filters.command("stats"))
async def stats_command(client, message):
    await send_prompt(client, message.chat.id)

@app.on_message(filters.text & filters.reply)
async def receive_config(client, message):
    if 'Please send your config URI:' in message.reply_to_message.text:
        config_uri = message.text
        client_id = extract_client_id_from_uri(config_uri)

        tehran = timezone('Asia/Tehran')
        tehran_time = datetime.now(tehran).strftime('%Y-%m-%d %H:%M:%S')
        
        database_paths = [
            "x-ui-english-A.db",
            "x-ui-english-B.db",
            "x-ui-english-C.db",
            "x-ui-english-D.db",
        ]

        for db_path in database_paths:
            result = fetch_inbounds_records(db_path, client_id)
            if result:
                await message.reply_text(result)
                return

        await message.reply_text("😞 No matching records found.")

app.run()
