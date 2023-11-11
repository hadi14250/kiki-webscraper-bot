import requests
import threading
import time
from requests.exceptions import RequestException, ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError


def make_request(payload, flag):
    try:
        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=('hadi14250', '05590560352Hk200018'), #Your credentials go here
            json=payload,
        )
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
        if (flag == "twitterProfile"):
            with open('twitterProfile.html', 'wb') as f:
                f.write(response.content)
        elif (flag == "tweet"):
            with open('tweet.html', 'wb') as f:
                f.write(response.content)
        elif (flag == "instagramProfile"):
            with open('instagramProfile.html', 'wb') as f:
                f.write(response.content)
        elif (flag == "instagramPost"):
            with open('instagramPost.html', 'wb') as f:
                f.write(response.content)
        elif (flag == "tiktokProfile"):
            with open('tiktokProfile.html', 'wb') as f:
                f.write(response.content)
        elif (flag == "tiktokPost"):
            with open('tiktokPost.html', 'wb') as f:
                f.write(response.content)
    except (ConnectionError, HTTPError, Timeout, TooManyRedirects, SSLError, RequestException) as e:
        print(f"An error occurred: {e}")



twitterHandle = "ordinalHO"
twitterSession = "?t=jkhlbh&s=04"
url = "https://x.com/{}{}".format(twitterHandle, twitterSession)

twitterProfilePayload = {
    "source": "universal",
    "url": "https://x.com/{}{}".format(twitterHandle, twitterSession),
    "render": "html",
}

tweetPayload = {
    "source": "universal",
    "url": "https://twitter.com/billyrestey/status/1723108332591030474?t=jqnZFH3KytAI1zwsOJyU-A&s=19",
    "render": "html",
}

instagramProfilePayload = {
    "source": "universal",
    "url": "https://www.instagram.com/pubity/",
    "render": "html",
}

instagramPostPayload = {
    "source": "universal",
    "url": "https://www.instagram.com/p/CzTWqUWLLvJ/",
    "render": "html",
}

tiktokProfilePayload = {
    "source": "universal",
    "url": "https://www.tiktok.com/@thezachchoi",
    "render": "html",
}

tiktokPostPayload = {
    "source": "universal",
    "url": "https://www.tiktok.com/@thezachchoi/video/7298038955348397354",
    "render": "html",
}

thread1 = threading.Thread(target=make_request, args=(twitterProfilePayload, "twitterProfile"))
time.sleep(0.5)
thread2 = threading.Thread(target=make_request, args=(tweetPayload, "tweet"))
time.sleep(0.5)
thread3 = threading.Thread(target=make_request, args=(instagramProfilePayload, "instagramProfile"))
time.sleep(0.5)
thread4 = threading.Thread(target=make_request, args=(instagramPostPayload, "instagramPost"))
time.sleep(0.5)
thread5 = threading.Thread(target=make_request, args=(tiktokProfilePayload, "tiktokProfile"))
time.sleep(0.5)
thread6 = threading.Thread(target=make_request, args=(tiktokPostPayload, "tiktokPost"))

# Start the threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()


# Wait for both threads to finish
thread1.join()
thread2.join()
thread3.join()
thread4.join()
thread5.join()
thread6.join()

