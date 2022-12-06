import pymongo
import pandas as pd
import json

client=pymongo.MongoClient('mongodb://localhost:27017/neurolabDB')
database='aps'
collection_name='sensor'
location_file='/config/workspace/aps_failure_training_set1.csv'





if __name__=="__main__":
    df=pd.read_csv(location_file)
    print('row and column',df.shape)

    #convert to json so we can dump in mongodb
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())

    client[database][collection_name].insert_many(json_record)