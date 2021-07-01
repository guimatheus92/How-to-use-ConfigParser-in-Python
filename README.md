# Obtain Power BI users and licenses from Azure through PowerShell

With this Python module, you can load a separate file with `.ini` extension.
A document repository can also be found in my profile article at [Medium](https://guimatheus92.medium.com/obtain-power-bi-users-and-licenses-from-azure-through-powershell-7f78bb4c4e21 "Medium").

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

