#!/usr/bin/env python3

# API testing for netrunnerdb.com
# api info can be obtiained here http://netrunnerdb.com/en/apidoc

import json
import urllib

decklist_base_url = "http://netrunnerdb.com/api/decklist/"
card_base_url = "http://netrunnerdb.com/api/card/"
allcards_base_url = "http://netrunnerdb.com/api/cards/"

url = "http://netrunnerdb.com/api/decklist/30766"

#####urldata = urllib.urlopen(url)

#####raw_deckdata = urldata.read()

#####deckdata_json = json.loads(str(raw_deckdata))

#print deckdata_json

def get_card_name(card_id):
    url = "http://netrunnerdb.com/api/card/" + str(card_id)
    #####urldata = urllib.urlopen(url)
    #####raw_carddata = urldata.read()
    card_json = json.loads(str(raw_carddata))
    #print "card_json", card_json
    return card_json[0]['title']

def get_card_info(card_id):
    url = "http://netrunnerdb.com/api/card/" + str(card_id)
    #####urldata = urllib.urlopen(url)
    #####raw_carddata = urldata.read()
    card_json = json.loads(str(raw_carddata))
    #print "card_json", card_json
    #return card_json[0]['title']
    #print card_json[0]
    #####print " Code:" + card_json[0]['code']
    #####print "Title:" + card_json[0]['title']
    #####print " Type:" + card_json[0]['type']
    #print " Cost:" + str(card_json[0]['cost'])
    #####print " Text:" + card_json[0]['text']

def parse_all_cards():
    with open('all_cards.json') as data_file:
        all_cards = json.load(data_file)

    for card in all_cards:
        print(card)
        all_keys = []
        #print "Title:" + card['title'] + "Keys:" + str(card.keys())
        for key, value in card.items():
            #print "key:", key.encode('utf-8'), "value:", value.encode('utf-8')
            try:
                print("key:", str(key), "value:", str(value)) #fails on unicode error
            except Exception as e:
                print(e)
            if key not in all_keys:
                all_keys.append(key)
        print(all_keys)


#print deckdata_json['cards']

#for card in deckdata_json['cards']:
    #card_name = get_card_name(card)
    #print "Card:", card, "Name:", card_name, "Qty:", deckdata_json['cards'][card]

#get_card_name("01002")
#get_card_info("01002")
#get_card_info("02020")
#get_card_info("02046")
#get_card_info("01036")
parse_all_cards()
