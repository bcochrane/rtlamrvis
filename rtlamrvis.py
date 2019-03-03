import json

rtlamr_file = "testdata/rtlamr_20190130.json"

rtlamr_data = []
with open(file=rtlamr_file) as rtlamr_f:
    for line in rtlamr_f:
        line_json = json.loads(line)

        #  normalize key names (EndpointID -> ID)
        if 'EndpointID' in line_json['Message']:
            line_json['Message']['ID'] = line_json['Message']['EndpointID']
 
        # flatten data structure
        for key in ('ID', 'Consumption'):
            line_json[key] = line_json['Message'][key]

        # delete fields we don't need
        for key in ('Offset', 'Length', 'Message'):
            del line_json[key]

        # print(line_json)
        rtlamr_data.append(line_json)
