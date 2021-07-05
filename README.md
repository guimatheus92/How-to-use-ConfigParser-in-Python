# How to use ConfigParser in Python

With this Python module, you can load a separate file with `.ini` extension.
A document repository can also be found in my profile article at [Medium](https://guimatheus92.medium.com/how-to-use-configparser-in-python-with-ini-file-3c2739a43d80 "Medium").

------------

The first step is to install configparser module on Python:
```python
 pip install configparser 
```

The second step is to change your `.ini` file with the variables you need

If you want, you can change the folder where you want to upload your `.ini` file
```python
config.read(r'EnvVariables.ini')
```

