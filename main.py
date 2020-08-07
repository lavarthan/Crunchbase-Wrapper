import json
import time
import random
from ulits import get_name, get_social_medias, get_details, get_about, get_highlights, get_short_description
from ulits import get_suggestion, get_website, get_brief_description, get_image
from ulits import get_soup, get_financial_details

while True:
    try:
        company = input("if you have the exact organization name Type here or Just press Enter")
        if company == '':
            url = input("Enter URL:").split('.')[1]
            company = input("Enter company")

            search_result = get_suggestion(company)
            result = {}
            for i in search_result:
                soup1, soup2 = get_soup(i)
                if get_website(soup1).split('.')[1] == url:
                    result.update(get_about(soup1))
                    try:
                        result.update(get_name(soup1))
                    except:
                        pass
                    try:
                        result.update(get_about(soup1))
                    except:
                        pass

                    try:
                        result.update(get_short_description(soup1))
                    except:
                        print("No short description found")
                        pass

                    try:
                        result.update(get_highlights(soup1))
                    except:
                        pass

                    try:
                        result.update(get_details(soup1))
                    except:
                        pass

                    try:
                        result.update(get_brief_description(soup1))
                    except:
                        print("no brief description found")
                        pass
                    try:
                        result.update(get_image(soup1))
                    except:
                        print("No logo image found")
                        pass

                    try:
                        result.update(get_social_medias(soup1))
                    except:
                        pass

                    try:
                        result.update(get_financial_details(soup2))
                    except:
                        pass

                    break
                time.sleep(random.randint(2, 4))


            else:
                print("Company not found!")


        else:
            result = {}
            soup1, soup2 = get_soup(company)

            try:
                result.update(get_about(soup1))
            except:
                print('some thing went wrong!')
                # break

            try:
                result.update(get_name(soup1))
            except:
                pass

            try:
                result.update(get_short_description(soup1))
            except:
                print("No short description found")
                pass

            try:
                result.update(get_highlights(soup1))
            except:
                pass

            try:
                result.update(get_details(soup1))
            except:
                pass

            try:
                result.update(get_brief_description(soup1))
            except:
                print("no brief description found")
                pass

            try:
                result.update(get_image(soup1))
            except:
                print("No logo image found")
                pass

            try:
                result.update(get_social_medias(soup1))
            except:
                pass

            try:
                result.update(get_financial_details(soup2))
            except:
                pass

        file_name = result['Name']
        with open('Company/' + file_name + '.json', 'w') as f:
            json.dump(result, f, indent=4, separators=(',', ': '))
    except:
        print("Something went wrong. \n1. Check your internet connection\n2. check the url is valid or not")
