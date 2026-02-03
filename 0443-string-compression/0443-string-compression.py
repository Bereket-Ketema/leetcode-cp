class Solution:
    def compress(self, chars: list[str]) -> int:
        counter = 1
        ptr1 = 0
        ptr2 = 1

        while len(chars) > ptr2:
            # 
            if chars[ptr1] == chars[ptr2]:
                counter += 1
                chars.pop(ptr2)
            else: 
                # the case they are not equal consider counter length
                #  do inserting 
                if counter == 1:
                    ptr1 += 1
                    ptr2 += 1
                else:
                    counter = list(str(counter))
                    # iterate over counter and insert one by one
                    for dig in counter:
                        ptr1 += 1
                        chars.insert(ptr1, dig)
                    counter = 1
                    ptr1 += 1
                    ptr2 = ptr1 + 1
            
        if counter != 1:
            counter = list(str(counter))
            # iterate over counter and insert one by one
            for dig in counter:
                chars.append(dig)
        return len(chars)