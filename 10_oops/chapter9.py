# Static Methods In Python
# When u want utility methods grouped with your class but u want them to be independent of an object.

class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        # creating a list of words from a text msg after removing any spaces surrounding the word.
        return [item.strip() for item in text.split(",")]
    
raw="water , milk  , ginger,     honey"
# obj=ChaiUtils
# print(obj.clean_ingredients(raw))

cleaned=ChaiUtils.clean_ingredients(raw)
print(cleaned)