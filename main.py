from bot import telegram_bot

update_id = None
while True:
    print("...")
    updates = telegram_bot().get_updates(offset = update_id)
    updates = updates["result"]
    if updates:
        for msgs in updates:
            update_id = msgs["update_id"]
            try:
                type = msgs["message"]["chat"]["type"]
                if(type=="private"):
                    message = msgs["message"]["text"]
                    if(message=="/start"):
                        uname = msgs["message"]["from"]["first_name"]
                        message = f"Hey {uname}\nIam Anynous Bot To Send Messages in SKT\nI Was Created By Titan Hacky\n\n Hit /help to find How I work"
                        chat_id = msgs["message"]["chat"]["id"]
                    elif(message=="/help"):
                        message = "Just Message something Here Ill send it in Script Kiddie Tamil"
                        chat_id = msgs["message"]["chat"]["id"]
                    else:
                        message = message
                        chat_id = "-1001244441025"
                elif(type=="group"or type=="supergroup"):
                    message = msgs["message"]["text"]
                    
                    if(message=="/start"):
                        uname = msgs["message"]["from"]["first_name"]
                        message = f"Hey {uname}\nWrite Me In Private"
                        chat_id = msgs["message"]["chat"]["id"]
                    elif(message=="/help"):
                        uname = msgs["message"]["from"]["first_name"]
                        message = f"Hey {uname}\nWrite Me In Private"
                        chat_id = msgs["message"]["chat"]["id"]
                    else:
                        message = ""
                        chat_id = "-100149287915"
                else:
                    message = ""
                    chat_id = "-100149287915"
            except:
                message = ""
                chat_id="-100149287915"
            reply = message
            telegram_bot().send_messages(reply,chat_id)
            #support @TITANHACKY
