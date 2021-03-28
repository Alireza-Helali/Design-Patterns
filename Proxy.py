"""
Proxy:
        Proxy is a structural design pattern that provides
        an object that acts as a substitute for a real
        service object used by a client. A proxy receives
        client requests, does some work(access control,
        caching, etc.) and then passes the request to a
        service object.
"""


class Car:
    def __init__(self, driver):
        self.driver = driver

    def drive(self):
        return f'car is driven by {self.driver.name}'


class CarProxy:
    def __init__(self, driver):
        self.driver = driver
        self._car = Car(self.driver)

    def drive(self):
        if self.driver.age > 16:
            return self._car.drive()
        else:
            return 'Driver too young to drive a car!'


class Driver:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    # driver = Driver('alireza', 25)
    # car = Car(driver)
    # print(car.drive())
    driver = Driver('alireza', 15)
    car = CarProxy(driver)
    print(car.drive())
