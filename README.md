# MessengerAnalyser
Python App to analyse chats from Facebook Messenger.
Utilises Beautiful Soup to scrape html
Utilises Pandas for data analysis (poorly currently!) 

## Instructions
### Facebooky Stuff
1. Login to your Facebook Account on your computer
2. Go to the top right hand of the screen, and click the down arrow
3. On the down arrow, click Settings
4. On the left hand side, click the **"Your Facebook Information"** tab
5. Click *"View"* for **"Download Your Information"** - this is your Facebook download page
6. To speed things up, you only want to download your messages, therefore hit *"Deselect All"* on the right hand side above the list, and select only **"Messages"**
7. Select an appropriate timeframe (mileage will vary if you have a lot of messages to download), HTML and Medium as your three options, then click *"Create File"*
8. Facebook will then accumulate your message data for download - be warned if you have a lot of messages this can take days, so choose your time period appropriately
9. Once Facebook is done accumulating your information, it will send you a notification. Either select this notification, or navigate back to your Facebook Download page and click the **"Available Files"** tab. 
10. Select your newly created file and click *"Download"*

### File Handling Stuff
1. Once the download is complete, you'll want to decompress the file using the unzipper of your choice, and it should then contain a folder called *"messages"*.
2. Inside this messages folder, go to the *"inbox"* folder. 
**TODO:** Continue writing instructions from here once automatic process for file selection is implemented! Plan is to have a messages folder for User to copy the conversation they want into a messages folder. Index file will then take the latest value available, rather than having to hack the file. 
