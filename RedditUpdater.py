import praw
import os


def DeleteTextFile():
    if os.path.exists("subs.txt"):
        os.remove("subs.txt")
    else:
        print("The file does not exist")


class RedditUpdater:
    def __init__(self, user_agent, client_id, client_secret, username, password):
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            password=password,
            user_agent=user_agent,
            username=username,
        )
        self.subscribed_subreddits = list(self.reddit.user.subreddits(limit=None))

    def UnsubscribeAll(self):
        if len(self.subscribed_subreddits) == 0:
            print('Account not subbed to any subreddit')
            return

        for sub in self.subscribed_subreddits:
            self.reddit.subreddit(sub.display_name).unsubscribe()
        self.subscribed_subreddits = list(self.reddit.user.subreddits(limit=None))

    def PrintSubs(self):
        if len(self.subscribed_subreddits) == 0:
            print('Account not currently subscribed to any subreddits')
            return

        for sub in self.subscribed_subreddits:
            print(sub.display_name)

    def SubscribeFromTextFile(self):
        subs = []
        with open('subs.txt') as f:
            for line in f:
                subs.append(line)
        f.close()
        for s in subs:
            self.reddit.subreddit(s).subscribe()
        self.subscribed_subreddits = list(self.reddit.user.subreddits(limit=None))


#
# updater = RedditUpdater(user_agent, client_id, client_secret, username, password)
# updater.PrintSubs()
# # updater.UnsubscribeAll()
# # updater.SubscribeFromTextFile()

