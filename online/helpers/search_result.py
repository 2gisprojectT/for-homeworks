from online.helpers.base_component import BaseComponent


class SearchResult(BaseComponent):

    selectors = {
        'self': '.searchResults__list',
        'count': '//*[@id="module-1-9-1-1"]/nav/div[2]/div[2]'
    }

    @property
    def count(self):
        return self.driver.find_element_by_xpath(self.selectors['count']).text