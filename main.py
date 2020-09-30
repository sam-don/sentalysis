from Twitter import Twitter
from Analysis import Analysis

twitter = Twitter()
analysis = Analysis()

running = True

print("Welcome to SentAlysis!\n")

while running:

    user_option = input("""
1. Enter text to be analysed
2. Provide a text file to analyse
3. Search Twitter and retrieve tweets to analyse
4. Quit

What would you like to do? (Enter 1, 2, 3 or 4) """)

    if user_option == '4':
        running = False
        break
    elif user_option == '3':

        print("""There are a few options you can use for Twitter search:
        
Add '@' at the start to get a specific Twitter users tweets.
Add '#' to get the tweets with a particular hashtag.

Anything else will be accepted as a generic Twitter search.
""")

        twitter_user = input("Enter Twitter username, hashtag or search query: ")

        latest_tweets = twitter.get_tweets(twitter_user)
        if latest_tweets == []:
            continue

        data = twitter.parse_tweets(latest_tweets)
    elif user_option == '2':
        print("Sorry, This functionality isn't available yet.")
        continue
    elif user_option == '1':
        print("Please enter the text to analyse here.\n"
              "To end recording Press Ctrl+D on Linux/Mac on Crtl+Z on Windows\n")
        lines = []
        try:
            while True:
                lines.append(input())
        except EOFError:
            pass
        data = "\n".join(lines)
        # data = input("Enter the text you would like to analyse here:\n\n")
    else:
        print("That was not a valid option, try again.")
        continue

    deep_ai_data = analysis.analyse_text(data)
    if deep_ai_data == []:
        continue

    analysed_data = analysis.collate_data(deep_ai_data)

    analysis.view_report(analysed_data)
