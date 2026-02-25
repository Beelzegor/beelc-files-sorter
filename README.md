# 🗂️ Beelc's Files Sorter v1.0.0

Beelc's Files Sorter es un programa de automatización de archivos que resuelve el problema de tener un gran número de archivos en la carpeta de descargas, ahorrando tiempo buscando archivos de forma desordenada.

---

## 📸 Demo

![Demo](assets/demo.png)

---

## 🛠️ Tecnologías

- Python
- CustomTkinter
- Watchdog
- Logging
- pystray
- PIL

---

## 📦 Instalación

Descarga el `.rar` desde la sección de [Releases](https://github.com/Beelzegor/beelc-files-sorter/releases) y extrae los archivos.
Tendrás dos archivos, un .exe y un .json, estos dos archivos son obligatorios para el correcto funcionamiento del programa.
No necesitas tener Python instalado.

---

## 🚀 Uso

1. Abre el programa
2. Selecciona una carpeta destino con **Select Destination Folder**
3. Presiona **Start Sorting**
4. El programa correrá en segundo plano, incluso si cierras la ventana

Todo lo que llegue a tu carpeta de Descargas será clasificado automáticamente en subcarpetas dentro de tu carpeta destino.

---

## 📁 Estructura del proyecto
```
BFS/
├── src/
│   ├── app.py
│   ├── watcher.py
│   ├── sorter.py
│   └── logger.py
├── config.json
├── logs/
├── requirements.txt
└── README.md
```

---

## ⚙️ Extensiones soportadas

| Extensión | Carpeta destino |
|-----------|----------------|
| `.pdf` | PDF |
| `.docx` | Docs |
| `.mp3` | Audio |
| `.mp4` | Video |
| `.png` | Images |
| `.pptx` | Presentations |
| `.txt` | Text |
| `.exe` | Apps |
| `.rar` | Compressed |
