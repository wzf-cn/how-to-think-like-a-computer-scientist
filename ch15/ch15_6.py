# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:36:50 2017

@author: wzFelix

Email: wzfhrb.cn@gmail.com

Learn with everyone
"""
"""
q_6:
    Create a new class, SMS_store. The class will instantiate SMS_store 
    objects, similar to an inbox or outbox on a cellphone:
        my_inbox = SMS_store()
    This store can hold multiple SMS messages (i.e. its internal state will 
    just be a list of messages). Each message will be represented as a tuple:
        (has_been_viewed, from_number, time_arrived, text_of_SMS)
    The inbox object should provide these methods:
        my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS)
          # Makes new SMS tuple, inserts it after other messages
          # in the store. When creating this message, its
          # has_been_viewed status is set False.
        
        my_inbox.message_count()
          # Returns the number of sms messages in my_inbox
        
        my_inbox.get_unread_indexes()
          # Returns list of indexes of all not-yet-viewed SMS messages
        
        my_inbox.get_message(i)
          # Return (from_number, time_arrived, text_of_sms) for message[i]
          # Also change its state to "has been viewed".
          # If there is no message at position i, return None
        
        my_inbox.delete(i)     # Delete the message at index i
        my_inbox.clear()       # Delete all messages from inbox        
"""

class SMS:
    def __init__(self, been_viewed = False, number = '', time = '', text = ''):
        self.has_been_viewed = been_viewed
        self.from_number = number
        self.time_arrived = time
        self.text_of_SMS = text   
        
class SMS_store:
    def __init__(self):
        self.list_of_SMS = []
        
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        sms = SMS(False, from_number, time_arrived, text_of_SMS)
        self.list_of_SMS.append(sms)
        
    def message_count(self):
        return len(self.list_of_SMS)
        
    def get_unread_indexes(self):
        unread_list = []
        for i in range(len(self.list_of_SMS)):
            if self.list_of_SMS[i].has_been_viewed == False:
                unread_list.append(i)
        return unread_list
                
    def get_message(self, i):
        return self.list_of_SMS[i].text_of_SMS
    
    def delete(self, i):
        self.list_of_SMS.__delitem__(i)
        
    def clear(self):
        self.list_of_SMS.clear()
    
my_inbox = SMS_store()
            
my_inbox.add_new_arrival(1234, '2012,02,31', 'I love you')  
my_inbox.add_new_arrival(1234, '2012,02,31', 'I love you more')    
print('there are {0} messages.'.format(my_inbox.message_count()))
print('unread messages are:\n{0}'.format(my_inbox.get_unread_indexes()))
print(my_inbox.get_message(0))           
print(my_inbox.get_message(1))            
            
            
            
            
            
            
            
            
            
            
            