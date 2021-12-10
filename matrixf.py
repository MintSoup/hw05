#!/usr/bin/env python3

import json

def save_matrix(mat, path):
	with open(path, "w") as json_file:
		json.dump(mat, json_file)

def load_matrix(path):
	with open(path, "r") as json_file:
		return json.load(json_file)
