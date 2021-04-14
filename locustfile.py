import json
import time
import random
from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(3, 5)
    host = "https://flask-ml-service-ikhono.azurewebsites.net:443"

    @task(1)
    def connectivity_test(self):
        self.client.get("https://flask-ml-service-ikhono.azurewebsites.net")

    @task(2)
    def prediction_test(self):
        payload = {
            "CHAS": {"0": 0},
            "RM": {"0": 6.575},
            "TAX": {"0": 296.0},
            "PTRATIO": {"0": 15.3},
            "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}
        }
        response = self.client.post(
            "/predict", json=payload, headers={'Content-Type': 'application/json'})
        time.sleep(1)
