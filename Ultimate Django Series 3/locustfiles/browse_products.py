from locust import HttpUser, task, between
from random import randint


class WebsiteUser(HttpUser):
    #TODO -> * Viewing products * Viewing product details * Add product to cart
    
    #! This will make the tasks wait between 1 and 5 seconds before executing the next task
    wait_time = between(1, 5)
    
    #! This task numbers are weight of each task i.e their priority
    #! Higher number means higher priority
    @task(2)
    def view_products(self):
        print("View products")
        collection_id = randint(2, 6)
        self.client.get(f"/store/products/?collection_id={collection_id}", name="/store/products")

    @task(4) 
    def view_product_details(self):
        print("View product details")
        product_id = randint(1, 1000)
        self.client.get(f"/store/products/{product_id}", name="/store/products/:id")

    @task(1)
    def add_to_cart(self):
        print("Add to cart")
        product_id = randint(1, 10)
        self.client.post(f"/store/carts/{self.cart_id}/items/", name="/store/carts/items/", json={'product_id': product_id, 'quantity': 1})

    #! This is not a task but will run on start of every load test
    def on_start(self):
        response = self.client.post("/store/carts/")
        result = response.json()
        self.cart_id = result["id"]
