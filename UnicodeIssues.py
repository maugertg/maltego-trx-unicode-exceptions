from maltego_trx.transform import DiscoverableTransform
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform, UIM_FATAL

### Uncomment these lines to resolve the exceptions the second line sys.stdout.reconfigure(encoding="utf-8") can also be added to project.py
# import sys
# sys.stdout.reconfigure(encoding="utf-8")

class UnicodeIssues(DiscoverableTransform):
    """
    Reproduce Exceptions Unicode cp1252 encoding errors 
    Traceback (most recent call last):
      File "C:/Users/JDoe/Maltego Transforms/threatgrid/project.py", line 15, in <module>
        handle_run(__name__, sys.argv, app)
      File "C:/Users/JDoe/.virtualenvs/Maltego_Transforms-bIWLLOLO/lib/site-packages/maltego_trx/handler.py", line 25, in handle_run
        print(run_transform(transform_name, client_msg)[0])
      File "C:/Users/JDoe/AppData/Local/Programs/Python/Python39/lib/encodings/cp1252.py", line 19, in encode
        return codecs.charmap_encode(input,self.errors,encoding_table)[0]
    UnicodeEncodeError: 'charmap' codec can't encode character '/u2618' in position 662: character maps to <undefined>
    """

    @classmethod
    def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
        value = request.Value

        ### Uncomment this line to throw an exception when returning an Entity containing Unicode Character Shamrock (U+2618)
        shamrock_entity = response.addEntity("maltego.File", "☘")
        
        ### Uncomment these lines to throw an exception when returning an Entity Property containing Unicode Character Shamrock (U+2618)
        string_entity = response.addEntity("maltego.Alias", "Entity with Property")
        string_entity.addProperty("shamrock","","loose","☘")

        ### Uncomment this line to throw an exception when returning a UI Message containing Unicode Character Shamrock (U+2618)
        response.addUIMessage("☘ this will throw an exception", UIM_FATAL)
