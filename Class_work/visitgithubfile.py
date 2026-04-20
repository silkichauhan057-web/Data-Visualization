import urllib.request

url = "https://raw.githubusercontent.com/silkichauhan057-web/Task2/main/import%20java.util.scanner%3B.txt"

data = urllib.request.urlopen(url)

print(data.read().decode())