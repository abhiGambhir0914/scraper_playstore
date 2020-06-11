from countries import all_countries,lang_map
import csv,json
from langdetect import detect,DetectorFactory

""" 
*** External dependencies ***
 
    1. pip install langdetect

*** OTHER **

    2. change *_PATH vars 
    3. map countries with language code in counties.py (if required)

*** TODO ***
    1. output dataset contains country name synonym like US,USA, United State, United States of america
        so we need to eliminate these patterns
    
"""
DATASET_PATH = "dataset/app-details.csv"
OUTPUT_PATH = "dataset/apps-with-countries.json"


def detect_lang(text): # return language code
    try:
        DetectorFactory.seed=0
        return detect(text)
    except:
        return ""

def is_english(text): # returns Boolean
    text= text.lower()
    # checking for ascii value of characters
    for word in text.split(' '):
        if ord(word[0]) >= 97 and ord(word[0])<=122:
            return True
    return False
    # return True if detect_lang(text)=='en' else False


def get_app(): # generator function | returns one row from csv file
    with open(DATASET_PATH,mode='r',encoding="utf-8") as dataset:
        reader = csv.DictReader(dataset)
        count = 0
        for row in reader:
            count+=1
            yield row
        print('total rows:',count)

def dump_new_dataset(in_dict): #dump data in json
    with open(OUTPUT_PATH,mode="w+",encoding="utf-8") as new_dataset:
        json.dump(in_dict,new_dataset)

def find_country(address): # returns country name or ""
    if not address :
        return ""

    if is_english(address): # first check if address is in english 
        for country in all_countries:
            index = address.lower().find(country.lower())
            if index>-1:
                return country
        return ""
    else:
        # print(address)
        lang_code = detect_lang(address)
        return lang_map[lang_code] if lang_code in lang_map else lang_code


def extract_countries(): #returns [{'app_package_name':app['app_package_name'],'country':country},...]
    try:
        extracted_countries = []
        for app in get_app():
            country = find_country(app['developer_address'])
            if country:
                extracted_countries.append({'app_package_name':app['app_package_name'],'country':country})
                # print(app['app_package_name'],country)
        return extract_countries
    except Exception as e:
        print('Operation stopped!\n',e)
        exit()

if __name__ == "__main__":
    new_dataset = extract_countries()
    dump_new_dataset(new_dataset)
    # pass



