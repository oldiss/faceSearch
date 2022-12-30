#Python program to scrape website
#and save quotes from website
import requests
from bs4 import BeautifulSoup
from download import downloadPic
import  cv2
import os,glob

parent_dir = './all'
parent_dir_with_dash = parent_dir + '/'
sucFaces = [os.path.basename(f) for f in glob.glob(os.path.join(parent_dir, '*.jpg'))]

def runTest():
    try:
        fails = 0
        failNameList = []
        import csv
        for k in range (99,123):
            for j in range(1,67):
                try:
                    preUrl = ('https://fappeningbook.com/browse/' + chr(k) + '/' + str(j) + '/')
                    URL = preUrl
                    r = requests.get(URL)
                    names = []

                    soup = BeautifulSoup(r.content, 'html.parser')
                    res = soup.find_all('a')

                    table = soup.find_all('div', attrs = {'class':'models-previews-dv'})
                    #print(table)
                    name = ''
                    for row in table:
                        if True:
                            name = (row.text).replace(' ', '-')

                            #print(name)
                            print('\n')
                            #print(names)
                    names = name.split()
                    #print(names)
                    firstletter = ((names[0]).replace('-', '').replace('.','')[0]).lower()
                    secondLetter = ((names[0]).replace('-', '').replace('.','')[1]).lower()

                    for i in range(100):
                        print('page: ' + str(j) + 'id: ' + str(i) )
                        firstletter = ((names[i]).replace('-', '')[0]).lower()
                        secondLetter = ((names[i]).replace('-', '')[1]).lower()
                        try:
                            if(sucFaces.__contains__(names[i])):
                                pass
                            else:
                                downloadPic(names[i].replace('.','').lower() , str(firstletter), str(secondLetter),'./failedFaces/')
                                print(fails)
                                print(chr(k))
                            
                            print( failNameList)
                        except(FileNotFoundError,OSError):
                            failNameList.append(names[i])
                            fails = fails + 1 
                            pass
                except(IndexError):
                    pass
                print(firstletter)
                print(secondLetter)
            print(fails)
            
    except(NameError):
        print('name error')



