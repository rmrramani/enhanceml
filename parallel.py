import time
from metaflow import FlowSpec, step

class ForeachFlow(FlowSpec):

    @step
    def start(self):
        self.data = ["Apple", "Orange"]
        self.next(self.process,foreach="data")

    @step
    def process(self):
        print(f"Processing: {self.input}")
        self.fruit = self.input
        self.score = len(self.input)
        self.next(self.join)

    @step
    def join(self, inputs):
        print(f"Choosing the best fruit")
        self.best = max(inputs, key=lambda x: x.score).fruit
        print(f"Best fruit: {self.best}")
        self.next(self.end)

    @step
    def end(self):
        pass

if __name__ == "__main__":
    ForeachFlow()


    https://idx.google.com/enhanceml-2504998
