import random
import pandas as pd 

id_1 = 0000 #change to first student id
id_2 = 0000 #change to second student id
id_3 = 0000 #change to third student id "leave 0000 if team of 2"
random_seed = id_1+id_2+id_3
random.seed(random_seed)
data_path="data.csv"#reaplace with data path
output_path="your_data.csv"#reaplace with output data path

all_data=pd.read_csv(data_path) 
all_columns = all_data.columns.tolist()

target_column = 'smoking'  # Replace 'specific_column_name' with the actual column name

all_columns.remove(specific_column)

features_numbers = random.sample(range(23), 10)


selected_columns = np.random.choice(all_columns, features_numbers, replace=False)
print(selected_columns) #MUST BE PRINTED
selected_columns = np.append(selected_columns, target_column)
sample_df = all_data[selected_columns].copy()
sample_df.to_csv(output_path)   #From HERE YOU CAN SPLIT FOR TRAIN ,VALID AND TEST
