class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []
            
        in_len = len(words[0])
        total_words = len(words)
        total_len = in_len * total_words
        answer = []
        
        # 1. Build original frequency map
        check = {}
        for word in words:
            if word not in check:
                check[word] = 1
            else:
                check[word] = check[word] + 1
                
        # 2. Outer Loop: Slide 'left' character by character as the window ANCHOR
        for left in range(len(s) - total_len + 1):
            
            # Create a true, fresh copy of your counts for THIS window attempt
            current_check = check.copy()
            words_matched = 0
            
            # 3. Inner Loop: Use an independent tracker to read word chunks
            for i in range(total_words):
                start_idx = left + (i * in_len)
                chunk = s[start_idx : start_idx + in_len]
                
                # If the chunk matches our map and we still need it, count it
                if chunk in current_check and current_check[chunk] > 0:
                    current_check[chunk] = current_check[chunk] - 1
                    words_matched = words_matched + 1
                else:
                    # Invalid word or ran out of copies -> break this attempt early
                    break
            
            # 4. Success check
            if words_matched == total_words:
                answer.append(left)
                
        return answer
