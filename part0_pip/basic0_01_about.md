# pip とは

[pypi](https://pypi.org/) に登録されている python パッケージをインストール/アンインストールするためのツール

***

# インストールの構文

```commandline
pip install openpyxl
```

すると、指定したライブラリが依存する別のライブラリも同時にインストールされる。  
以下では、 et-xmlfile もインストールされた。

```commandline
(venv) PS D:\projects\python_basic_sec1> pip install openpyxl
Collecting openpyxl
  Using cached openpyxl-3.0.10-py2.py3-none-any.whl (242 kB)
Collecting et-xmlfile
  Using cached et_xmlfile-1.1.0-py3-none-any.whl (4.7 kB)
Installing collected packages: et-xmlfile, openpyxl
Successfully installed et-xmlfile-1.1.0 openpyxl-3.0.10
```

複数を同時にインストールすることも可能

```commandline
pip install openpyxl urllib3 
```

バージョンを指定できる  
(イコールの数に注意！)

```commandline
pip install urllib3==1.26.11
```

***

# アンインストールの構文

```commandline
pip uninstall openpyxl
```

以下は例。  
アンインストール時に、確認を求められる。

```commandline
(venv) PS D:\projects\python_basic_sec1> pip uninstall openpyxl
Found existing installation: openpyxl 3.0.10
Uninstalling openpyxl-3.0.10:
  Would remove:
    d:\projects\python_basic_sec1\venv\lib\site-packages\openpyxl-3.0.10.dist-info\*
    d:\projects\python_basic_sec1\venv\lib\site-packages\openpyxl\*
Proceed (Y/n)? y
  Successfully uninstalled openpyxl-3.0.10
```

-y オプションをつけると、確認を求められなくなる。

```commandline
(venv) PS D:\projects\python_basic_sec1> pip uninstall urllib3 -y
Found existing installation: urllib3 1.26.11
Uninstalling urllib3-1.26.11:
  Successfully uninstalled urllib3-1.26.11
```

***

インストール済ライブラリのリストを出力できる

```commandline
(venv) PS D:\projects\python_basic_sec1> pip freeze -l
et-xmlfile==1.1.0
openpyxl==3.0.10
urllib3==1.26.11
```

(コマンドに共通のことだが)出力先としてテキストファイル等を指定できる。  
以下では、 requirements.txt というファイルにリストを出力する。

```commandline
pip freeze -l > requirements.txt
```

requirements.txt に載っているライブラリを一気に導入してみよう。  
-r オプションを使う。

```commandline
pip install -r requirements.txt
```
