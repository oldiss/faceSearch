import requests

def downloadPic(name, firstLetter,secondLetter,directory):
        imgUrl = ('https://fappeningbook.com/avatars/' + firstLetter + '/' + secondLetter + '/' + name + '/avatar.jpg')
        print(imgUrl)
        img_data = requests.get(imgUrl).content 
        filename = directory + name + '.jpg'
        with open(filename, 'wb') as handler: 

            handler.write(img_data)

#downloadPic('aj-alexander' , 'a', 'j')