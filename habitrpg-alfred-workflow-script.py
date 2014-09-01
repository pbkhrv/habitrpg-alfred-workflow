import os
import json
import sys
import httplib, urllib

def main(query):
    config = get_config()
    data = json.dumps({'type': 'todo', 'text': query})
    headers = {
        'Content-type': 'application/json; charset=utf-8',
        'x-api-user': config['habitrpg_api_user'],
        'x-api-key': config['habitrpg_api_key']}
    conn = httplib.HTTPSConnection("habitrpg.com", "443")
    conn.request("POST", "/api/v2/user/tasks", data, headers)
    response = conn.getresponse()
    if str(response.status) == "200":
        print "SUCCESS: New todo created"
    else:
        print "FAIL: HabitRPG returned an error! %s" % response.reason
    conn.close()

def get_config():
    with open('test-config.json') as f:
        return json.load(f)

def get_query():
    # if it's running in Alfred, query will be substituted
    query = "{query}"
    # or can be called from command line
    if query == '\{query\}':
        if len(sys.argv) > 1:
            query = sys.argv[1]
        else:
            query = ""
    if len(query) == 0:
        return None
    else:
        return query

if __name__ == "__main__":
    q = get_query()
    if q:
        main(q)
    else:
        print "Nothing to do"
