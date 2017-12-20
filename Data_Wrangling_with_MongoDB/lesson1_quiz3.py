# To experiment with this code freely you will have to run this code locally.
# We have provided an example json output here for you to look at,
# but you will not be able to run any queries through our UI.
import json
import requests


BASE_URL = "http://musicbrainz.org/ws/2/"
ARTIST_URL = BASE_URL + "artist/"

query_type = {  "simple": {},
                "atr": {"inc": "aliases+tags+ratings"},
                "aliases": {"inc": "aliases"},
                "releases": {"inc": "releases"}}


def query_site(url, params, uid="", fmt="json"):
    """
    This is the main function for making queries to the musicbrainz API. The
    query should return a json document.
    """
    params["fmt"] = fmt
    r = requests.get(url + uid, params=params)
    print "==> requesting", r.url

    if r.status_code == requests.codes.ok:
        return r.json()
    else:
        r.raise_for_status()


def query_by_name(url, params, name):
    """
    This adds an artist name to the query parameters before making an API call
    to the function above.
    """
    params["query"] = "artist:" + name
    return query_site(url, params)


def main():
    # Q1: How many bands are named "First Aid Kit"?
    results = query_by_name(ARTIST_URL, query_type["simple"], "First aid kit")
    n = 0
    for i, artist in enumerate(results["artists"]):
        if artist["name"].lower() == "first aid kit":
            n += 1
    print '\nThere are ' + str(n) + ' bands named First Aid Kit.\n'

    # Q2: What is 'begin_area' name for Queen?
    results = query_by_name(ARTIST_URL, query_type["simple"], "queen")
    for i, artist in enumerate(results["artists"]):
        if artist["name"].lower() == "queen":
            try:
                print '\nQueen is from ' + artist["begin-area"]["name"] + '.\n'
            except:
                None

    # Q3: What is the Spanish alias for The Beatles?
    results = query_by_name(ARTIST_URL, query_type["simple"], "beatles")
    for i, artist in enumerate(results["artists"]):
        if artist["name"].lower() == "the beatles":
            for j, aliases in enumerate(artist["aliases"]):
                if aliases["locale"] == "es":
                    try:
                        print '\nThe Spanish alias for The Beatles is ' + aliases["name"] + '.\n'
                    except:
                        None

    # Q4: What is the disambiguation for Nirvana?
    results = query_by_name(ARTIST_URL, query_type["simple"], "Nirvana")
    for i, artist in enumerate(results["artists"]):
        if artist["name"].lower() == "nirvana":
            try:
                print 'Disambiguation for Nirvana is "' +  artist["disambiguation"] + '".\n'
            except:
                None

    # Q5: When was One Direction formed?
    results = query_by_name(ARTIST_URL, query_type["simple"], "one direction")
    for i, artist in enumerate(results["artists"]):
        if artist["name"].lower() == "one direction":
            try:
                print '\nOne Direction was formed in ' + artist["life-span"]["begin"] + '.\n'
            except:
                None    
            
    
if __name__ == '__main__':
    main()


