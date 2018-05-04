import requests
import constants
from BotManager import BotManager


class IssueManager:
    def __init__(self):
        self.bot_manager = BotManager()

    def split_message(self, msg):
        text = ''
        if msg != '':
            if len(msg.split(' ', 1)) > 1:
                text = msg.split(' ', 1)[1]
            msg = msg.split(' ', 1)[0]
        return msg, text

    def new_issue(self, name, chat):
        """Create an Issue"""
        payload = "{\n  \"title\": \""+name+"\",\n  \"labels\": [\n    \"telegram\"\n  ]\n}"
        print(payload)
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Basic WWVzdGVyZGF5WW91U2FpZFRvbW9ycm93Qm90Olllc3RlcmRheVlvdVNhaWRUb21vcnJvdw==",
            'Cache-Control': "no-cache",
            'Postman-Token': "49817fa1-698d-496d-b6e3-252e81bc792f"
        }

        response = requests.request("POST", constants.URL_GITHUB, data=payload, headers=headers)

        print(response.text)

        return self.bot_manager.send_message("New Issue created {}".format(name), chat)

    def rename_issue(self, msg, chat):
        """rename a task by id"""
        msg, text = self.split_message(msg)

        if text == '':
            self.bot_manager.send_message("""
                          You want to modify the issue {},
                          but you didn't provide any new text
                         """.format(msg), chat)
            return

        payload = "{\n  \"title\": \""+text+"\",\n  \"labels\": [\n    \"telegram\"\n  ]\n}"
        print(payload)
        headers = {
            'Content-Type': "application/json",
            'Authorization': "Basic WWVzdGVyZGF5WW91U2FpZFRvbW9ycm93Qm90Olllc3RlcmRheVlvdVNhaWRUb21vcnJvdw==",
            'Cache-Control': "no-cache",
            'Postman-Token': "49817fa1-698d-496d-b6e3-252e81bc792f"
        }
        result = requests.request("GET", constants.URL_GITHUB + msg)

        try:
            result['message']
        except:
            self.bot_manager.send_message("Issue does not exist", chat)

        requests.request("POST", constants.URL_GITHUB+'/'+msg, data=payload, headers=headers)
        return self.bot_manager.send_message("Issue renamed {}".format(text), chat)