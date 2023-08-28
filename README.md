# LinkedIn Group Scrapper
This script will scrape the Profile of users from the groups.

### Project Setup
* Download and install Git - [Official Download Link](https://git-scm.com/downloads)
* Install Python 3 - [Official Download Link](https://www.python.org/downloads/)
```bash
# Clone the Project
git clone https://github.com/ThanhNguyen03/Scrape_memIn4_in_LinkedInGroup.git
# Get into project directory
cd linkedin-profile-scrapper
# Make Virtual Env with python 3
python3 -m venv
# Activate Virtual Env
source venv/bin/activate
# Install requirements
pip install -r requirements.txt
# Update WebDriver
pip install webdriver-manager
``` 

### Scrape
Run with command
```bash
python src/scrape_profiles.py --email=enteryouremail --password=enteryourpassword --group_ids=entergroupid 
```

### Common Issues
Make sure you have compatible chrome driver version with installed chrome on your machine.
Link to Driver is [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)


### Known Issues:
* Initial 20 members of groups are going to scrape (Scroll pagination is pending)
* Generate separate file for each group
* Add option to don't scrape already scraped profiles
