import jwt
import requests
import urllib.parse
import datetime


class EfecteClient:
    _user = None
    _pass = None
    _url = None
    _token = None
    _expire = None

    def __init__(self, url):
        self._url = url

    def _get_request(self, path, params=None, full_url=False):
        headers = {'accept': 'application/json'}
        if self._token is not None:
            headers['Authorization'] = self._token
        if full_url:
            uri = path
        elif params is not None:
            encoded_params = urllib.parse.urlencode(params)
            uri = '{0}/{1}?{2}'.format(self._url, path, encoded_params)
        else:
            uri = '{0}/{1}'.format(self._url, path)
        return requests.get(uri, headers=headers)

    def _post_request_form(self, path, payload: dict):
        headers = {'accept': 'application/json'}
        if self._token is not None:
            headers['Authorization'] = self._token
        uri = '{0}/{1}'.format(self._url, path)
        return requests.post(uri, data=payload, headers=headers)

    def _post_request_json(self, path, payload: dict):
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        if self._token is not None:
            headers['Authorization'] = self._token
        uri = '{0}/{1}'.format(self._url, path)
        return requests.post(uri, json=payload, headers=headers)

    def _patch_request(self, path, payload: dict):
        headers = {
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        if self._token is not None:
            headers['Authorization'] = self._token
        uri = '{0}/{1}'.format(self._url, path)
        return requests.patch(uri, json=payload, headers=headers)

    def login(self, username, password):
        self._user = username
        self._pass = password
        return self._ensure_login()

    def _ensure_login(self):
        if self._expire is not None and self._expire > datetime.datetime.utcnow():
            return True
        if self._user is None or self._pass is None:
            raise Exception("Please login first")
        payload = {
            'login': self._user,
            'password': self._pass
        }
        r = requests.post('{0}/users/login'.format(self._url), data=payload)
        if not r.ok:
            return False
        json_response = r.json()
        token_content = json_response['token'].split(' ')
        if len(token_content) != 2 or token_content[0] != 'Bearer':
            return False
        self._token = json_response['token']
        token_data = jwt.decode(token_content[1], options={"verify_signature": False})
        self._expire = datetime.datetime.fromtimestamp(token_data['exp'])
        return True

    def echo(self, message: str) -> object:
        payload = {
            'message': message
        }
        return self._get_request("echo", payload)

    def echo_jwt(self, message: str) -> object:
        payload = {
            'message': message
        }
        self._ensure_login()
        return self._get_request("echo/jwt", payload)

    def get_templates(self):
        self._ensure_login()
        r = self._get_request("dc", None)
        if r.ok:
            return r.json()
        else:
            raise Exception("efecte returned error: {}".format(r.content))

    def get_template(self, template_code: str) -> object:
        self._ensure_login()
        r = self._get_request("dc/{}".format(template_code))
        if r.ok:
            return r.json()
        else:
            raise Exception("efecte returned error: {}".format(r.content))

    def get_datacards(self, template_code: str, filter=None, data_cards=False,
                      selected_attributes="", limit=50) -> [object]:
        self._ensure_login()
        params = {
            "filter": filter,
            "dataCards": data_cards,
            "selectedAttributes": selected_attributes
        }
        r = self._get_request("dc/{}/data".format(template_code), params=params)
        if not r.ok:
            raise Exception("efecte returned error: {}".format(r.content))
        result = list()
        data = r.json()
        result.extend(data["data"])
        while "links" in data["meta"] and "next" in data["meta"]["links"] and data["meta"]["links"]["next"] != "":
            if limit is not None and len(result) > limit:
                return result[:limit]
            self._ensure_login()
            r = self._get_request(data["meta"]["links"]["next"], full_url=True, params=params)
            if not r.ok:
                raise Exception("efecte returned error: {}".format(r.content))
            data = r.json()
            if "data" in data:
                result = result + data["data"]
        return result

    def create_datacard(self, template_code: str, folder_code: str, data: dict):
        self._ensure_login()
        params = {
            'folderCode': folder_code,
            'data': data
        }
        r = self._post_request_json(payload=params, path='dc/{0}/data'.format(template_code))
        if not r.ok:
            raise Exception("efecte returned error: {}".format(r.content))
        response_data = r.json()
        if 'dataCard' in response_data:
            return response_data['dataCard']['dataCardId']
        return None

    def update_datacard(self, template_code: str, folder_code: str, datacard_id: str, data: dict):
        self._ensure_login()
        params = {
            'folderCode': folder_code,
            'dataCardId': datacard_id,
            'data': data
        }
        r = self._patch_request(payload=params, path='dc/{0}/data/{1}'.format(template_code, datacard_id))
        if not r.ok:
            raise Exception("efecte returned error: {}".format(r.content))
        return True