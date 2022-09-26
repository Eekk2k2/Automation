import requests

url = "https://privatix-temp-mail-v1.p.rapidapi.com/request/one_attachment/id/%7Bmail_id%7D/%7BatId%7D/"

headers = {
	"X-RapidAPI-Key": "49750ce4d5mshaed91dc1542a8c0p1d4260jsn0d552377ac1e",
	"X-RapidAPI-Host": "privatix-temp-mail-v1.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)

print(response.text)