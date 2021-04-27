class WebGraph:
    def __init__(self):
        self.pages = {}
    
    def add_page(self, new_page):
        self.pages[new_page.title] = new_page

class Page:
    def __init__(self, title):
        # Page title
        self.title = title

        # Outbound connections 
        self.links = {}

    def add_link(self, title):        
        if not title in self.links:
            self.links[title] = 1
        else:
            self.links[title] += 1

    