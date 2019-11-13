import requests
import json
from threading import Thread
class Starter(object):
    @staticmethod
    def start_scrapper(time_str):
        my_thread = thread_Scrap(time_str)
        my_thread.start()
    @staticmethod
    def start_stat():
        pass

class thread_Scrap(Thread):
    def __init__(self,  time_str):
        Thread.__init__(self)
        self.time_str=time_str
    
    def run(self): 
        
       
        data={"time":self.time_str}
        
        r = requests.post(url = 'http://scr:5000', data = json.dumps(data), timeout=40) 
        print(data)
        return data
    
# extracting response text  
        
        
    

 
 
