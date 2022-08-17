from configparser import ConfigParser
 
 
def read_db_config(filename='config.ini', section='mysql'):
    # Парсим и читаем ini файл
    parser = ConfigParser()
    parser.read(filename)
 
    # Собираем данные в формат запроса
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))
 
    return db
