import flask_task.reader as reader

class Processor(object):
    @staticmethod
    def process(n=5,pol=3):
        dict_curr=reader.IOClass.readJSON()
        for date_r in dict_curr.items():
            for  bank_r in date_r [1].items():
                for k in bank_r[1].items():
                    if k[1]=='':
                        del dict_curr[date_r[0]]
                        break
        arr_list=reader.IOClass.makeAll(dict_curr)
        return arr_list
        

