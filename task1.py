import requests
import bs4

# input url from user
url = input("Enter the url: ")
response = requests.get(url)
# print(response)
soup = bs4.BeautifulSoup(response.text,"html.parser")
# print(soup.text)

formatted_text = soup.prettify()
# print(formatted_text)

filename= "myfile.html"

with open(filename,"w+") as f:
    f.write(formatted_text)

#find number of images
list_images = soup.find_all("img")
no_img = len(list_images)
print("number of images: ",no_img)

#find number of anchor tages
list_as = soup.find_all("a")
no_as = len(list_as)
print("number of anchor tags: ",no_as)