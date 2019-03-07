import json
import pandas as pd
import matplotlib.pyplot as plt

rtlamr_file = "testdata/test.json"

rtlamr_data = {}
with open(file=rtlamr_file) as rtlamr_f:
    for line in rtlamr_f:
        line_json = json.loads(line)

        ID = None
        if 'EndpointID' in line_json['Message']:
            ID = line_json['Message']['EndpointID']
        else:
            ID = line_json['Message']['ID']

        Time = line_json['Time']
        Consumption = line_json['Message']['Consumption']

        if ID not in rtlamr_data:
            rtlamr_data[ID] = []
        rtlamr_data[ID].append({'Time': Time, 'Consumption': Consumption})

for ID in rtlamr_data:
    print(f'ID: {ID}')

    df = pd.DataFrame(rtlamr_data[ID])
    df['Time'] = pd.to_datetime(df['Time'])
    df = df.set_index('Time')
    df['delta'] = df.rolling(window='1h').var()

    # df.plot(y='delta', marker='o')
    df.plot(y='Consumption')
    df.plot(kind='bar', y='delta')
    plt.show()
