import praw


class RedditExporter:
    def __init__(self, user_agent, client_id, client_secret, username, password):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent=user_agent,
            username=username,
        )

    def ExportSubs(self):
        subscribed_subreddits = list(self.reddit.user.subreddits(limit=None))

        # subs = [s.display_name for s in subscribed_subreddits]
        f = open("subs.txt", "w")
        for s in subscribed_subreddits:
            f.write(s.display_name + '\n')
        f.close()


#
# exporter = RedditExporter(user_agent, client_id, client_secret, username, password)
# exporter.ExportSubs()
