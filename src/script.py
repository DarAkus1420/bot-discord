def main(version='10.9'):

    from bs4 import BeautifulSoup
    import requests

    patch = version[0:2] + '-' + version[3:]

    base_url = f"https://las.leagueoflegends.com/es-ar/news/game-updates/notas-de-la-version-{patch}"
    base2_url = f"https://las.leagueoflegends.com/es-ar/news/game-updates/patch-{patch}-notes/"

    

    result = requests.get((base_url))

    # print(src)

    soup = BeautifulSoup(result.content, 'html.parser')

    error = soup.find_all("p", text="The page you were looking for was not found.")
    if error:
        result2 = requests.get((base2_url))
        soup = BeautifulSoup(result2.content, 'html.parser')

    images = soup.find_all("a", {"class": "skins cboxElement"})

    image_url = images[0].find('img')['src']
    return (image_url)


if __name__ == '__main__':
    main()
    