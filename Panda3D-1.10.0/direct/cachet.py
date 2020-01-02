import os
from datetime import datetime
import requests
import json
import certifi
import traceback

class cachet():

    def __init__(self):
        self.cachet_token = os.environ["cachet_token"]

    def report(self, method, url, value_dict):
        headers = {"Content-Type": "application/json", "X-Cachet-Token": self.cachet_token}
        req = requests.request(method=method, url=url, json=value_dict, headers=headers, verify=certifi.where())
        return req

    def report_login_time(self, milliseconds, login_metric_id):
        data = {
            "value": int(milliseconds),
            "timestamp": int(datetime.utcnow().timestamp())
        }
        req = self.report("POST", "https://status.projectalt.is/api/v1/metrics/" + str(login_metric_id) + "/points", data)
        return req

    def report_component(self, status_value, component_id):
        if status_value == self.get_component(component_id):
            print("Not updating component " + str(component_id) + " with the same value")
            return
        data = {
            "status": int(status_value)
        }
        req = self.report("PUT", "https://status.projectalt.is/api/v1/components/" + str(component_id), data)
        return req

    @staticmethod
    def get_component(component_id):
        req = requests.get("https://status.projectalt.is/api/v1/components/" + str(component_id))
        try:
            jsn = json.loads(req.text)
            return int(jsn["data"]["status"])
        except:
            print("Cachet API is dying with code " + str(req.status_code) + ": " + req.text)
            return 0