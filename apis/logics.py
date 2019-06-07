import requests
import pycurl
from io import BytesIO
import json
try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode


def batch_mechanism_requests(url, method, post_data={}, get_params={}, headers={}):
    """
    :description: Call API through python requests.
    :param url: Pass the API URL
    :param method: GET or POST
    :param post_data: Post Data
    :param get_params: Get Data to URL
    :param headers: Additional HTTP headers if needed
    :return: API json return
    """
    if method == "get":
        response = requests.get(url=url, params=get_params, headers=headers)
        return response

    if method == "post":
        response = requests.post(url=url, data=post_data, headers=headers)
        return response


def batch_mechanism_curl(url, method, post_data={}, get_params={}, headers=['Accept-Language: en']):
    """
    :description: Call API through pycurl
    :param url: Pass the API URL
    :param method: GET or POST
    :param post_data: Post Data
    :param get_params: Get Data to URL
    :param headers: Additional HTTP headers if needed
    :return: API json return

    :samples tests:
        a) GET METHOD : batch_mechanism_curl('http://127.0.0.1:8000/PSID_list/','get')
        b) POST METHOD : batch_mechanism_curl('http://127.0.0.1:8000/PSID_page_map/','post',{'owner': 1, 'page': 1})

    :additional info:
        Facebook Python SDK :
            https://facebook-sdk.readthedocs.io/en/latest/api.html#class-facebook-graphapi
        PHP Sample
            https://developers.facebook.com/docs/php/howto/example_batch_request/
        Emulate -F in curl
            https://stackoverflow.com/questions/10937164/how-to-emulate-curl-f-for-facebook-graph-api-batch-request-in-python
    """

    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.HTTPHEADER, headers)
    buffer = BytesIO()
    c.setopt(c.WRITEDATA, buffer)

    if method == "get":

        if len(get_params) > 0:
            c.setopt(c.URL, url + '?' + urlencode(get_params))

        c.perform()
        body = buffer.getvalue()
        response_code = c.getinfo(c.RESPONSE_CODE)
        print('Response Code: %d' % response_code)
        print('Response Time: %f' % c.getinfo(c.TOTAL_TIME))
        c.close()

        return response_code, json.loads(body.decode('iso-8859-1'))

    elif method == "post":
        c.setopt(c.POSTFIELDS,  urlencode(post_data))
        c.perform()
        body = buffer.getvalue()
        response_code = c.getinfo(c.RESPONSE_CODE)
        print('Response Code: %d' % response_code)
        print('Response Time: %f' % c.getinfo(c.TOTAL_TIME))
        c.close()

        return response_code, json.loads(body.decode('iso-8859-1'))


def organize_bulk_fb_data(data):
    """
    :param data: Data is a list of Ordered Dict with keys owner , page , label_id and access token
    :sample data format :

     OrderedDict([('owner', 1), ('page', 1), ('label_id', u''), \
     ('access_token', u'3294790573450794350354083450'), \
     ('user', u'kerlkwhe9759345flkg04365gkhdsglsdgkdsfg,dfg074097 03 -03476')])

    :return: No Response
    """
    try:
        consolidate_data = {}
        post_data = {}
        label_data={}
        for i in data:
            if i['access_token'] not in consolidate_data:
                consolidate_data[i['access_token']]=[]
                label_data[i['access_token']] = []

            consolidate_data[i['access_token']].append(i['user'])
            label_data[i['access_token']].append(i['label_id'])

        for key in consolidate_data:
            post_data['access_token'] = key
            post_data['batch'] = []
            for i, val in enumerate(consolidate_data[key]):
                relative_url = "/"+label_data[key][i]+'/label?access_token='+key
                body = urlencode({'user': val})
                post_data['batch'].append({"method": "POST", "relative_url": relative_url, "body": body})
                response = batch_mechanism_curl('https://graph.facebook.com', 'post', post_data)
                print("BULK RESPONSE FROM FB ", response)

    except Exception as e:
        print("Error ", e)
