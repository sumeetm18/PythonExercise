class LongNameDict(dict):
    def longest_key(self):
        longest = None
        for key in self:
            if not longest or len(key) > len(longest):
                longest = key
        return longest

longdict=LongNameDict()
longdict["Hi"]=1
longdict["Hello"]=2
longdict["Hello world"]=2
print(longdict.longest_key())