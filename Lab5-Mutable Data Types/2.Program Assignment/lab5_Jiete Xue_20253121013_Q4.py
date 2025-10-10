def top_3_frequency_words(file):
    word_frequency = {}
    with open(file, "r") as f:
        for line in f:
            words = line.split()
            for word in words:
                if word in word_frequency:
                    word_frequency[word] += 1
                else:
                    word_frequency[word] = 1
    sorted_word_frequency = sorted(word_frequency.items(), key=lambda x: x[1], reverse=True)
    return sorted_word_frequency[:3]


print(top_3_frequency_words('article.txt'))