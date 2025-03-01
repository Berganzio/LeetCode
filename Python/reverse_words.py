class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # take the string and split it into words
        words = s.split()
        # reverse the words
        words = words[::-1]
        # join the words back together
        return ' '.join(words)