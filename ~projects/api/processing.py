
def file_to_list(str):
    words = str.split()
    words = [word.lower() for word in words]
    return words

def strip_punctuation(ls, punc):
    for x in range(len(ls)):
        if ls[x].endswith(punc):
            ls[x] = ls[x].strip(punc)
    return ls

def strip_multiple(list):
    strip_words = ["n't", ",", ".", "'ll"]
    for f in strip_words:
        list = strip_punctuation(list, f)
    return list

def stop_words(list):

    stopwords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
    list = [x for x in list if x not in stopwords]
    return list

def jaccard_simmilarity(ls1, ls2):
    set1 = set(ls1)
    set2 = set(ls2)
    intersect = set1.intersection(set2)
    return float(len(intersect)) / (len(set1) + len(set2) - len(intersect))

def final(str1, str2):
    try:
        str_list1 = file_to_list(str1)
        str_list2 = file_to_list(str2)
        str_list1 =strip_multiple(str_list1)
        str_list2 =strip_multiple(str_list2)
        fin_list1 =  stop_words(str_list1)
        fin_list2 = stop_words(str_list2)
        metric = jaccard_simmilarity(fin_list1, fin_list2)
        return metric
    except:
        "Please pass two strings"
