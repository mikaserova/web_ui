#import json
from couchbase.exceptions import CouchbaseError
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.n1ql import N1QLQuery
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta
import re
class IOClass(object):
    @staticmethod
    def dbConnect(link='http://cdb:8091', buck='currency_rate'):#link changed must be cdb
        cluster = Cluster(link)
        print("CLUSTER:",cluster)
        authenticator = PasswordAuthenticator('sashasierova', '4esZXdr5')
        cluster.authenticate(authenticator)
        bucket = cluster.open_bucket(buck)
        return bucket 
    @staticmethod
    def readJSON(link='http://cdb:8091'):
        w_bucket=IOClass.dbConnect(buck="currency_weekly")
        m_bucket=IOClass.dbConnect(buck="currency_monthly")
        bucket=IOClass.dbConnect(link)
        feeds={}
        td=date.today()
        sd = td + relativedelta(days=-td.weekday())
        sw = td + relativedelta(days=-td.day )
        sd = re.sub('-', '/',str(sd))
        sw = re.sub('-', '/',str(sw))
        m_query = N1QLQuery("SELECT META().id, * FROM `currency_monthly` LIMIT 12") 
        w_query = N1QLQuery("SELECT META().id, * FROM `currency_weekly` WHERE META().id >$1",sw)
        query = N1QLQuery("SELECT META().id, * FROM `currency_rate` WHERE META().id >$1",sd)
        for row in bucket.n1ql_query(m_query):
            if row is not None:
                feeds[row['id']]=row['currency_monthly']

        for row in bucket.n1ql_query(w_query):
            if row is not None:
                feeds[row['id']]=row['currency_weekly']

        for row in bucket.n1ql_query(query):
            if row is not None:
                feeds[row['id']]=row['currency_rate']

        return feeds

    @staticmethod
    def makeArraysByBankCurr(d,bank_name, curr_name ):
        keys=[]
        buy=[]
        sell=[]
        for key, val in d.items():
            keys.append(key[:10])
            bank=val[bank_name]
            temp=bank[curr_name+'_buy']
            buy.append(float(temp))
            temp=bank[curr_name+'_sell']
            sell.append(float(temp))
        return  keys, buy, sell,bank_name, curr_name
    @staticmethod
    def makeAll(d):
        res=[]
        curr_names=['EUR','USD','RUB']
        bank_names=['Privat', 'Oschad', 'Aval']
        for b in bank_names:
            for c in curr_names:
                res.append(IOClass.makeArraysByBankCurr(d,b,c))
        return res