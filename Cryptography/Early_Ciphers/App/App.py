import importlib, re
validator = "^[ a-z]{,}$"


list_modules = {
    'Ciesar',
    'Vigener',
    'Vernam',
    'Permutation',
    'Substituting',
}

def setup_app(list_modules_):
    # Load modules for supported services.
    modules = {module_name: importlib.import_module(name='.utils', package=f'modules.{module_name}')
               for module_name in list_modules_}

    return modules


MODULES = setup_app(list_modules)

while True:
    print("\nОберіть модуль: ", list_modules, '. або введіть exit')
    name = input()
    if name == 'exit':
        break

    if name not in MODULES:
        print('Невірно введена назва модулю')
        continue

    while True:
        print("\n\tЗашифрувати(1), Розшифрувати(2), Згенерувати новий ключ(3), Вихід(4)")
        d = input()
        if d == '1':
            MODULES[name].Cipher()
        elif d == '2':
            MODULES[name].Uncipher()
        elif d == '3':
            MODULES[name].Generate_Key()
        elif d == '4':
            break
        else:
            print('\tПовторіть ввод')
            continue


