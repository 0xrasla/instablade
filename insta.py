import requests, json
from bs4 import BeautifulSoup

def video_downloader(url, video_name):
    try:
        r = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
        soup = BeautifulSoup(r.content, 'html.parser')
        video_link = soup.find("meta", property="og:video")['content']

        v_soup = requests.get(video_link, headers={'User-agent': 'your bot 0.1'})

        with open(str(video_name) + '.mp4', 'wb') as f: 
                for chunk in v_soup.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk)
        print("Downloading success!")

    except Exception as e:
        print("Try AGain BrO......enna nadakunu thrla")
        print(e)

def picture_download(url, pic_name):
    r = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
    soup = BeautifulSoup(r.content, 'html.parser')
    pic_link = soup.find("meta", property="og:image")['content']

    v_soup = requests.get(pic_link, headers={'User-agent': 'your bot 0.1'})
    with open(str(pic_name) + '.jpg', 'wb') as f: 
        for chunk in v_soup.iter_content(chunk_size = 1024*1024): 
            if chunk: 
                f.write(chunk)

if __name__ == "__main__":
    print("""What You want to download ?
            a: Insta video download
            b: Insta image download
    """ )
    option = input()
    if str(option).strip() == 'a':
        url = input('ENTer tHe Video uRl Makka ==> ')
        video_name = input('ENter how to save your Videoname ==> ')
        video_downloader(url.strip(), video_name)
        print("Maklae Download Success....")
    elif str(option).strip() == 'b':
        url = input('ENTer tHe Image uRl Makka ==> ')
        image_name = input('ENter how to save your Image ==> ')
        picture_download(url.strip(), image_name)
        print("Maklae Download Success....")
