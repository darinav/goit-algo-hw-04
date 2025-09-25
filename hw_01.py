import pathlib
import argparse
import shutil

def recursive_file_parse(source_path: pathlib.Path, destination_path: pathlib.Path):
    for item in source_path.iterdir():
        if item.is_dir():
            recursive_file_parse(item, destination_path)
        elif item.is_file():
            try:
                extension = item.suffix[1:] if item.suffix else 'no_extension'
                target_folder = destination_path / extension
                target_folder.mkdir(exist_ok=True, parents=True)

                shutil.move(str(item), str(target_folder))
            except Exception as e:
                print(f"❌ Не вдалося обробити файл {item}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Скрипт для сортування файлів.")
    parser.add_argument('source', help='Шлях до вихідної директорії')
    parser.add_argument('--destination', default='dist', help='Шлях до директорії призначення (за замовчуванням: dist)')

    args = parser.parse_args()

    source_path = pathlib.Path(args.source)
    destination_path = pathlib.Path(args.destination)

    print(f"▶️ Сортування з '{source_path}' до '{destination_path}'...")

    try:
        recursive_file_parse(source_path, destination_path)
        print(f"✅ Сортування успішно завершено!")
    except FileNotFoundError:
        print(f"❌ Помилка: Директорію '{source_path}' не знайдено.")
    except Exception as e:
        print(f"❌ Сталася непередбачувана помилка: {e}")

if __name__ == "__main__":
    main()