# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
import urllib.request

count = 1
with open('C:\queries2.txt', encoding="utf-8") as f:
    for line in f:  
        outf = open(str(count)+'.txt', 'a+')
        query = line.strip('\n').replace(':', '')
        query = line.strip('\n').replace('#', '')
        query = line.strip('\n').replace('@', '')
        query = urllib.parse.quote(query)
        inurl = 'http://54.186.7.246:8983/solr/lol/select?defType=dismax&fl=score,id,text_en&indent=on&q=' + query + '&rows=20&wt=json&qf=tweet_hashtags^12.0+text_all^10.0+text_en+text_de+text_ru&pf=text_all^100'
        qid = count
        IRModel = 'IRModel'        
        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        rank = 1
        for doc in docs:
            if (qid < 10) :
                outf.write('00' + str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')
            else:
                outf.write('0' + str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + IRModel + '\n')

            rank += 1
        outf.close()
        count += 1



