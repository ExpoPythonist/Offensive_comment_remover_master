# Overall Description
The application will remove the negative comments from posts and ads in pages, using Graph API and sentiment analysis. 
Graph API

The app used facebook’s graph API for the following
* Fetch User Token on Login
* Fetch Group List and Group Access Token
* Fetch comments from Posts
* Delete comment
* Sentiment Analysis
  * Returns if the comment is negative or not
  
# Functionality Description
The app is built on top of the Django framework, which handles the backend for the API. The complete backend of the app is built as an API. The app contains mainly 3 modules
* Graph API
* Comment Manager
* Sentiment Analyser
## API
The working of app is basically, when a signal for starting sentiment analysis is recieved, the backend will add the comment_manager.py file with commandline arguments as access_token and page id to the system Cron Job, with 2 minutes as runtime gap.

When a signal to stop is received, the corresponding command will be removed from the cron job.

## Description based on Django Modules
The app contains 3 django modules named,
* api
* Modules
* frontend

### API
API module handles all the api calls.
* sentiment_analysis
Api request will turn sentiment analyzer on or off
* ad_only
Updates db for ad only analysis
* fetch_pages
Returns pages of current user
* add_pages
Page selection - Add page for sentiment analysis
* flip_page_selection
Page selection - Select and diselects pages
* register
Register user

### Modules

Modules has 3 main functions
* Handles facebook graph api
* Encrtption
* Comment Manager

#### Graph Api
Handles requests to graph api with parameters. The file graphapi.py is self explanatory with all classes and functions commented with description.
#### Encryption
Used for encryption and decryption of password
#### Comment Manager
Commen_manager.py file will use facebook/graphapi.py file and fetch the comments from the facebook posts and send to sentiment analyzer function.
The function will returns whether the comment is negative or not, if negative then the comment will be removed.

## System Requirements
| Key | Value |
| --- | --- |
| Server Os | Linux (Ubuntu) |
| Language | Python3 |
| Platform | Django |
| Database | MySQL |

# Database details
`The database details are given in the modules/models.py`

# Installation and Configuration
## Facebook Config
1. Create and app on developer.facebook.com
2. Complete the required steps and add the details needed
3. On permission for application list add
    * manage_pages
    * pages_show_list
    * publish_pages
4. Configure facebook login
    * Click on facebook login in products from left sidebar
    * Click on Settings
        * Add localhost to Valid OAuth Redirect URIs
            * It is also better to add 127.0.0.1:8000 also
5. Goto facebook.com
6. Create a facebook page for testing
    
  
## Django app Config
1. Install mariadb server and client.
    * Sudo apt install mariadb-server mariadb-client
2. Install python3 mysqldb
    * sudo apt install python3-mysqldb
3. Run pip3 install -r requirements.py to install the python requirements
    * Install requiremnts system wide as programs outside django will be using the above reqs
4. Add the mysql username, password and database name to following files
    * modules/config.json
    * My.cnf
5. Import elio_off_com_rem.sql file into database
6. Update the app_id and app_secret to the app_details table

# Testing the app
1. Run the app using python3 manager.py runserver
2. Goto localhost:8000/signup
    * Signup by filling the details
3. Signup you will be redirected to the facebook auth page
4. Click on Facebook login button
5. Which will redirect to select pages page
6. Select the required page
7. Click on next and will be redirected to the dashboard

In the backend the crontab for sentiment analysis would be started.

To test it create a post in the page and add a good and bad comment and wait for like 3 minutes and refresh the page.
