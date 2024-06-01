import unittest
from client3 import *

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]


    actual1 = getDataPoint(quotes[0])
    actual2 = getDataPoint(quotes[1])
    expected1 = ('ABC', 120.48, 121.2 , 120.84)
    expected2 = ('DEF', 117.87, 121.68, 119.775)

    assert actual1 == expected1
    assert actual2 == expected2

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    actual3 = getDataPoint(quotes[0])
    actual4 = getDataPoint(quotes[1])

    expected3 = ('ABC', 120.48, 119.2 , 119.84)
    expected4 = ('DEF', 117.87, 121.68, 119.775)
    assert actual3 == expected3
    assert actual4 == expected4
  def test_getRatio_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price1 = getDataPoint(quotes[0])[3]
    price2 = getDataPoint(quotes[1])[3]
    actual = getRatio(price1,price2)
    expected = 1.008891671884784

    assert actual == expected




if __name__ == '__main__':
    unittest.main()
