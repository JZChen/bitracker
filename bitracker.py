import rumps
import urllib
import json

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Awesome App")

    @rumps.timer(60)
    def sayhi(self, _):
        template = 'https://api.coinbase.com/v2/prices/%s/spot'
        options = ['BTC-USD','ETH-USD','LTC-USD']
        title = ''
        for option in options:
            url = template % option
            j = json.loads( urllib.urlopen( url ).read() )
            title = title + j['data']['base'] + '=' + j['data']['amount'] +' '
        self.title = title

if __name__ == "__main__":
    AwesomeStatusBarApp().run()