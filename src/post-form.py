import requests

url = "https://docs.google.com/forms/d/e/1FAIpQLSd0aT6g3_SIG797M9B2JKKYdSK-MZ3pXu-K1iGNBvjW5Yal9g/formResponse"

submission = {"entry.1123972501": "python_teste2"}

print(submission)

sent = requests.post(url, data=submission)

if sent:
	print('Success')
else:
	print('An error has occurred.')
