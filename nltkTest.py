# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 11:12:31 2016

@author: MaGesh
"""

import nltk
import re

class IdentifyNames(object):
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.returnAPI = self.firstName+" "+self.lastName+"'s message box" #Assuming this is what LinkedIn API returns
    
    def identifyCorrectReceipentName(self):
        sent = self.returnAPI
        sent1 = nltk.word_tokenize(sent)
        sent2 = nltk.pos_tag(sent1)
        for chunk in nltk.ne_chunk(sent2):
            num=re.sub(r'\W'," ",str(chunk))
            if num.split()[0] == 'PERSON':
                self.name = num.split()[1] #Identifies the name of the person
                break
                
    def sendEmail(self):
        mailBody = "This is Magesh Rajasekaran, a recent graduate student at the University of New Mexico. I am more passionate towards machine learning and data mining. At this moment, I am looking for any entry level software engineer position at Intel. Please write me back to let me know if I can have opportunity then I would send my CV over to you."
        mailHeader = "Hi"+" "+self.name+","
        mailSignature = "Thank you, MR"
        print mailHeader
        print mailBody
        print mailSignature
        self.mailSentConfirmation()
        
    def mailSentConfirmation(self):
        print "Mail has been sucessfully sent to "+self.name+"!"
    
    def processStarts(self):
        self.identifyCorrectReceipentName()
        self.sendEmail()    

def main():
    identifyNames = IdentifyNames('Rohit','Malshe')
    identifyNames.processStarts()


if __name__ == '__main__':
    main()