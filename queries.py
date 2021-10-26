from datetime import datetime
from pymongo.collection import Collection
from lru_cash_limit_obj import lru_cache


def create_abonent(collection: Collection, name: str, birthday: datetime = None, address: str = None, phones: list = [], emails: list = [], note: str = None):
    """Добавляет новго абонентаив базу данных

    Параметры:
    collection - объект коллекции MongoDB, входящий в базу данных
    name - имя, абонента. Обязательный параметр. При отсутствии или неверном типе данных
    функция генерирует TypeError
    birthday - необязательный параметр
    address - необязательный параметр
    phones - необязательный параметр, тип list, должен содержать строковые выражения телефонов
    emails - необязательный параметр, тип list, должен содержать строковые выражения email
    note - необязательный параметр. При записи в БД будет установлена временная метка внесения записи,
    которая будет доступна при отображении и поиске

    """
    data = {
        "name": name,
        "birthday": birthday,
        "address": address,
        "phones": phones,
        "enmails": emails,
        "notes": {
            "date": datetime.today().replace(microsecond=0),
            "text": note
        }
    }
    return collection.insert_one(data).inserted_id


@lru_cache()
def read_abonents(collection: Collection, **kwargs) -> list:

    res_list = []
    for r in collection.find(kwargs):
        res_list.append(r)

    return res_list


def delete_abonent(collection: Collection, abonents_id):
    """Удаляет записи в с id = abonents_id
    Парпметры:
    collection - объект коллекции MongoDB, входящий в базу данных
    abonents_id - обязательный. Содержит список id (type(id) == Integer) записей для удаления
    """
    return collection.delete_many({"_id": abonents_id})


def update_abonent(
        collection: Collection,
        abonent_id: int,
        **kwargs):
    """

    Обновляет данные по абоненту.
    - collection - объект коллекции MongoDB, входящий в базу данных
    - abonent_id - обязательный парпметр, должен соотвествоать первичному ключу записи в
    таблице abonent, которая должна быть обновлена. Остальные параметры - необязательны.
    Если значение других параметов c соотвествующими ключами присутствуеи в строке 
    аргументов - параметр обновляется. При передаче неизвстного ключа - возбуждается исключение на уровне 
    MongoDB
    Доступные значения ключей:
    name: str, birthday: datetime, address: str, phones: list, emails: list

    """

    return collection.update_one(
        {"_id": abonent_id},
        {"$set": kwargs}
    )
