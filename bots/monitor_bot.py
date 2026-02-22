import time
import requests

class MonitorBot:
    def __init__(self, symbol, alert_threshold):
        self.symbol = symbol
        self.alert_threshold = alert_threshold
        self.url = f'https://api.example.com/marketdata/{symbol}'  # Placeholder URL

    def get_price(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            data = response.json()
            return data['price']
        else:
            print('Error fetching price data')
            return None

    def check_price(self):
        price = self.get_price()
        if price is not None:
            print(f'Current price of {self.symbol}: ${price}')
            if price >= self.alert_threshold:
                self.send_alert(price)

    def send_alert(self, price):
        print(f'ALERT: {self.symbol} has reached the alert threshold! Current price: ${price}')

    def start_monitoring(self, interval):
        while True:
            self.check_price()
            time.sleep(interval)

if __name__ == '__main__':
    bot = MonitorBot('BTC', 30000)
    bot.start_monitoring(60)  # Check price every minute