import os
import time
import hashlib
import requests


sleep_time = 2.5
url_address = "https://outpostclimbing.sg/"
# url_address = "https://outpostclimbing.sg/package"
# url_address = "https://www.instagram.com/outpostclimbing/"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Pragma": "no-cache",
    "Cache-Control": "no-cache",
}

# response = requests.get(URL_TO_MONITOR, headers=headers)


# response_ref = requests.get(url_address)
# print(f"{r.status_code=}")
# print(f"{r.headers['content-type']=}")
# print(f"{r.encoding=}")
# print(f"{r.text=}")

records = [
    "1da9dc825d168140fbdbff499c27cff1e25fca8ceb0016b6b1334836a973dffd",  ## Package page #1
    "d5517c75aa9794dfef23627d9c6e516875b29f1e27fb55ca65ecd58a5f7f7ea5",  ## Package page #2
    "da597c673fc111a201097840bde44150720fa50a670bd8e3f5d985f5145b857f",  ## Home #1
    "0ac602328e79004e9846eb3fd8200ef933a2cdaf4e038755f3a152bf74ce936f",  ## Home #2
    "228451a78bc42aa8fb10800c54f4a2d72c1936d13884aa9e56b6dfee1f116170",  ## Home #3
    "e1100916d614ac26ba6fa6c6d5680c55344de1f90e7f22c85a7386a619be4101",  ## Home #4
    "118dfc01bf1e8197ff45ed97b9b813a1c199c7eb546e93ff63226329bee2656f",  ## Home #5
]


def notify(title, text):
    # os.system(f"""osascript -e 'display notification "{text}" with title "{title}"'""")
    # os.system("""afplay '/System/Library/Sounds/Hero.aiff'""")
    pass


while True:
    r = requests.get(url_address, headers=headers)
    h = hashlib.new("sha256")
    h.update(r.content)
    hashcode = h.hexdigest()
    is_changed = hashcode not in records
    if is_changed:
        print(f"CHANGED!!! - {hashcode=}")
        notify("Title", "Heres an alert")
    else:
        print(f"nope. alls good {hashcode=}")
    time.sleep(sleep_time)
