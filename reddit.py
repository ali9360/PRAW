import praw
reddit = praw.Reddit(
                    client_id='nJ8qvvY9yhiUyA',
                    client_secret='fqLEJ35aTqPmVlyX2sV-f0K9IUM',
                    password='Ali@Saab8989',
                    user_agent='FieverrApp',
                    username='aliahmad6095'
                    )
subreddit = reddit.subreddit('pics')
reply_text = 'Usman Khalid And Ali Ahmad Bot Reply using API'
for submission in subreddit.stream.submissions():
    submission.reply(reply_text)
    print(submission)
    break