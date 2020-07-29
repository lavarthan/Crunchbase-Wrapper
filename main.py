import json
import time
import random
from ulits import get_name, get_social_medias, get_details, get_about, get_soup, get_highlights, get_short_description
from ulits import get_suggestion, get_website, get_brief_description, get_image


while True:
    company = input("if you have the exact organization name Type here or Just press Enter")
    if company == '':
        url = input("Enter URL:").split('.')[1]
        company = input("Enter company")

        search_result = get_suggestion(company)
        result = {}
        for i in search_result:
            soup = get_soup(i)
            if get_website(soup).split('.')[1] == url:
                result.update(get_about(soup))
                try:
                    result.update(get_name(soup))
                except:
                    pass
                try:
                    result.update(get_about(soup))
                except:
                    pass

                try:
                    result.update(get_short_description(soup))
                except:
                    print("No short description found")
                    pass

                try:
                    result.update(get_highlights(soup))
                except:
                    pass

                try:
                    result.update(get_details(soup))
                except:
                    pass

                try:
                    result.update(get_brief_description(soup))
                except:
                    print("no brief description found")
                    pass
                try:
                    result.update(get_image(soup))
                except:
                    print("No logo image found")
                    pass

                try:
                    result.update(get_social_medias(soup))
                except:
                    pass
                break
            time.sleep(random.randint(5, 10))


        else:
            print("Company not found!")


    else:
        result = {}
        soup = get_soup(company)

        try:
            result.update(get_about(soup))
        except:
            print('some thing went wrong!')
            # break

        try:
            result.update(get_name(soup))
        except:
            pass

        try:
            result.update(get_short_description(soup))
        except:
            print("No short description found")
            pass

        try:
            result.update(get_highlights(soup))
        except:
            pass

        try:
            result.update(get_details(soup))
        except:
            pass

        try:
            result.update(get_brief_description(soup))
        except:
            print("no brief description found")
            pass


        try:
            result.update(get_image(soup))
        except:
            print("No logo image found")
            pass

        try:
            result.update(get_social_medias(soup))
        except:
            pass

    file_name = result['Name']
    with open('Company/'+file_name+'.json', 'w') as f:
        json.dump(result, f, indent=4, separators=(',', ': '))
