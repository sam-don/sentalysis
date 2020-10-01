from Twitter import Twitter
from Analysis import Analysis

twitter = Twitter()
analysis = Analysis()

analysis.load_saved()

running = True

print("Welcome to SentAlysis!\n")

while running:

    user_option = input("""
1. Enter text to be analysed
2. Provide a text file to analyse
3. Search Twitter and retrieve tweets to analyse
4. Load previously saved report
5. Quit

What would you like to do? (Enter 1, 2, 3, 4 or 5) """)

    if user_option == '5':
        running = False
        break
    elif user_option == '4':
        analysis.view_saved()
        continue
    elif user_option == '3':

        print("""
There are a few options you can use for Twitter search:

Add '@' at the start to get a specific Twitter users tweets.
Add '#' to get the tweets with a particular hashtag.

Anything else will be accepted as a generic Twitter search.
""")

        twitter_user = input("\nEnter Twitter username, \
hashtag or search query: ")

        latest_tweets = twitter.get_tweets(twitter_user)
        if latest_tweets == []:
            continue

        data = twitter.parse_tweets(latest_tweets)

    elif user_option == '2':
        data = ''

        while not data:
            filename = input("\nEnter filename of file to analyse: ")
            data = analysis.read_file(filename)

    elif user_option == '1':
        data = input("\nPlease enter the text to analyse here.\n\
Pressing Enter will submit text for analysis.\n\n")

    else:
        print("\nThat was not a valid option, try again.")
        continue

    deep_ai_data = analysis.analyse_text(data)
    if deep_ai_data == []:
        continue

    analysed_data = analysis.collate_data(deep_ai_data)

    analysis.view_report(analysed_data)
