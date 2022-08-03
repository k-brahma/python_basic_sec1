## よくある問題(pip install に共通)

以下の類のエラーメッセージが出る場合:

```shell
(venv) PS D:\projects\python_basic_sec1> pip install tzdata
WARNING: You are using pip version 21.3.1; however, version 22.2.1 is available.
You should consider upgrading via the 'D:\projects\python_basic_sec1\venv\Scripts\python.exe -m pip install --upgrade pip' command.
```

pip のバージョンが古いです。

ほとんどの場合致命的な問題にはなりません。  
ですが、pip の動作に支障が出た場合は、 pip を upgrade します。

上記の例であれば、指定されたコマンドをそのまま実行するか

```commandline
D:\projects\python_basic_sec1\venv\Scripts\python.exe -m pip install --upgrade pip
```

あるいは、単に以下でもOKです。

```commandline
python -m pip install --upgrade pip
```

```commandline
(venv) PS D:\projects\python_basic_sec1> python -m pip install --upgrade pip
Requirement already satisfied: pip in d:\projects\python_basic_sec1\venv\lib\site-packages (21.3.1)
Collecting pip
  Downloading pip-22.2.1-py3-none-any.whl (2.0 MB)
     |████████████████████████████████| 2.0 MB 3.3 MB/s            
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.3.1
    Uninstalling pip-21.3.1:
      Successfully uninstalled pip-21.3.1
Successfully installed pip-22.2.1
```

