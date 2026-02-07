import websockets
import websocket
import json
import asyncio
import ssl

import websockets.asyncio
import websockets.asyncio.client

class QlikEngine:
    def __init__(self, url, cert_path, user):
        self.url = url
        self.cert_path = cert_path
        self.user = user
        self.responses = []
        self._create()
    def _create(self):
        self._tls_context()
        self._set_user()
    def _tls_context(self):
        self.tls_ctxt = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.tls_ctxt.load_verify_locations(f'{self.cert_path}/root.pem')
        self.tls_ctxt.load_cert_chain(f'{self.cert_path}/client.pem', f'{self.cert_path}/client_key.pem')
        self.tls_ctxt.check_hostname = False
        self.tls_ctxt.verify_mode = ssl.CERT_REQUIRED
    def _set_user(self):
        double_bs = "\\"
        if "\\" in self.user: 
            self.full_user = f"UserDirectory={self.user.split(double_bs)[0]}; UserId={self.user.split(double_bs)[1]}"
            self.full_user_2 = self.user
        else:
            self.full_user = f"UserDirectory=INTERNAL; UserId={self.user}"
            self.full_user_2 = f"INTERNAL\\{self.user}"
        self.ws_header = {"X-Qlik-User": self.full_user}
        self.ws_header_2 = {"header_user": self.full_user_2}
    def _send(self, url=None, reqs=[]):
        ws_url = self.url if url is None else url
        async def send_fetch():
            async with websockets.connect(ws_url, ssl=self.tls_ctxt, additional_headers=self.ws_header) as ws:
                for req in reqs:
                    req_json = {"jsonrpc": "2.0", "id": 1}
                    req_json["method"] = req["method"]
                    req_json["params"] = req["params"]
                    req_json["handle"] = (self.responses[int(req["handle"])]["result"]["qReturn"]["qHandle"] 
                                          if type(req["handle"]) is str
                                          else req["handle"])
                    await ws.send(json.dumps(req_json))
                    resp_raw = await ws.recv()
                    # print(resp_raw)
                    resp_dict = json.loads(resp_raw)
                    self.responses.append(resp_dict)
                    if "method" in resp_dict and resp_dict["method"] == "OnConnected":
                        resp_raw = await ws.recv()
                        # print(resp_raw)
                        resp_dict = json.loads(resp_raw)
                        self.responses.append(resp_dict)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_fetch())
        loop.close()
    def _send_6(self, url=None, reqs=[]):
        ws_url = self.url if url is None else url
        async def send_fetch():
            async with websockets.connect(ws_url, ssl=self.tls_ctxt, additional_headers=self.ws_header) as ws:
                for req in reqs:
                    req_json = {"jsonrpc": "2.0", "id": 1}
                    req_json["method"] = req["method"]
                    req_json["params"] = req["params"]
                    req_json["handle"] = (self.responses[int(req["handle"])]["result"]["qReturn"]["qHandle"] 
                                          if type(req["handle"]) is str
                                          else req["handle"])
                    if "await" in req.keys() and req["await"] == False:
                        ws.send(json.dumps(req_json))
                    else:
                        await ws.send(json.dumps(req_json))
                        resp_raw = await ws.recv()
                        print(resp_raw)
                        resp_dict = json.loads(resp_raw)
                        self.responses.append(resp_dict)
                        if "method" in resp_dict and resp_dict["method"] == "OnConnected":
                            resp_raw = await ws.recv()
                            print(resp_raw)
                            resp_dict = json.loads(resp_raw)
                            self.responses.append(resp_dict)
        asyncio.run(send_fetch())
    def _get_responses(self):
        ret_dict = {}
        for i, resp in enumerate(self.responses):
            ret_dict[i] = resp
        self.responses = []
        return ret_dict
    def _get_responses_2(self):
        ret_dict = {}
        for i, resp in enumerate(self.resps):
            ret_dict[i] = json.loads(resp)
        self.resps = []
        return ret_dict
    def get_doc_list(self):
        self._send(reqs=[{"method": "GetDocList", "handle": -1, "params": []}])
        return self._get_responses()
    def get_supported_code_pages(self):
        self._send(method="GetSupportedCodePages")
        return self._get_responses()
    def get_script(self, appid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]},
            {"method": "GetScript", "handle": "-1", "params": []}
        ])
        return self._get_responses()[2]["result"]["qScript"]
    def set_script(self, appid, script):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]},
            {"method": "SetScript", "handle": "-1", "params": [script]}
        ])
        return self._get_responses()
    def check_script_syntax(self, appid):
        self._send(url=self.url + appid, method="CheckScriptSyntax")
        return self._get_responses()
    def open_doc(self, appid):
        self._send(method="OpenDoc", params=[appid])
        return self._get_responses()
    def get_objects(self, appid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObjects", "handle": "-1", "params": [{"qTypes": ["sheet"]}]}
        ])
        return self._get_responses()
    def get_table_objects(self, appid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObjects", "handle": "-1", "params": [{"qTypes": ["table"]}]}
        ])
        return self._get_responses()
    def get_object(self, appid, objid):
        print("GET_OBJECT")
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [objid]},
            {"method": "GetProperties", "handle": "-1", "params": []}
        ])
        return self._get_responses()[3]["result"]["qProp"]
    def get_object_layout(self, appid, objid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [objid]},
            {"method": "GetLayout", "handle": "-1", "params": []}
        ])
        return self._get_responses()
    def get_child(self, appid, objectid, childid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [objectid]},
            {"method": "GetChild", "handle": "-1", "params": [childid]}
        ])
        return self._get_responses()
    def get_child_infos(self, appid, objectid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [objectid]},
            {"method": "GetChildInfos", "handle": "-1", "params": []}
        ])
        return self._get_responses()
    def get_sheet(self, appid, sheetid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [sheetid]},
            {"method": "GetFullPropertyTree", "handle": "-1", "params": []}
        ])
        return self._get_responses()
    def reload_app_wosave(self, appid):
        self._send_6(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "DoReload", "handle": "-1", "params": {"qMode": 1, "qPartial": False, "qDebug": False}, "await": False}
        ])
        return self._get_responses()
    def get_script_sync(self, appid):
        self._send_5(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]},   # "params": {"qDocName": appid}   OK
            {"method": "GetScript", "handle": "-1", "params": []}
        ])
        return self._get_responses()
    def save_app(self, appid):
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "DoSave", "handle": "-1", "params": {"qFileName": appid}}
        ])
        return self._get_responses()
    def reload_app(self, appid):
        print("RELOAD_APP")
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "DoReload", "handle": "-1", "params": {"qMode": 1, "qPartial": False, "qDebug": False}},
            {"method": "DoSave", "handle": "-2", "params": {"qFileName": appid}}
        ])
        return self._get_responses()
    def get_reload_progress(self, appid):
        self._send_6(url=self.url + appid, reqs=[
            {"method": "GetProgress", "handle": -1, "params": [0]}
        ])
        return self._get_responses()
    def create_child(self, appid, objectid, prop):
        print("CREATE_CHILD")
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [objectid]},
            {"method": "CreateChild", "handle": "-1", "params": prop},
            {"method": "DoSave", "handle": "-3", "params": {"qFileName": appid}}
        ])
        return self._get_responses()[3]["result"]["qReturn"]["qGenericId"]
    def create_object(self, appid, prop):
        print("CREATE_OBJECT")
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "CreateObject", "handle": "-1", "params": prop},            
            {"method": "DoSave", "handle": "-2", "params": {"qFileName": appid}}
        ])
        return self._get_responses()[2]["result"]["qReturn"]["qGenericId"]
    def set_properties(self, appid, objid, prop):
        print("SET_PROPERTIES")
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetObject", "handle": "-1", "params": [objid]}, 
            {"method": "SetProperties", "handle": "-1", "params": prop},         
            {"method": "DoSave", "handle": "-3", "params": {"qFileName": appid}}
        ])
        return self._get_responses()
    def get_dimension(self, appid, dimid):
        print("GET_DIMENSION")
        self._send(reqs=[
            {"method": "OpenDoc", "handle": -1, "params": [appid]}, 
            {"method": "GetDimension", "handle": "-1", "params": [dimid]}
        ])
        return self._get_responses()