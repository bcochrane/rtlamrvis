import json
import pprint

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

pp = pprint.PrettyPrinter(width=100)
pp.pprint(rtlamr_data)
