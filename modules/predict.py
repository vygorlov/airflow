import json
import os
import os.path as path
import pandas as pd

import dill


def predict():
    data = pd.DataFrame()
    test_list = []
    two_up = path.abspath(path.join(__file__, "../.."))
    for file_name in os.listdir(two_up + "/data/models/"):
        with open(two_up + "/data/models/" + file_name, 'rb') as model_file:
            model = dill.load(model_file)
            my_list = []
            for test in os.listdir(two_up + "/data/test/"):
                with open(two_up + "/data/test/" + test, 'rb') as test_file:
                    if not (test in test_list):
                        test_list.append(test)
                    test_json = json.load(test_file)
                    test_df = pd.DataFrame([test_json])
                    my_list.append(model.predict(test_df))
            data[file_name] = my_list
    data["test"] = test_list
    data = data.set_index('test')
    data.to_csv(two_up+"/data/predictions/predict.csv")


if __name__ == '__main__':
    predict()
