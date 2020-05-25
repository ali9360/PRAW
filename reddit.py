import praw
reddit = praw.Reddit(
                    client_id='YOUR CLINET ID',
                    client_secret='YOUR SECRET CODE',
                    password='YOUR PASSWORD',
                    user_agent='YOUR USER AGENT',
                    username='YOUR USERNAME'
                    )
subreddit = reddit.subreddit('pics')
reply_text = 'Usman Khalid And Ali Ahmad Bot Reply using API'
for submission in subreddit.stream.submissions():
    submission.reply(reply_text)
    print(submission)
    break
