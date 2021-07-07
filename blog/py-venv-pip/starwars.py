import requests


def main():
    base_url = "https://swapi.dev/api/"
    search_url = "people/?search="

    r = requests.get(f"{base_url}{search_url}vader")
    print(f"status: {r.status_code}")
    print(r.json())


if __name__ == "__main__":
    main()
