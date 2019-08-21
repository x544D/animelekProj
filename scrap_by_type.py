from scrap_me import *


#title,animePageLink,pageNum,coverLink,yearProd,rates,types,story
#############################################################################################
#THIS COLLECTION SHOULD BE FILLED AFTER EVERY SINGLE ANIME AND ITS EPISODES ARE SCRAPED !   #
_COLLECTION_BY_TYPE = dict(zip(ANIME_TYPES, str(range(len(ANIME_TYPES)))))                  #
#############################################################################################

MAX_NUMBER_PAGES = 101 # means 100

SAVE_DATA_FILE_NAME = 'animes_data.txt' 

########################################################################################################################
# dictionary : {title[KEY] : LIST [ animeLinkPage > PageNumber > cover > year > rates > list[types] > short story]}   ##
_ANIMES_COLECTION_INFO = {}                                                                              ###############
#EACH ANIME WITH ITS INFO AND MAIN PAGE TO SCRAP EPISODES                                        #########
#################################################################################################

def RunScraper():
    
    ###### init #########
    getAnimeTypes()     #
    #####################
    opf = GetFile(SAVE_DATA_FILE_NAME,mode='wb')
    counter = 1
    for a_type in ANIME_TYPES :  

        for pageNum in range(MAX_NUMBER_PAGES):

            _soup = getSoup(GENRE_LINK+a_type+'/'+str(pageNum)+'/')

            if len(_soup.findAll('div', class_='list-container')) >= 1: # hadi bach ntchecker if page khawya

                for anime in _soup.findAll('div', class_='list-container'):

                    #ANIME MAIN PAGE URL
                    mainPageLink    = (anime.find('div',class_='title')).find('a')['href']

                    #COVER IMAGE OF ANIME
                    cover   = anime.find('div',class_='image')
                    cover   = cover.find('img')['src']

                    #YEAR OF PRODUCTION
                    yearProd    = (anime.find('div',class_='top')).find('div').getText()

                    #POSITIVE RATES
                    rates   =   (anime.find('div',class_='top')).findAll('div')[1].getText()

                    #Types
                    _typs   =   []
                    for a in anime.find_all('a',class_='genrehref'):
                        _typs.append((a['href'].replace(GENRE_LINK,'')).replace('/',''))

                    #Brief Story
                    story = anime.find('div',class_='story').getText()

                    #TITLE OF ANIME
                    title = anime.find('div',class_='title').getText()

                    # > SAVIING INTO COLLECTION
                    # > FULL ANIME COLLECTION
                    _ANIMES_COLECTION_INFO[title] = [mainPageLink,pageNum,cover,yearProd,rates,_typs,story]
                    CLEAR()
                    STRING = "+-> ["+str(counter)+"] TYPE : ["+a_type +"]  PAGE : ["+ str(pageNum) +"] ANIME : ["+title+"]"
                    opf.write(bytes("ANIME"+str(counter)+"\n", encoding='utf-8'))
                    for ele in _ANIMES_COLECTION_INFO[title] :
                        if isinstance(ele, list):
                            for sub_ele in ele :
                                opf.write(getBytes('\t'+sub_ele+'\n'))
                        else:
                            opf.write(getBytes(str(ele)+'\n'))
                    opf.write(getBytes('\n\n'))
                    counter += 1
                    print(STRING)
            
    opf.close()#File close
    SCRAPER.close() #close a bb :-p
    return _ANIMES_COLECTION_INFO
