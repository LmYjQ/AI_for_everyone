import yaml
import random
import pandas as pd

class FakeDataGenerator(object):
    def __init__(self, conf_file):
        with open(conf_file, 'r') as f:
            self.conf = yaml.load(f)
        self.data = self._make_fake_data()

    def _make_fake_data(self):
        data = {}
        self.num = int(self.conf['num_samples'])
        data['label'] = self._random_col(self.conf['label'])
        for field, value_str in self.conf['fields'].items():
            data[field] = self._random_col(value_str)
        print(data)
        return data

   # 随机产生一列数据，离散或连续
    def _random_col(self, value_str):
        if ',' in value_str:  # discrete
            value_set = value_str.split(',')
            return [int(random.choice(value_set)) for i in range(self.num) ]
        else: # continuous
            value_set = value_str.split('-')
            return [random.uniform(int(value_set[0]), int(value_set[1])) for i in range(self.num)]

    def get_dataframe():
        pass


if __name__=='__main__':
    fdg = FakeDataGenerator('./conf/classification.yaml')
    fdg._make_fake_data()
