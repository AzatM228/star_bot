import requests
from datetime import datetime

async def get_celebrity_info(name: str):
    try:
        search_url = f"https://www.wikidata.org/w/api.php?action=wbsearchentities&search={name}&language=ru&format=json"
        search_res = requests.get(search_url).json()

        if not search_res.get("search"):
            return None

        person_id = search_res["search"][0]["id"]

        data_url = f"https://www.wikidata.org/w/api.php?action=wbgetentities&ids={person_id}&format=json&props=labels|claims"
        data = requests.get(data_url).json()

        birth_date = data["entities"][person_id]["claims"].get("P569", [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("time", "")

        if birth_date:
            birth_date = birth_date.split("T")[0].replace("-", ".").replace("+", "")

        return {
            "name": data["entities"][person_id]["labels"]["ru"]["value"],
            "birthday": birth_date or "не указана",
            "url": f"https://www.wikidata.org/wiki/{person_id}"
        }
    except Exception as e:
        print(f"Ошибка: {e}")
        return None