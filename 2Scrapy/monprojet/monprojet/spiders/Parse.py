def parse_category(self, response):
    for article in response.css(".river")[0].css(".teaser"):
        title = self.clean_spaces(article.css("h3::text").extract_first())
        image = article.css("img::attr(data-src)").extract_first()
        description = article.css("p::text").extract_first()
        yield {
            "title": title,
            "image": image,
            "description": description
        }