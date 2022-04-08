# Semantic_Similarity_SBERT

**NOTE**

- This Module is For Identifying Semantic Similarity between Sentences
- We Used Sentence Transformers as Pre-trained Model for Embeddings
- We USed Cosine Similarity for Calculating the Similarity Score 

------------------------------------------------------------------------------------------------------
**Pre-Requisites:**

< Use Linux/Ubuntu > --> Sentence Transformers works best with Linux/Ubuntu 

< Upgrade pip3 to latest version > 

pip3 install sentence_transformers

pip3 install sklearn  

------------------------------------------------------------------------------------------------------
**To Execute the Program:**

Python3 semanticSimilarity.py "Any_Sentence <str>" "Any_Other_Sentence_To_Compare <str>" 
------------------------------------------------------------------------------------------------------
**To Execute Batch Program**
-
  Populate Input_utt_list.txt ==> with Input Sentences   
 -Populate DB_Utt_List.txt ==> with Sentences to compare 
  
  Python3 semanticSimilarity.py
------------------------------------------------------------------------------------------------------
