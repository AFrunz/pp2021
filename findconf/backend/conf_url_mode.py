def conf_url_update(theme_value, keywords):
    url_f = "https://konferencii.ru/search?advance%5Bkeyword%5D="
    url_s = "&advance%5BsearchOr%5D=1&advance%5BstartDate%5D=&advance_startDate=&advance%5BendDate%5D=&advance_endDate=&advance%5Bbackup%5D=1&advance%5BlastRequestDate1%5D=&advance_lastRequestDate1=&advance%5BlastRequestDate2%5D=&advance_lastRequestDate2=&advance%5BcountryId%5D=&advance%5BcityId%5D=&advance%5BeventId%5D=&advance%5BtopicId%5D%5B%5D="
    url_t = "&advance%5BparticalId%5D=&advance%5BorderBy%5D=startDate&advance%5Blimit%5D=20&submit=Искать"
    znaki = [",", ";", "!", "?", ":"]
    for i in znaki:
        keywords = keywords.replace(i, " ")
    keywords = keywords.replace(" ", "+")
    url = url_f+keywords+url_s+theme_value+url_t
    print(url)
    return url
conf_url_update("40","математика")
