import unittest
from trading_bots import Bot1, Bot2, Bot3  # Assuming your trading bots are named Bot1, Bot2, Bot3

class TestTradingBots(unittest.TestCase):

    def test_bot1_functionality(self):
        bot = Bot1()
        result = bot.trade()
        self.assertIsNotNone(result)
        self.assertIn("success", result)
        
    def test_bot2_functionality(self):
        bot = Bot2()
        result = bot.trade()
        self.assertIsNotNone(result)
        self.assertGreater(result['profit'], 0)
        
    def test_bot3_functionality(self):
        bot = Bot3()
        result = bot.trade()
        self.assertIsNotNone(result)
        self.assertEqual(result['status'], "completed")

    def test_integration(self):
        bot = Bot1()
        result1 = bot.trade()
        bot2 = Bot2()
        result2 = bot2.trade(input=result1)
        self.assertGreater(result2['profit'], result1['profit'])

if __name__ == '__main__':
    unittest.main()