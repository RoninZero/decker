#!/usr/bin/python

# API testing for netrunnerdb.com
# api info can be obtiained here http://netrunnerdb.com/en/apidoc

import json
import urllib

decklist_base_url = "http://netrunnerdb.com/api/decklist/"
card_base_url = "http://netrunnerdb.com/api/card/"

url = "http://netrunnerdb.com/api/decklist/30766"

urldata = urllib.urlopen(url)

raw_deckdata = urldata.read()

deckdata_json = json.loads(str(raw_deckdata))

#print deckdata_json

def get_card_name(card_id):
    url = "http://netrunnerdb.com/api/card/" + str(card_id)
    urldata = urllib.urlopen(url)
    raw_carddata = urldata.read()
    card_json = json.loads(str(raw_carddata))
    #print "card_json", card_json
    return card_json[0]['title']

#print deckdata_json['cards']

for card in deckdata_json['cards']:
    card_name = get_card_name(card)
    print "Card:", card, "Name:", card_name, "Qty:", deckdata_json['cards'][card]

get_card_name("01002")
