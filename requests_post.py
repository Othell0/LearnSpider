import requests

data = {'firstname': 'othell0', 'lastname': 'cs'}
r = requests.post('http://pythonscraping.com/pages/files/processing.php', data)
print(r.text)
