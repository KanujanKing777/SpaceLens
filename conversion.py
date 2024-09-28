import json

def tsv_to_json(tsv_file, json_file):
    # Read the TSV file and process it
    with open(tsv_file, 'r') as file:
        lines = file.readlines()
    
    # Extract header from the first line
    headers = lines[0].strip().split('\t')
    
    # Process the remaining lines
    data = []
    for line in lines[1:]:
        values = line.strip().split('\t')
        item = {headers[i]: values[i] for i in range(len(headers))}
        data.append(item)
    
    # Write the data to a JSON file
    with open(json_file, 'w') as json_out:
        json.dump(data, json_out, indent=4)

files = [
    "a_OSD-379_transcription-profiling_rna-sequencing-(rna-seq)_Illumina NovaSeq",
    "a_OSD-665_transcription-profiling_rna-sequencing-(rna-seq)_illumina",
    "i_Investigation-379",
    "i_Investigation-665",
    "s_OSD-379",
    "s_OSD-665"
]

for i in files:
    tsv_file = i + '.txt'  
    json_file = 'Output' + i + '.json' 
    tsv_to_json(tsv_file, json_file)
