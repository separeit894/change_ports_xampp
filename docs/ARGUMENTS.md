<a style="text-align: center; display: block" href="https://github.com/separeit894/change_ports_xampp">Назад на главную страницу</a>

### **--help** или **-h** 

- **Описание**: Выводит описание программы и другие аргументы, которые можно использовать
- **Примеры**: 
```bash
python main.py --help
```
```bash
python main.py -h
```

### **--version** или **-v**
- **Описание**: Выводит версию программы
- **Примеры**: 
```bash
python main.py --version
```
```bash
python main.py -v
```

### **--console** 
- **Описание**: Запускает программу в консольном режиме
- **Пример**: 
```bash
python main.py --console
```

### **--no-admin**
- **Описание**: Запускает программу, убирая возможность перезапуска с правами администратора
- **Примеры**: 
```bash
python main.py --no-admin
```
**В CLI**
```bash
python main.py --console --no-admin
```

### **-e** или **--encoding**
- **Описание**: Задаёт кодировку, в которой будут сохраняться файлы
- **Примеры**:
```bash
python main.py -e utf-8
```

или 

```bash
python main.py --encoding utf-8
```


### **--create-config**
- **Описание**: Создаёт конфигурацию со встроенными значениями. 
- **Примеры**:
```bash
python main.py --create-config
```

### **--use-config**
- **Описание**: Использует конфигурацию, файл json
- **Примеры**:

```bash
python main.py --use-config config.json 
```