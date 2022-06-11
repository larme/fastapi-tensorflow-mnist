from locust import HttpUser, between, task

with open("samples/0.png", "rb") as f:
    test_image_bytes = f.read()


class TensorFlow2MNISTLoadTestUser(HttpUser):

    wait_time = between(0.01, 2)

    @task
    def predict_image(self):
        files = {"file": test_image_bytes}
        self.client.post("/predict_image", files=files, timeout=1.0)
