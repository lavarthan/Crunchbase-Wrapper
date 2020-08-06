# import appropriate libraries
import re
import random
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def get_suggestion(query):
    """
    :param query: the search key word
    :return: first five results for the search query

    """
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # adding user agent to prevent blocked permanently
    UserAgents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 "
        "Safari/537.36",
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 '
        'Safari/534.57.2',
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"]
    user_agent = UserAgents[random.randint(0, 8)]
    options.add_argument("--user=%s" % user_agent)
    # if you don't want to open the browser uncomment the below line
    # options.headless = True
    d = webdriver.Chrome(options=options, executable_path='chromedriver')
    wait = WebDriverWait(d, 10)
    d.get('https://www.crunchbase.com/home')

    # wait until the search bar loaded
    wait.until(EC.visibility_of_element_located((By.ID, "mat-input-0")))
    try:
        # type and send the search key word
        e = d.find_element_by_id('mat-input-0')
        e.click()
        e.send_keys(query)

        # wait until the 'SHOW MORE' button load
        wait.until(EC.visibility_of_element_located((By.XPATH,
                                                     "//search-results-section[@class='ng-star-inserted']//span[@class='mat-button-wrapper'][contains(text(),'Show More')]")))
        # click on the 'SHOW MORE' button
        btn = d.find_element_by_xpath(
            '/html[1]/body[1]/chrome[1]/div[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/div['
            '1]/multi-search-results[1]/page-layout[1]/div[1]/div[1]/div[1]/div[1]/search-results-section[1]/mat-card['
            '1]/div[1]/button[1]/span[1]')
        btn.click()

        # scrape the whole page
        content = d.page_source
        soup = BeautifulSoup(''.join(content), 'html.parser')
        result = [i['href'].split('/')[-1] for i in soup.find_all('a', attrs={
            'class': 'row-anchor cb-padding-medium-horizontal flex layout-row layout-align-start-center '
                     'cb-text-color-medium ng-star-inserted'})[0:5]]

        d.quit()
        return result
    except:
        print("something wrong")
        d.quit()


def get_soup(query):
    """
    :param query: organization name
    :return: soup for the company name

    """
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    # if you don't want to open the browser uncomment the below line
    # options.headless = True

    # adding user agent to prevent blocked permanently
    UserAgents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 "
        "Safari/537.36",
        'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:23.0) Gecko/20100101 Firefox/23.0',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0)',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
        'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140205 Firefox/24.0 Iceweasel/24.3.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
        'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:28.0) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 '
        'Safari/534.57.2',
        "Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"]
    user_agent = UserAgents[random.randint(0, 8)]
    options.add_argument("--user-agent=%s" % user_agent)

    d = webdriver.Chrome(options=options, executable_path='chromedriver')
    d.get('https://www.crunchbase.com/organization/' + query)

    try:
        wait(d, 40).until(
            EC.presence_of_element_located((By.XPATH, '//identifier-image[@class=\'ng-star-inserted\']//img')))
        # press the load more button to get the full description
        wait(d, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),\'Read More\')]')))
        btn = d.find_element_by_xpath('//a[contains(text(),\'Read More\')]').click()
        # btn.click()
        content = d.page_source
        soup = BeautifulSoup(''.join(content), 'html.parser')
    except:
        print("lets passes the captcha")
        pass
    sleep(5)
    content = d.page_source
    soup = BeautifulSoup(''.join(content), 'html.parser')

    # content = d.page_source
    # soup = BeautifulSoup(''.join(content), 'html.parser')

    # by pass the captcha if get blocked by clicking and holding the captcha button
    if soup.find('title').text == 'Access to this page has been denied.':
        action = ActionChains(d)
        element = d.find_element_by_id('px-captcha').location
        x = element['x']
        y = element['y']
        action.move_by_offset(x, y)
        action.click_and_hold().perform()
        sleep(4)
        action.reset_actions()

        # wait until page fully loaded
        try:
            wait(d, 40).until(
                EC.presence_of_element_located((By.XPATH, '//identifier-image[@class=\'ng-star-inserted\']//img')))
            # wait(d, 20).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),\'Read More\')]')))
            btn = d.find_element_by_xpath('//a[contains(text(),\'Read More\')]').click()
            # btn.click()
            content = d.page_source
            soup = BeautifulSoup(''.join(content), 'html.parser')
        except:
            pass
        # try:
        #     # press the load more button to get the full description
        #     wait(d, 20).until(EC.presence_of_element_located((By.XPATH, '//a[contains(text(),\'Read More\')]')))
        #     btn = d.find_element_by_xpath('//a[contains(text(),\'Read More\')]').click()
        #     # btn.click()
        #     content = d.page_source
        #     soup = BeautifulSoup(''.join(content), 'html.parser')
        # except:
        #     print('no read more')
        #     pass
        # content = d.page_source
        # soup = BeautifulSoup(''.join(content), 'html.parser')
    d.quit()
    return soup


def get_brief_description(soup):
    """
    :param soup: soup of the company
    :return: brief description as a dictionary

    """
    p_tag = soup.find_all('description-card')[1].find_all('p')
    return {'Brief_description': ' '.join([i.text for i in p_tag])}


def get_image(soup):
    """
    :param soup: soup of the company
    :return: company logo url as a dictionary

    """
    return {'Logo': soup.find('img', attrs={'style': 'opacity: 1;'})['src']}


def get_website(soup):
    """
    :param soup: soup of the company
    :return: website url if available

    """
    try:
        return get_about(soup)['Website']
    except:
        print("No website URL found")


def get_short_description(soup):
    """
    :param soup: soup of the company
    :return: short description as a dictionary

    """
    return {'short description': soup.find('description-card').text}


def get_highlights(soup):
    """
    :param soup: soup of the company
    :return: all details under 'Highlights' field as a dictionary

    """
    result = soup.find('anchored-values').find_all('a')
    result = [i.text.split('\xa0') for i in result]
    final = {}
    for i in result:
        final[i[0]] = i[1]
    return final


def get_about(soup):
    """
    :param soup: soup of the company
    :return: all details under 'About' field

    """
    values = [i.text for i in soup.find('ul', attrs={'class': 'icon_and_value'}).find_all('li')]
    keys = [i.text for i in soup.find('div', attrs={'id': 'cdk-describedby-message-container'}).find_all('div')]
    final = {}
    for i in range(len(values)):
        final[keys[i]] = values[i]
    return final


def get_details(soup):
    """
    :param soup: soup of the company
    :return: all details under 'Details' field

    """
    ul = soup.find_all('ul', attrs={'class': 'text_and_value'})
    results = []
    for i in ul:
        results += [j.text for j in i.find_all('li')]

    keys = [i.split('\xa0')[0] for i in results]
    values = [i.split('\xa0')[1] for i in results]
    final = {}
    for i in range(len(keys)):
        if keys[i] == 'Industries':
            final[keys[i]] = re.sub(r'([a-z](?=[A-Z])|[A-Z](?=[A-Z][a-z]))', r'\1,', values[i])
        else:
            final[keys[i]] = values[i]
    return final


def get_social_medias(soup):
    """
    :param soup: soup of the company
    :return: company social media links as dictionary

    """
    keys = [i['title'].split(' ')[-1] for i in soup.find('ul', attrs={'class': 'icon'}).find_all('a')]
    values = [i['href'] for i in soup.find('ul', attrs={'class': 'icon'}).find_all('a')]
    final = {}

    for i in range(len(keys)):
        final[keys[i]] = values[i]
    return final


def get_name(soup):
    """
    :param soup: soup of the company
    :return: company name as a dictionary

    """
    return {'Name': soup.find('h1').text}
