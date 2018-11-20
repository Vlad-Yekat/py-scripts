"""
self def with
"""


class SayUgu:
    def __init__(self, result):
        self.result = result

    def __enter__(self):
        self.result += 1
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.result = 0


with SayUgu(1) as su:
    print(su*su)



