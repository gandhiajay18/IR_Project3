# -*- coding: utf-8 -*-
"""
Thanks to the author Ruhan Sa, who is the TA of IR project 3 in Fall 2015
"""

import json
import urllib.request

count = 1
with open('C:\\Users\\Ajay-Pc\\Desktop\\queries1.txt', encoding="utf-8") as f:
    for line in f:
        outf = open('DFR'+str(count)+'.txt', 'a+')
        query = line.strip('\n').replace(':', '')
        query = query.replace("#","")
        query = query.replace("@","")
        print(query)
        query = urllib.parse.quote(query)
        inurl = 'http://52.39.210.221:8983/solr/irptry/select?defType=dismax&fl=score,id,text_en&indent=on&q=' + query + '&rows=20&wt=json&qf=text_all^4.0+tweet_hashtags+text_en+text_de+text_ru&pf=text_all^40'
        qid = count
        IRModel = 'DFR'
        data = urllib.request.urlopen(inurl).read()
        docs = json.loads(data.decode('utf-8'))['response']['docs']
        rank = 1
        for doc in docs:
            if (qid < 10):
                outf.write('00'+str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + 'DFR' + '\n')
            else:
                outf.write('0'+str(qid) + ' ' + 'Q' + str(count) + ' ' + str(doc['id']) + ' ' + str(rank) + ' ' + str(doc['score']) + ' ' + 'DFR' + '\n')
            rank += 1
        count += 1
    outf.close()

