import json

rtlamr_file = "testdata/test.json"

rtlamr_data = []
with open(file=rtlamr_file) as rtlamr_f:
    for line in rtlamr_f:
        # normalize JSON objects and eliminate unnecessary fields
        if 'ID' in line:
            print("found ID key")


        # This isn't working. I have to stop thinking in Perl.

        #if 'ID' in line{'Message'}:
        #    print("found ID")
        #elif 'EndpointID' in line{'Message'}:
        #    print("found EndpointID")

        rtlamr_data.append(json.loads(line))

print(rtlamr_data)