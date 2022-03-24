import requests
import json


def publications_list():
    my_api_token = "Token 1c78af92d5738971f4f5b45b8e315d4bd8da41bd"

    publications = "https://publons.com/api/v2/academic/publication/?academic=J-5196-2018"

    header = {"Authorization": my_api_token}
    response = requests.get(publications, headers=header)
    publications_data = response.json()
    results = publications_data["results"]
    publication_list = ''
    number = 0
    for i in results:
        # for l in results:
        journal = (i["journal"]["name"])
        title = (i["publication"]["title"])
        date = (i["publication"]["date_published"])[0:4]  # слайс от строки с датой
        # year = (i)
        number += 1
        publication_list += f"{number}).{title}, {journal}, {date}\n"

    return publication_list


#print(publications_list())

# print(publications_data_)
