#!/usr/bin/python

# API testing for netrunnerdb.com
# api info can be obtiained here http://netrunnerdb.com/en/apidoc

import json
import urllib

# Superscripts in unicode
# https://en.wikipedia.org/wiki/Unicode_subscripts_and_superscripts
# CTRL+v u xxxx
# 0 u+2070 eg. Trace⁰
# i u+2071 eg. Traceⁱ
# 1 u+00B9 eg. Trace¹
# 2 u+00B2 eg. Trace²
# 3 u+00B3 eg. Trace³
# 4 u+2074 eg. Trace⁴
# 5 u+2075 eg. Trace⁵
# 6 u+2076 eg. Trace⁶
# 7 u+2077 eg. Trace⁷
# 8 u+2078 eg. Trace⁸
# 9 u+2079 eg. Trace⁹

decklist_base_url = "http://netrunnerdb.com/api/decklist/"
card_base_url = "http://netrunnerdb.com/api/card/"
allcards_base_url = "http://netrunnerdb.com/api/cards/"

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

def get_card_info(card_id):
    url = "http://netrunnerdb.com/api/card/" + str(card_id)
    urldata = urllib.urlopen(url)
    raw_carddata = urldata.read()
    card_json = json.loads(str(raw_carddata))
    #print "card_json", card_json
    #return card_json[0]['title']
    #print card_json[0]
    print " Code:" + card_json[0]['code']
    print "Title:" + card_json[0]['title']
    print " Type:" + card_json[0]['type']
    #print " Cost:" + str(card_json[0]['cost'])
    print " Text:" + card_json[0]['text']

#print deckdata_json['cards']

#for card in deckdata_json['cards']:
    #card_name = get_card_name(card)
    #print "Card:", card, "Name:", card_name, "Qty:", deckdata_json['cards'][card]

#get_card_name("01002")
#get_card_info("01002")
get_card_info("02020")
get_card_info("02046")
get_card_info("01036")
