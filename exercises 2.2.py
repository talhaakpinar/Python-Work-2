class WebPush():
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type
    def send_push(self):
        print("Push gönderildi!")
class TriggerPush(WebPush):
    trigger_page = "Category Page"
class BulkPush(WebPush):
    send_date = 624752
class SegmentPush(WebPush):
    segment_name = "new user segment"
class PriceAlertPush(WebPush):
    def discountPrice(self, price_info, Discount_rate):
        discounted_price = price_info - (price_info * Discount_rate / 100)
        return print(discounted_price)
class InstockPush(WebPush):
    def stockUpdate(self, stock_info):
        if stock_info == True:
            return print(False)
        if stock_info == False:
            return print(True)
triggerP = TriggerPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Trigger")
bulkP = BulkPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Bulk")
segmentP = SegmentPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Bulk")
priceAlertP = PriceAlertPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "Price Alert")
instockP = InstockPush("Desktop", True, 3, "12.07.2019", "12.07.2021", "English", "In Stock")
triggerP.send_push()
bulkP.send_push()
segmentP.send_push()
priceAlertP.discountPrice(250, 15.5)
priceAlertP.send_push()
instockP.stockUpdate(True)
instockP.send_push()