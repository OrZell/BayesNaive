import json
import requests

class AuxiFuncs:

    @staticmethod
    def encode_dict(d: dict) -> dict:
        def encode_key(k):
            return {"__key__": str(k), "__type__": type(k).__name__}

        def encode_item(obj):
            if isinstance(obj, dict):
                return {json.dumps(encode_key(k)): encode_item(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [encode_item(x) for x in obj]
            else:
                return obj

        return encode_item(d)

    @staticmethod
    def decode_dict(d: dict):

        def decode_key(k):
            key_info = json.loads(k)
            raw = key_info["__key__"]
            t = key_info["__type__"]
            if t == "int":
                return int(raw)
            elif t == "float":
                return float(raw)
            elif t == "bool":
                return raw == "True"
            else:
                return raw  # str

        def decode_item(obj):
            if isinstance(obj, dict):
                return {decode_key(k): decode_item(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [decode_item(x) for x in obj]
            else:
                return obj

        return decode_item(d)

    @staticmethod
    def reqs(url):
        response = requests.get(url)
        status = response.status_code
        if status == 200:
            return response.json()
        else:
            raise 'Err'