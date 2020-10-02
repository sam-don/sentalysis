# SentAlysis

## Sentiment analysis of any text, text file or latest tweets for any Twitter user, hashtag or search term

Analysing text to infer the sentiment behind it can be a useful tool that is used in many industries including politics, finance and medicine to provide valuable insight to make informed business decisions. SentAlysis was designed and built to provide sentiment analysis through Deep AI of text that is input directly by the user, provided in a text file or by searching Twitter for a particular user or search term.

Sentalysis requires a text input to anylse, which can be provided by the user in a few different ways:

- User types text directly into the app.
- User provides a text file to analyse.
- User specifies a username or term to search on Twitter using the Twitter API.

Once the input is provided or retrieved, Sentalysis collates the data and sends it to the Deep AI Semantic Analysis API for analysis. The results are then gathered and displayed to the user.

### Table of Contents

- [SentAlysis](#sentalysis)
  - [Sentiment analysis of any text, text file or latest tweets for any Twitter user, hashtag or search term](#sentiment-analysis-of-any-text-text-file-or-latest-tweets-for-any-twitter-user-hashtag-or-search-term)
    - [Table of Contents](#table-of-contents)
    - [App Structure](#app-structure)
      - [Dependencies](#dependencies)
      - [Flowchart](#flowchart)
    - [Installation](#installation)
    - [Using SentAlysis](#using-sentalysis)

### App Structure

[Back To Top](#sentalysis)

Twitter Class

- get_tweets method

    Send request to Twitter API to retrieve tweets.
  
    input: search term or Twitter username provided by user, max results to retrieve

    output: dictionary of the retrieved tweets

- parse_tweets method

    Retrieved tweets are parsed and just the text content is concatenated into a single string which is returned.

    input: dictionary of the tweets retrieved by the Twitter API

    output: The text content of every tweet concatenated into a single string

Analysis Class

- analyse_text method

    Send text to Deep AI to analyse and return as a list of strings for each phrase analysed.

    input: text provided by user or data received from Twitter API

    output: list of strings provided by Deep AI API

- collate_data method

    Take list provided by Deep AI and collate data into total phrases, totals of each response from Deep AI and return dictionary of values.

    input: list provided by analyse_text method

    output: dictionary of collated data

- view_report method

    Using the data which has been retrieved and collated, generate and display a report for the user to see.

    input: dictionary of collated data, boolean 'saved' to determine whether the report is one that's already saved - default False

    output: none, prints report to terminal

- read_file method

    Reads the contents of a given file and returns the data

    input: the path and/or filename of the file to be read

    output: the data in the file as a string, or an empty string on Exception

- save_file method

    Save analysis results to file

    input: the analysis report to be added to the already saved reports and saved

    output: the saved report

- load_saved method
  
    Load file of previously saved analysis results, or create the file with an empty list if the file doesn't exist

    input: none

    output: none

- view_saved method

    Display a list of the saved reports and display report that is selected by user

    input: none

    output: none

#### Dependencies

[Back To Top](#sentalysis)

- Python 3.8: This app was built using the latest version of Python at the time
- requests: Communicating with APIs
- python_dotenv: Loading environment variables
- os: Loading environment variables, reading and writing files
- mypy: Static type hinting in Python
- flake8: Style guide enforcement
- json: Work with json data and files

#### Flowchart

[Back To Top](#sentalysis)

![Flowchart](docs/flow.drawio.svg)

### Installation

[Back To Top](#sentalysis)

- Clone the GitHub repository into a folder in your development environment and enter the project directory.

- Create a new virtual environment using the following command, note that SentAlysis requires Python 3.8

    `python3.8 -m venv venv`

    If you do not have the venv module installed, run `pip install venv` - this command can change depending on what versions of pip you have installed on your system.

- Activate your virtual environment using the following command:

    `source venv/bin/activate`

- Install the dependencies using the following command:

    `pip install -r requirements.txt`

- In the project directory, create a new file called `.env`.

- Create an account on the [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard).

- Create a new app and get a Twitter Bearer Token, add the Bearer Token to your `.env` file as so:

    `BEARER_TOKEN=xxxxxxxxxxxxxxxxxx`

- Create an account on [Deep AI](https://deepai.org/dashboard/).

- Get your api-key from the profile page and add it to your `.env` file as so:

    `DEEP_API_KEY=xxxxxxxxxxxxxxxxxx`

- Now you're good to go! Open the app by running `python main.py`.

### Using SentAlysis

[Back To Top](#sentalysis)

There are three main ways to analyse text in SentAlysis:

- Type text directly into the terminal.
- Enter the path and/or filename of a text file which contains the text you want to analyse.
- Search Twitter and retrieve the latest tweets for any user, hashtag or search term.
  - To search for a user simply prefix the Twitter handle with '@' ie. '@twitter'.
  - Similarly, to search a hashtag, prefix the term with '#' ie. '#twitter'.
  - Anything apart from the previous examples are considered a generic search term.

After analysis using any of the methods, you have the option of saving the report if you would like to refer back to it later. SentAlysis will prompt you to give a name for the report, which is useful when loading the reports later for easier recognition.
