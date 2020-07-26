import json as jsn
import logging
import os
import requests as reqs

logger = logging.getLogger('turq')
logger.setLevel(logging.DEBUG)

# MOCK_API_CLIENT = get_env('MOCK_API_CLIENT', 'true') == 'true'

def proxy(url, method='GET', payload=None, headers={}):
    logger.debug("proxy => url=%s, method=%s, payload=%s, headers=%s", url, method, jsn.dumps(payload), str(headers))
    hds = {'Content-Type': 'application/json', 'xtid': request.headers['xtid']}
    hds.update(headers)
    if method == 'GET':
        return reqs.get(url, headers=hds)
    elif method == 'POST':
        return reqs.post(url, data=jsn.dumps(payload), headers=hds)
    return {}

def gateway_proxy(url, method='GET', payload=None, headers={}):
    return proxy(GATEWAY_URL + url, method, payload, headers)

def get_env(name, default=None, parser=str):
    if name in os.environ:
        v = os.environ[name]
        logger.debug('%s=%s', name, v)
        return v if parser is None else parser(v)
    return default

def handle_response(resp, parser=None):
    logger.debug('response: %i %s', resp.status_code, resp.text)
    if resp.status_code == 200:
        if parser is None:
            json(resp.json())
        else:
            json(parser(resp.json()))
    else:
        status(resp.status_code)
        json(resp.json())

GATEWAY_URL = ''
if 'GATEWAY_URL' in os.environ:
    GATEWAY_URL = os.environ['GATEWAY_URL']

def log(message):
    logging.getLogger('turq').debug("[DEBUG] %s" % message)


log('GATEWAY_URL=%s' % GATEWAY_URL)

if route('/cliente-active/:documento') and GET:

    log("Retorno por Mock")
    json({
        "name": "Cliente",
        "Documento": "9714744890"
    })    
    status(200)

elif route('/clientes') and POST:

    documento = request.json['Documento']
    email = request.json['Email']

    log('Saving cliente')
    json({
        "documento": documento,
        "email": email,
        "status": "CREATED"
    })
    status(201)