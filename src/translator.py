import deepl
import os
from comparer import comparer
import dotenv
# Load environment variables from .env file
dotenv.load_dotenv()

class translator:     
    def __init__(self, file1, file2):
        self.file1 = file1  
        self.file2 = file2

    def translate_diffs(self):
        import json
        # Get language code from the first two characters of file2's name (without path)
        target_language = os.path.basename(self.file2)[:2].upper()
        translator = deepl.DeepLClient(os.getenv("YOUR_DEEPL_API_KEY"))
        # Find keys missing in file2
        _, missing_keys = comparer(file1=self.file1, file2=self.file2).missing()
        print(missing_keys)
        # Load file1 as dict
        with open(self.file1, 'r', encoding='utf-8') as f:
            data1 = json.load(f)
        translations = {}
        for key in missing_keys:
            value = data1.get(key)
            print(value)
            if value:
                translated_text = translator.translate_text(value, target_lang=target_language)
                translations[key] = translated_text.text
        return translations

print(translator('en.json', 'de.json').translate_diffs())