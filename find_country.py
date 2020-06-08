import requests
from urllib.parse import quote as encode_url

# change limit parameter to get more results from a single query
api_url = "https://api.tomtom.com/search/2/geocode/{encoded_addr}.json?limit=1&key={api_key}"
tomtom_api_key = "WlKkYbkxFL8PzxkARuMqqHlyN8pZExNh" #can only request 2500 req a day


def tomtom_search(addr):
    url = api_url.format(encoded_addr=encode_url(addr,encoding="utf-8"),api_key=tomtom_api_key)
    print(url)
    resp=requests.get(url)
    if resp.status_code==200:
        return filter_country(resp.json())
    
    print(f"error in search:{resp.status_code}")
    return ""
    # print(resp.content)

def filter_country(resp):
    try:
        #print(resp)
        resp = resp['results'][0]['address']
        return {'state':resp['countrySubdivision'],
                'city':resp['countrySecondarySubdivision'],
                'country':resp['country']}
    except Exception as e:
        print('error in filter_country :',e)
        return ""

if __name__ == "__main__":
    """ function : tomtom_search(address) returns a dict like {state:'rajasthan',city:'jaipur',country:'india'} 
        or
        print error with status code and return "" """
    # for non english characters we can identify the lnaguage using textblob lib and map it to the country name
    r=tomtom_search('jaipur')
    print(r)
