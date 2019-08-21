import os
import cfscrape # Anti CloudFlare
from bs4 import BeautifulSoup
from urllib import parse


######################### GENERAL VARS ############################

TYPES_FILE  = 'anime_types.txt'                             #List of types
SCRAPER     = cfscrape.create_scraper()                     #INIT
CLEAR       = lambda : os.system('clear')                     #Clear console
ANIME_TYPES = []                                            #this will have all types
MAIN_LINK   = 'https://animelek.net/'                       #Main Website URL
GENRE_LINK  = 'https://animelek.net/genre/'                 #add type
MAIN_PATH   =  os.path.abspath(os.path.dirname(__file__))   #CHECK FILE

###################################################################

def StartPlease():
    CLEAR()
    hello = '''
    #########################################################
    ##   M  A  D  E     -      B  Y      -    5  4  4  D   ##
    #########################################################
    ##           ARE YOU SURE YOU WANNA START ?            ##
    #########################################################
    
    # y = yes
    # n = no
    '''
    print(hello)
    r = input('')
    if r != 'y' :
        exit()

def getBytes(string,encoding='utf-8'):
    return bytes(string,encoding)
    
def GetFile(fname,mode='w+'):
    return open(fname,mode)

def getSoup(link,scraper=SCRAPER):
    _html = scraper.get(link).content
    CLEAR()
    return BeautifulSoup(_html)


# THIS WILL SCRAP THE MENUE LIST 
def scrapGenres(FileToWrite=None, scraper=SCRAPER,main_link=MAIN_LINK):   
    soup = getSoup(main_link)
    for a in (soup.findChildren('ul')[0]).find_all('a'):
        if ('/genre/' in a['href']) :
            ANIME_TYPES.append((str(a['href']).replace(GENRE_LINK,'')).replace('/',''))
    for t in ANIME_TYPES:
        FileToWrite.write(t+'\n')
    FileToWrite.close()


#THIS WILL SAVE SCRAPED MENU TO A FILE TO FILL ANIME_TYPES[] LATER WITHOUT ANY SCRAPPING
#ALSO WILL FILL ANIME_TYPES[] EITHER THE FILE ALREADY EXISTS OR NOT 
def getAnimeTypes(filename=TYPES_FILE):
    StartPlease()
    if os.path.isfile(filename) :
        of = open(filename,'r')
        for t in of.readlines():
            ANIME_TYPES.append(t.replace('\n',''))
        of.close()
        if len(ANIME_TYPES) >= 1 :
            print("LOADED "+str(len(ANIME_TYPES))+" ANIME TYPES SUCCESSFULLY !")
        else :
            scrapGenres(FileToWrite=open(filename,'w+'))
            print("SCRAPED , SAVED AND LOADED "+str(len(ANIME_TYPES))+" ANIME TYPES SUCCESSFULY !")
    else:
        scrapGenres(FileToWrite=open(filename,'w+'))
        print("SCRAPED , SAVED AND LOADED SUCCESSFULY !")
    

