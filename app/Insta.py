import requests, json
from bs4 import BeautifulSoup


def video_downloader(url, video_name):
    
    try:
        print("Downloading video...")
        r = requests.get(url, headers = {'User-agent': 'your bot 0.1'})

        soup = BeautifulSoup(r.content, 'html.parser')
        _id = soup.find("link", hreflang="en")['href'].split("next=/reel/")[1].split("/&hl=en")[0]

        response = requests.get("https://www.instagram.com/p/{}/?__a=1".format(_id), headers={'User-agent': 'your bot 0.1'})
        
        # with open("res.json", "w") as f:
        #     json.dump(response.json(), f)

        video_link = response.json()['graphql']['shortcode_media']['video_url']

        r = requests.get(video_link, headers={'User-agent': 'your bot 0.1'})

        with open(str(video_name) + '.mp4', 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk)
        return "Downloading success!"

    except Exception as e:
        return "Something Went Wrong! " + str(e)

def picture_download(url, pic_name):
    r = requests.get(url, headers = {'User-agent': 'your bot 0.1'})

    soup = BeautifulSoup(r.content, 'html.parser')
    _id = soup.find("link", hreflang="en")['href'].split("https://www.instagram.com/accounts/login/?next=/p/")[1].split("/&hl=en")[0]

    print(_id)
    # response = requests.get("https://www.instagram.com/p/{}/?__a=1".format(_id), headers={'User-agent': 'your bot 0.1'})
        
    # with open("res.json", "w") as f:
    #     json.dump(response.json(), f)

    # pic_link = response.json()['graphql']['shortcode_media']['display_url']
    # v_soup = requests.get(pic_link, headers={'User-agent': 'your bot 0.1'})
    # with open(str(pic_name) + '.jpg', 'wb') as f: 
    #     for chunk in v_soup.iter_content(chunk_size = 1024*1024): 
    #         if chunk: 
    #             f.write(chunk)
