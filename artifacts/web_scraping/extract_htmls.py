import requests
import os


other_sites = {"Amazon Prime": "https://www.yaguara.co/amazon-prime-statistics/"}

zippia = {"Neflix": "https://www.zippia.com/netflix-careers-8010/revenue/",
         "Hulu": "https://www.zippia.com/hulu-careers-26793/revenue/",}

business_of_apps = {#"Disney+": "https://www.businessofapps.com/data/disney-plus-statistics/",
                    "Tubi": "https://www.businessofapps.com/data/tubi-statistics/",
                    #"Netflix": "https://www.businessofapps.com/data/netflix-statistics/",
                    "Prime Video": "https://www.businessofapps.com/data/amazon-prime-video-statistics/",
                    #"Hulu": "https://www.businessofapps.com/data/hulu-statistics/",
                    #"HBO Max": "https://www.businessofapps.com/data/hbo-max-statistics/",
                    #"Twitch": "https://www.businessofapps.com/data/twitch-statistics/",
                    "Youtube": "https://www.businessofapps.com/data/youtube-statistics/",
                    #"Apple TV+": "https://www.businessofapps.com/data/apple-statistics/",
                    }

if __name__ == "__main__":

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Connection": "keep-alive"
}
    # print("ZIPPIA")
    # for service in zippia:
    #     response = requests.get(zippia[service], headers=headers)

    #     try:
    #         html = response.text

    #         file_name = os.path.join("zippia", f"{service}.html")

    #         with open(file_name, "w", encoding="utf-8") as f:
    #             f.write(html)
            
    #         print(f"successfully extracted html from {service}")
    #     except Exception as e:
    #         print(f"failed to extract html from {service}. Error code: {e}")

    print("OTHER SITES")
    for service in other_sites:
        response = requests.get(other_sites[service], headers=headers)

        try:
            html = response.text

            file_name = os.path.join("other_sites", f"{service}.html")

            with open(file_name, "w", encoding="utf-8") as f:
                f.write(html)
            
            print(f"successfully extracted html from {service}")
        except Exception as e:
            print(f"failed to extract html from {service}. Error code: {e}")

    exit()

    for service in business_of_apps:
        response = requests.get(business_of_apps[service], headers=headers)

        try:
            html = response.text

            file_name = os.path.join("business_of_apps", f"{service}.html")

            with open(file_name, "w", encoding="utf-8") as f:
                f.write(html)
            
            print(f"successfully extracted html from {service}")
        except Exception as e:
            print(f"failed to extract html from {service}. Error code: {e}")
