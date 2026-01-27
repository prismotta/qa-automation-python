class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def start_checkout(self):
        self.page.click("#checkout")

    def fill_information(self, first_name, last_name, postal_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", postal_code)
        self.page.click("#continue")

    def finish(self):
        self.page.click("#finish")