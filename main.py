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

    def GetValues(self):
        return [self.client_id, self.client_secret, self.password, self.user_agent, self.username]


def main():
    with open('config.json') as f:
        data = json.load(f)

    acc = Account("export", data)
    vals = acc.GetValues()
    # print(vals[0])
    # print(type(vals[0]))

    exporter = ExportReddit.RedditExporter(vals[0], vals[1], vals[2], vals[3], vals[4])
    exporter.ExportSubs()


if __name__ == "__main__":
    main()
