import requests

def send2server_jiang(ft_key, title, msg=None):
	data = {'text': title}
	if msg:
		data.update({'desp': msg})
	requests.get(f'https://sc.ftqq.com/{ft_key}.send', params=data)