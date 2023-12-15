import json


# функция парсинга отчета OWASP ZAP в JSON-формате
def json_parser(path_to_report, path_to_save):
    info = []
    result = {"vulnerabilities": info}
    with open(path_to_report, 'r') as file:
        data = json.load(file) # чтение данных из отчета

    # получение информации о названии уязвимости и количестве доказательств проявления
    for site in data["site"]:
        for alert in site["alerts"]:
            info.append({"name": alert["name"], "count": alert["count"]})

    with open(path_to_save + "result_of_parser.json", "w", encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False) # запись, полученной информации в JSON-формате

    print('The file (result_of_parser.json) was created successfully!')


if __name__ == '__main__':
    path_to_report = input('Enter the path to the report file (C:/ZAP/report.json): ')
    path_to_save = input('Enter the path to the directory to save the report to (C:/ZAP/): ')
    json_parser(path_to_report, path_to_save)

