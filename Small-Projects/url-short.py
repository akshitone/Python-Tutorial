import pyshorteners

url = input("Enter URL: ")

print("Your short URL --> " + pyshorteners.Shortener().tinyurl.short(url))
