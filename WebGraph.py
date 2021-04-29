class WebGraph:
    def __init__(self):
        self.pages = {}
        self.url_set = set()
    
    def add_page(self, new_page):
        # ignore duplicate visits
        if new_page.title in self.pages:
            return None

        self.pages[new_page.title] = new_page
        novel_links = []
        for link in new_page.links:
            if link not in self.url_set:
                self.url_set.add(link)
                novel_links.append(link)
        return novel_links

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

    