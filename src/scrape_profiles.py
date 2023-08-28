import argparse

from selenium.common.exceptions import WebDriverException

from generate_csv import write_to_csv
from linkedin_utils import *

from loginHandle import *



def main(argument):
    driver = get_chrome_driver()
    try:
        login_user(argument, driver)
        profile_urls = get_urls_of_group_members(argument.group_ids, driver)

        # Temp
        # Comment out this code if group has more then 20 members and you want all members
        # Navigate to members page of group
        # Open devtools of chrome
        # Execute Following commands:

        # ```
        # xpaths = $x('//a[@data-control-name="view_profile"]')
        # urls = []
        # for (i=0; i<=urls.length; i++) {
        #     urls.push(urls[i].href);
        # }
        # copy(urls)
        # ```

        # Replace the following array and comment out the `get_urls_of_group_members` calling
        # profile_urls = [
        #     "https://www.linkedin.com/in/faqir-aamir-55141639/",
        #     "https://www.linkedin.com/in/aamiriftikharahmed/",
        # ]

        members = list()
        i=0
        if i<3:
            for profile_url in profile_urls:
                member = scrape_profiles(driver, profile_url)
                members.append(member)
                sleep(0.5)
                i+=1
            
        
    except WebDriverException:
        pass
    finally:
        driver.close()

    write_to_csv(members)


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Scrape LinkedIn Profiles and save them as CSV File of given URLs')
    arg_parser.add_argument('--email', help='Enter your LinkedIn email, which account belongs to specific group')
    arg_parser.add_argument('--password', help='Enter your LinkedIn password')
    arg_parser.add_argument('--group_ids',
                            help='Enter id of of Group of which you want to get profiles data, comma separated')
    arguments = arg_parser.parse_args()

    main(arguments)
