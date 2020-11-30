from bot import telegram_chatbot
from mozilla import Google
from selenium.webdriver.firefox.options import Options

usernameStr = 'YOUR GMAIL ID'
passwordStr = 'YOUR PASSWORD'
token = 'YOUR TELEGRAM API TOKEN'  # get your toke @BotFather

bot = telegram_chatbot(token)


def make_reply(msg):
    reply = None
    if msg is not None:
        reply = msg
    return reply


url_meet = 'https://meet.google.com/gpd-yhgs-apq'
options = Options()

# Enable if you don't want GUI
# options.add_argument("--headless")
# options.add_argument("--disable-infobars")
options.set_preference("permissions.default.microphone", 2)
options.set_preference("permissions.default.camera", 2)


update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = str(item["message"]["text"])
            except:
                message = None
            from_ = item["message"]["from"]["id"]

            if message == '/quit':
                message = 'Quit Completed'

            else:
                msg = message.split()
                message = msg[0]
                try:
                    tim = int(msg[1])*60
                except:
                    tim = 90*60

                Google(usernameStr, passwordStr, options, message, tim)
                message = 'Meeting Ended Successfully ' + \
                    message + ' for '+str(tim) + ' Seconds'

            reply = make_reply(message)
            bot.send_message(reply, from_)
