import json
import random
from typing import List


def generate_versions(template: str) -> List[str]:
    parts = template.split('.')
    versions = set()

    for j in range(2):
        i = random.randint(0, 9)
        new_version = []
        for part in parts:
            if part == '*':
                new_version.append(str(i))
                ++j
            else:
                new_version.append(part)
        versions.add('.'.join(new_version))
    return list(versions)


def read_config_file(file_name: str) -> dict:
    with open(file_name, 'r') as f:
        return json.load(f)


def compare_versions(vers1: str, vers2: str) -> int:
    v1_parts = list(map(int, vers1.split('.')))
    v2_parts = list(map(int, vers2.split('.')))
    return (v1_parts > v2_parts) - (v1_parts < v2_parts)


def filter_versions(versions: List[str], version_input: str) -> List[str]:
    return [v for v in versions if compare_versions(v, version_input) < 0]


def main():
    version_input = input("Ввод версии продукта: ")
    config_file = input("Ввод имени конфигурационного файла : ")

    templates = read_config_file(config_file)
    all_versions = []

    for key, template in templates.items():
        all_versions.extend(generate_versions(template))

    all_versions = sorted(set(all_versions))

    print("Сгенерированные версии:")
    for version in all_versions:
        print(version)

    older_versions = filter_versions(all_versions, version_input)

    print("\nВерсии, которые меньше заданной:")
    for version in older_versions:
        print(version)


if __name__ == "__main__":
    main()
