import requests

file = {'uploadFile': open('./timg.jpeg', 'rb')}
r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
print(r.text)

# The file image.png has been uploaded.
