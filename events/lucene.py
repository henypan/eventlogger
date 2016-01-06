import sys
import requests
import json

from elasticsearch import Elasticsearch
from collections import OrderedDict


def init_index(host_url, index_name, index_dict):
    mapping_dict = {"settings": {"number_of_shards": 1, "number_of_replicas": 0}, "mappings": {
        "leet": {"_all": {"enabled": False}, "dynamic_templates": [{"template_1": {
            "mapping": {"index": "not_analyzed", "type": "string"}, "match_mapping_type": "string", "match": "*"}}],
            "properties": {}}}}
    date_mapping = {"type": "date", "format": "dateOptionalTime"}
    num_mapping = {"type": "long"}
    try:
        mapping_dict['settings']['number_of_shards'] = index_dict['settings']['number_of_shards']
        mapping_dict['settings']['number_of_replicas'] = index_dict['settings']['number_of_replicas']
    except KeyError:
        print('Using the default number_of_shards and number_of_replicas')

    for field_name in index_dict['fields']:
        if 'time' in field_name.lower():
            mapping_dict['mappings']['leet']['properties'][field_name] = date_mapping
        if 'number' in field_name.lower():
            mapping_dict['mappings']['leet']['properties'][field_name] = num_mapping

    response = requests.put(host_url + index_name, data=json.dumps(mapping_dict))
    if 'error' in response.json().keys():
        print('Index [' + index_name + '] already exists')


def start_index(index_json, eventdata):
    print('start_index')
    with open(index_json) as json_file:
        index_dict = json.load(json_file, object_pairs_hook=OrderedDict)
    try:
        host_ip = index_dict['host']
        index_name = index_dict['index_name']
    except KeyError:
        sys.exit('The format of input JSON is not correct.')

    es = Elasticsearch(hosts=host_ip, timeout=120)
    host_url = 'http://' + host_ip + ':9200/'
    if not es.indices.exists(index=index_name):
        init_index(host_url, index_name, index_dict)
    data_row = dict()
    title = eventdata.question_text.strip().lower()
    number = eventdata.number
    search_query = 'Number: query'.replace('query', str(number))
    matches = es.search(index=index_name, q=search_query, size=1000)
    hits = matches['hits']['hits']
    frequencies = 1
    frequencies += len(hits)

    data_row['Title'] = title
    data_row['Number'] = number
    data_row['Difficulty'] = eventdata.difficulty
    data_row['Note'] = eventdata.note.strip().lower()
    data_row['Method'] = eventdata.method.strip().lower()
    data_row['LogTime'] = eventdata.pub_date.strftime('%Y-%m-%dT%H:%M:%S')
    es.index(index_name, 'leet', data_row)
    print(data_row)
    return frequencies
