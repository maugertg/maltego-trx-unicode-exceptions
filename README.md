# Issue
Passing Unicode to Maltego TRX Python Library when running local transforms in Windows results in an exception:

```
Traceback (most recent call last):
  File "C:/Users/JDoe/Maltego Transforms/threatgrid/project.py", line 15, in <module>
    handle_run(__name__, sys.argv, app)
  File "C:/Users/JDoe/.virtualenvs/Maltego_Transforms-bIWLLOLO/lib/site-packages/maltego_trx/handler.py", line 25, in handle_run
    print(run_transform(transform_name, client_msg)[0])
  File "C:/Users/JDoe/AppData/Local/Programs/Python/Python39/lib/encodings/cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
UnicodeEncodeError: 'charmap' codec can't encode character '/u2618' in position 662: character maps to <undefined>
```

# Cause
The issue appears to be related to the way Python gets the encoding from the environment. Most of the time it will default to UTF-8 but there are instances when launching the termina/cli/command prompt it will end up using Windows-1252 / cp1252.

# Possible Solutions
## Set UTF-8 environment variable
Setting `PYTHONUTF8=1` environment variable forces UTF-8 encoding and resolves the issue

## Set encoding using IO
Placing this in the project.py, handler.py, or transform file resolves the issue and is compatible with Python version < 3.7
```
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
```

## Reconfigure STDOUT encoding Python 3.7+
Starting in Python 3.7 it is possible to call `reconfigure` to set the STDOUT encoding
```
import sys
sys.stdout.reconfigure(encoding="utf-8")
```
