from google import search

for url in search('"Breaking Code" Wordpress blog',stop=10):
	print(url)
