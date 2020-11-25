import webbrowser as wb


def web_auto():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
    URLs = (
        'linkedin.com/in/akshitone/',
        'github.com/akshitone/',
        'youtube.com/'
    )
    for url in URLs:
        print("opening... ", url)
        wb.get(chrome_path).open(url)


web_auto()
