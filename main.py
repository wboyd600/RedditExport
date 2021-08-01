import ExportReddit
import RedditUpdater
import json


class Account:
    def __init__(self, config, data):
        self.user_agent = data[config]["user_agent"]
        self.client_id = data[config]["client_id"]
        self.client_secret = data[config]["client_secret"]
        self.password = data[config]["password"]
        self.username = data[config]["username"]


def main():
    with open('config.json') as f:
        data = json.load(f)


    print(ex_user_agent)


if __name__ == "__main__":
    main()
