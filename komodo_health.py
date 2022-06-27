import collections 

'''
Write a program that parse the query string parameters and returns the following hashmap with query string key-values as the
key-value in data structure. If there are identical keys, add the values to a list.

Input:
url = 'https://api.komodohealth.com/v1/organizations?oid=5&pid=4&pid=7&qid=10'

Output:
{
    "oid": 5,
    "pid", [4, 7],
    "qid": 10
}
'''

def parse_query_string(url):
    query_params_map = collections.defaultdict(list)

    _, query_params = url.split('?')
    parsed_query_params = query_params.split('&')
    
    for query in parsed_query_params:
        query_key, query_value = query.split('=')
        query_params_map[query_key].append(query_value)

    for key, value in query_params_map.items():
        if len(value)==1: 
            query_params_map[key] = value[0]

    return dict(query_params_map)


query_string = 'https://api.komodohealth.com/v1/organizations?oid=5&pid=4&pid=7&qid=10'
print(parse_query_string(query_string))

