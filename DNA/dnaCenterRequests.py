import time

import requests

def get_tocken():

    # declare useful local variables to simplify request process
    api_path = "https://sandboxdnac2.cisco.com"
    auth = ("devnetuser", "Cisco123!")
    headers = {"Content-Type": "application/json"}

    # Issue HTTP POST request to the proper URL to request token
    auth_response = requests.post(f"{api_path}/dna/system/api/v1/auth/token",
                                  auth=auth, headers=headers)

    # if successful, print token. Else, raise HTTP ERROR with details
    auth_response.raise_for_status()
    token = auth_response.json()["Token"]
    return token

def get_devices_list():
    api_path = "https://sandboxdnac2.cisco.com"
    headers = {"Content-Type": "application/json", "X-Auth-Token": f"{get_tocken()}"}
    device_response = requests.get(f"{api_path}/dna/intent/api/v1/network-device", headers=headers)
    devices = device_response.json()["response"]
    for d in devices:
        id = d["id"]
        ip = d["managementIpAddress"]
        print(f"ID:{id} , IP: {ip}")

def add_device():
    api_path = "https://sandboxdnac2.cisco.com"
    headers = {"Content-Type": "application/json", "X-Auth-Token": f"{get_tocken()}"}

    new_device_dict = {
        "ipAddress": ["192.0.2.1"],
        "snppVersion": "v2",
        "snpROCommunity": "readonly",
        "snpRWCommunity": "readwrite",
        "snpRetry": "1",
        "snmpTimeout": "60",
        "cliTransport": "ssh",
        "userName": "devnetuser",
        "Password": "Cisco123!",
        "enablePassword" : "Cisco123!"

    }

    add_resp = requests.post(f"{api_path}/dna/intent/api/v1/network-device" ,
                             json = new_device_dict,
                             headers = headers)

    if add_resp.ok:
        print(f"Request accepted: status code {add_resp.status_code}")
        time.sleep(10)

        task = add_resp.json()["response"]["taskId"]
        task_resp = requests.get(f"{api_path}/dna/intent/api/v1/task/{task}", headers=headers)


def main():
    # token = get_tocken()
    # print(token)
    # get_devices_list()
    add_device()


if __name__ == '__main__':
  main()




# import requests
# url = 'https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token'
# headers = {
#   'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
# }
# response = requests.request('POST', url, headers = headers)
# print(response.text)
#
# import requests
# url = 'https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device'
# headers = {
#   'Content-Type': 'application/json',
#   'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiI1ZTVhN2JmNDc1MTYxMjAwY2M0YWUwNjQiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVlNWE0MzI2NzUxNjEyMDBjYzRhYzk2MyJdLCJ0ZW5hbnRJZCI6IjVlNWE0MzI1NzUxNjEyMDBjYzRhYzk1YyIsImV4cCI6MTU4Njg4OTIyMCwiaWF0IjoxNTg2ODg1NjIwLCJqdGkiOiIyZmEwNjM0MS00NTRjLTRjY2ItYmY3Ny0yMjU3NDEzOTgzYTkiLCJ1c2VybmFtZSI6ImRldm5ldHVzZXIifQ.ladYzx5JUEDbPvUW0CHvKQI9Pb83Ov2PEniC5UOkJPE_GMov2H49GIbyVCBBATJGxJJ2kjQO-W8YxwLTlQVSgoJxOaBMlZ4GtlcI0zHPTmvITQQOWfP0HvmsWI4w8DDKfJQiratr5_77L9IIlKyHScwDwCDjrJQgJp_SYkzCtADwH2THzyjY59FK2Ox_rDY32mikcckbtTic6fbVhsxgVPkuE_wws2yJBf5jMXDpPKpeF7Ad3dVQFgDnjHUQtsGLSaUPrziwqYnzI2XSpmMDqlVI9hpqp49hbPpJ8THm5hZB-6YrdYYJ2Da4KgSWXjTPJ7qo5fFPpmnHJUXS_EC_UQ'
# }
# response = requests.request('GET', url, headers = headers)