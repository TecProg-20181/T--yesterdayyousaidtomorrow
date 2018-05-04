# Yesterday You Said Tomorrow! - Rajesh

That is a Telegram Bot that manages tasks created by user's messages. Originally created for a discipline of Programming Techniques in [Brasília University](http://www.unb.br/).

You may find the homologation version at https://t.me/YesterdayYouSaidTomorrowBot

Or, if you wish to launch the code, follow the steps below:

## How to Setup (Linux)
- At first, clone this repository to your machine.
- To start your bot, go to [BotFather](https://telegram.me/BotFather) and ask to create a new bot for you. This is the bot who will send the messages generated by the code you just cloned. If you need any help, follow this [tutorial](https://core.telegram.org/bots#6-botfather).
- Then, copy the token provided by BotFather at the moment of creation and do command in your terminal `export BOT_API_TOKEN="<your token here>"`. This will set env a variable that the code will catch and set up the bot you just created.
- Run `pip3 install -r requirements.txt` in the project folder to install the dependencies of the project. You may like to set a [virtual environment](https://virtualenv.pypa.io/en/stable/) to make it.
- Finally, run `python3 taskbot.py` and send a message to your bot.
- To see what the bot can do, just do `/help`

**Note**: The conversation module still in progress.
