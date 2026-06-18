import uiautomator2 as u2
import asyncio
import time

d = u2.connect()

LAST_MESSAGE = ""

async def read_loop():
    global LAST_MESSAGE

    while True:
        try:
            # Read all messages
            messages = d.xpath('//*[@resource-id="com.wakie.android:id/text"]').all()
            users = d.xpath('//*[@resource-id="com.wakie.android:id/name"]').all()

            if not messages or not users:
                await asyncio.sleep(0.1)
                continue

            # Get the last message
            last_user = users[-1].text
            last_msg = messages[-1].text

            # If it's new, process it
            if last_msg != LAST_MESSAGE:
                LAST_MESSAGE = last_msg
                print(f"{last_user}: {last_msg}")

                # 🔥 Send to your bot command parser here
                # await bot.handle_message(last_user, last_msg)

        except Exception as e:
            print("Error reading UI:", e)

        # Fast polling (10× per second)
        await asyncio.sleep(0.1)


asyncio.run(read_loop())
