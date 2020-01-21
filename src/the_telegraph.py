import os

import src.utils as utils

website_base_url = "https://www.telegraph.co.uk"
website_url = website_base_url + "/brexit/page-"
number_of_pages = 367


def get_body_content(body):
    content = ""

    for paragraph in body.select("p"):
        content += "\n" + paragraph.get_text()

    return content


def start():
    articles = []

    utils.progress(0)

    for page_number in range(1, number_of_pages + 1):
        main_page = utils.scrape_page(website_url + str(page_number))

        article_anchors = main_page.select("article a.list-headline__link")

        for j, article_anchor in enumerate(article_anchors):
            article_url = article_anchor.get('href')
            article_url = website_base_url + article_url

            article_page = utils.scrape_page(article_url)

            article_title = article_page.select_one("h1.headline__heading").get_text()
            article_body = get_body_content(article_page.select_one("article"))

            article_date = article_page.select_one(".article-date time")["datetime"]

            articles.append({
                "title": article_title,
                "content": article_body,
                "url": article_url,
                "date": article_date
            })

        utils.progress(page_number / number_of_pages * 100)

    # Save all articles in a file.
    utils.save_data(os.path.splitext(os.path.basename(__file__))[0], articles)