import time
import logging 
from sklearn.metrics.pairwise import cosine_similarity 
import sys


localtime = time.asctime( time.localtime(time.time()) )

print("Local current time :", localtime)

from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

def single_Utternce_Processor():

     Utterance = sys.argv[1]
     Utterance_To_Compare = sys.argv[2]
     
     print("Utterance is " , Utterance)
     print("Utterance_To_Compare is ", Utterance_To_Compare )
     
     sentl = Utterance.replace("\n","") 
     sent2 = Utterance_To_Compare.replace("\n","") 
     
     sentence1_embed = model. encode(str(sentl)) 
     sentence2_embed = model.encode(str(sent2)) 
     
     cos_sim = cosine_similarity([sentence1_embed],[sentence2_embed])
     print(sentl , 'vs ',sent2 , "is" , cos_sim[0])     

     localtime = time.asctime( time.localtime(time.time()) )
     print("Local current time :", localtime)



def batch_Processor():
     
     f = open("input_utt_list.txt","r")
     f2 = open("db_utt_list.txt","r") 
     
     DB_UTTS = f.readlines() 
     INPUT_UTTS = f2.readlines() 

     eligible_utts = [] 
     print("DB_UTTS is " , DB_UTTS)
     print("INPUT_UTTS is " , INPUT_UTTS)

     for sentence in INPUT_UTTS:
          for sentence2 in DB_UTTS:
               sentl = sentence.replace("\n","") 
               sent2 = sentence2.replace("\n","") 
               sentence1_embed = model. encode(str(sentl)) 
               sentence2_embed = model.encode(str(sent2)) 
               cos_sim = cosine_similarity([sentence1_embed],[sentence2_embed])
               print("-----------------------")
               print(sentl , 'vs ',sent2 , "is" , cos_sim[0])
               if(cos_sim > 0.5):
                    eligible_utts.append(sentence)
                    print(sentl , 'vs ',sent2 , 'is' , cos_sim[0]) 

     print("eligible_utts ", eligible_utts) 
     myset = set(eligible_utts) 
     print("unique set" , myset) 

     localtime = time.asctime( time.localtime(time.time()) )

     print("Local current time :", localtime)

if(len(sys.argv) > 2 ):
     single_Utternce_Processor()

else:
     batch_Processor()