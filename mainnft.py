import csv, json, os, hashlib, requests,os
import argparse

url = f'https://docs.google.com/spreadsheets/d/1-9zf50iUmdtvpbEvQ7I-M2vlK8hCSB1DC_bF5bDNjxE/edit#gid=840755023'

data = {}

def csvFilePath():
    print("Uploading")
    response = requests.get(url)
    
    with open('.csv', 'w') as csvFile:
        csvFile.write(response.content.decode('utf-8'))
    print('Ready')
    
def jsonFilePath():
    
    if not os.path.exists('jsons.output'):
        os.mkdir('jsons.output')

    with open("teams.csv") as csvFile:
        reader = csv.reader(csvFile, delimiter=",")
        current_team = ''    
        
        for line,row in enumerate(reader):
            team, sn, filename, name, description, gender, attributes, _ = row[:8]
            
            if line== 0:
              
                print(f'HEADERS:  {", ".join([x for i,x in enumerate(row) if i<8])}')
                print()
                print('CHIP-007 json')
                
            else:
                if team:
                    current_team = team
                    
                item = {
                            "format": "CHIP-0007",
                            "name": name,
                            "description": description,
                            "minting_tool": current_team,
                            "sensitive_content": False,
                            "series_number": sn,
                            "series_total": 392,
                            "attributes": [
                                {
                                    "trait_type": "gender",
                                    "value": gender,
                                },
                                
                            ],
                            "collection": {
                                "name": "Zuri NFT Tickets for Free Lunch",
                                "id": "b774f676-c1d5-422e-beed-00ef5510c64d",
                                "attributes": [
                                    {
                                        "type": "description",
                                        "value": "Rewards for accomplishments during HNGi9.",
                                    }
                                ],
                            },
                        }
                attr = [x.split(':') for x in attributes.split(';') if x]
                
                for att in attr:
                    item['attributes'].append({'trait_type': att[0].strip(), 'value':att[1].strip()})
                
                with open(f'jsons/{filename}.json', 'w') as jf:
                    jf.write(json.dumps(item, indent=4))
                    
    print('Done')