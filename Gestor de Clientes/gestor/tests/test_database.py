import copy
import unittest
import database as db
import helpers
import csv
import config

class TestDatabase(unittest.TestCase):

    def setUp(self):
        #se ejecuta antes de cada prueba
        db.Cliente('15J', 'Marta', 'Pérez'),
        db.Cliente('48H', 'Manolo', 'López'),
        db.Cliente('28Z', 'Ana', 'García')