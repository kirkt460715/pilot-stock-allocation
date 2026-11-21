"""核对交接文件中的来源依据。"""
import unittest
from inspect_delivery import read_table


class DeliveryTest(unittest.TestCase):
    def test_linked_records(self):
        availability = read_table("availability.json")
        sales = read_table("sales.json")
        self.assertLess({r["block"] for r in sales}, {r["block"] for r in availability})
        self.assertEqual(sum(r["block"] == "river-ring-66-14" for r in availability), 2)
        self.assertEqual(len({r["lot"] for r in read_table("dispatches.json") if r["lot"] == "L1"}), 1)
