# -*- coding: utf-8 -*-

from __future__ import print_function

import pandas as pd
import os

DB_dir = 'database'
DB_csv = 'data.csv'


class Database(object):

	def __init__(self):
		self.classes = []
		self._gen_csv()
		self.data = pd.read_csv(DB_csv)

	def _gen_csv(self):
		with open(DB_csv, 'w', encoding='UTF-8') as f:
			f.write("img,class")
			for root, _, files in os.walk(DB_dir, topdown=False):
				cls = root.split('/')[-1]
				self.classes.append(cls)
				for name in files:
					if '.jpg' not in name:
						continue
					img = os.path.join(root, name)
					f.write("\n{},{}".format(img, cls))

	def __len__(self):
		return len(self.data)

	def get_class(self):
		return self.classes

	def get_data(self):
		return self.data


if __name__ == "__main__":
	db = Database()
	data = db.get_data()
	classes = db.get_class()

	print("DB length:", len(db))
	print(classes)
	print(data.loc[data["class"] == classes[0]])