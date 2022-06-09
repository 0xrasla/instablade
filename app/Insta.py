import requests, json

def video_downloader(url, video_name):
    
    try:
        print("Downloading video...")
        _id = url.split("https://www.instagram.com/")[1].split("/")[1]

        response = requests.get("https://www.instagram.com/p/{}/?__a=1".format(_id), headers={'User-agent': 'your bot 0.1'})
        
        with open("res.json", "w") as f:
            json.dump(response.json(), f)

        video_link = response.json()['graphql']['shortcode_media']['video_url']

        r = requests.get(video_link, headers={'User-agent': 'your bot 0.1'})
        _video_name = video_name + str(_id)+ ".mp4"

        with open("app/" + _video_name , 'wb') as f: 
                for chunk in r.iter_content(chunk_size = 1024*1024): 
                    if chunk: 
                        f.write(chunk)
        return _video_name

    except Exception as e:
        return "Something Went Wrong! " + str(e)

def picture_download(url, pic_name):
    try:
        print("Downloading picture...")
        _id = url.split("https://www.instagram.com/")[1].split("/")[1]

        response = requests.get("https://www.instagram.com/p/{}/?__a=1".format(_id), headers={'User-agent': 'your bot 0.1'})

        with open("res.json", "w") as f:
            json.dump(response.json(), f)

        pic_link = response.json()['graphql']['shortcode_media']['display_url']

        r = requests.get(pic_link, headers={'User-agent': 'your bot 0.1'})
        _pic_name = pic_name + str(_id)+ ".jpg"

        with open("app/" + _pic_name , 'wb') as f:
            for chunk in r.iter_content(chunk_size = 1024*1024):
                if chunk:
                    f.write(chunk)
        return pic_name + str(_id) + ".jpg"

    except Exception as e:
        return "Something Went Wrong! " + str(e)
