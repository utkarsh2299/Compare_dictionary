import pandas as pd
import os
import traceback
dict_location ="Fastspeech2_HS/phone_dict"
from indic_unified_parser.uparser import wordparse
from get_phone_mapped_python import TextReplacer
from tqdm import tqdm
phone_dictionary = {}
        # load dictionary for all the available languages
with open("/home/speech/Desktop/isro/Fastspeech2_HS/output.txt", "w") as file:
    
    for dict_file in os.listdir(dict_location):
        try:
            language = dict_file  
            if language != "hindi":
                continue
            print(language)
            dict_file_path = os.path.join(dict_location, dict_file)
            df = pd.read_csv(dict_file_path, delimiter=" ", header=None, dtype=str)
            phone_dictionary[language] = df.set_index(0).to_dict('dict')[1]
        except Exception as e:
                print(traceback.format_exc())   
                
                
    for language, inner_dict in phone_dictionary.items():
                print(f'Language: {language}')
                dict_len=len(inner_dict)
                print(dict_len)
                count = 0
                index=0
                for key, value in tqdm(inner_dict.items(), total = dict_len, desc="Total progress"):
                    index+=1
                    #print(key,"    old==", TextReplacer().apply_replacements(wordparse(key, 0, 0, 1)), "    New==", value)
                    if TextReplacer().apply_replacements(wordparse(key, 0, 0, 1)) == value:
                        continue
                        
                    else:
                        count += 1
                            # Write the output to the file
                        file.write(str(index)+" "+str(key)+ "    "+ str(value)+ "    New=="+str( TextReplacer().apply_replacements(wordparse(key, 0, 0, 1)))+ "\n")
                        #file.write("HEllo World\n")

                    
print("Total Erroneous Words:", (count/dict_len)*100, "%")

    