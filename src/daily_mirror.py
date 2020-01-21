import os

import src.utils as utils

website_url = "https://www.mirror.co.uk/all-about/brexit?pageNumber="
number_of_pages = 300


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

        article_anchors = main_page.select(".teaser a.headline")

        for j, article_anchor in enumerate(article_anchors):
            article_url = article_anchor.get('href')

            article_page = utils.scrape_page(article_url)

            article_title = article_page.select_one("h1.section-theme-background-indicator").get_text()
            article_body = get_body_content(article_page.select_one(".article-body"))

            article_date = article_page.select_one(".date-published")["datetime"]

            articles.append({
                "title": article_title,
                "content": article_body,
                "url": article_url,
                "date": article_date
            })

        utils.progress(page_number / number_of_pages * 100)

    # Save all articles in a file.
    utils.save_data(os.path.splitext(os.path.basename(__file__))[0], articles)