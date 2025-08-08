# src/comparer.py
# Comparer object
# Attributes:
# - file1: path to the first file
# - file2: path to the second file
# Methods:
# - compare: compares the contents of the two files and returns a message indicating if they are identical or different
# - diffs: returns a dictionary of differences between the two files, with keys the differing keys and values the differing values. If an element is present in one file but not the other, it is included with a value of None for the missing file.
# - missing: returns a list of only keys that are present in one file but not the other
# - translate_diffs: translates the differences into a specified language using the Deepl translation API
class comparer(object):
    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def compare(self):
        with open(self.file1, 'r') as f1, open(self.file2, 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()
            if content1 == content2:
                return "Files are identical."
            else:
                return "Files are different."
    
    def diffs(self):
        with open(self.file1, 'r', encoding='utf-8') as f1, open(self.file2, 'r', encoding='utf-8') as f2:
            content1 = sorted(f1.read().splitlines())
            content2 = sorted(f2.read().splitlines())
            diff_dict = {}
            i, j = 0, 0
            while i < len(content1) and j < len(content2):
                if content1[i] == content2[j]:
                    i += 1
                    j += 1
                elif content1[i] < content2[j]:
                    diff_dict[content1[i]] = None
                    i += 1
                else:
                    diff_dict[None] = content2[j]
                    j += 1
                # Add remaining lines
            while i < len(content1):
                diff_dict[content1[i]] = None
                i += 1
            while j < len(content2):
                diff_dict[None] = content2[j]
                j += 1
            return diff_dict
    def missing(self):
        with open(self.file1, 'r', encoding='utf-8') as f1, open(self.file2, 'r', encoding='utf-8') as f2:
            import json
            data1 = json.load(f1)
            data2 = json.load(f2)
            keys1 = set(data1.keys())
            keys2 = set(data2.keys())
            missing_in_file1 = keys2 - keys1
            missing_in_file2 = keys1 - keys2
            return list(missing_in_file1), list(missing_in_file2)
    

