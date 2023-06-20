import time


def timer(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        stop_time = time.time()
        dt = stop_time - start_time
        print(f"Δt = {dt}")

    return wrapper


class Utils:
    GENERIC_TOKEN = "$%$"

    @staticmethod
    def waste_some_time(waiting_time=.1):
        time.sleep(waiting_time)

    def make_required_byString(self, selector_definition, dynamic_selector_text=""):
        selector_definition = selector_definition.replace(self.GENERIC_TOKEN, dynamic_selector_text)
        if "CSS:" in selector_definition:
            return {"By": "css selector", "custom_selector": selector_definition.replace("CSS:", "")}
        if "ID:" in selector_definition:
            return {"By": "css selector", "custom_selector": selector_definition.replace("ID:", "#")}
        if "XPATH:" in selector_definition:
            return {"By": "xpath", "custom_selector": selector_definition.replace("XPATH:", "")}
        if "NAME:" in selector_definition:
            return {"By": "xpath", "custom_selector": selector_definition.replace("NAME:", "//*[@name='") + "']"}
        if "LINK_TEXT:" in selector_definition:
            return {"By": "xpath", "custom_selector": selector_definition.replace("LINK_TEXT:",
                                                                                  "//a[contains(text(),'") + "']"}
