# First You should run "pip install -r requirements.txt" in your shell
import wordcloud
from matplotlib import pyplot as plt

with open(input('Enter Text book file name: ')) as file:
    text = file.read()


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", "we",
                           "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                           "they", "them", "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was",
                           "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "but", "at", "by",
                           "with", "from", "here", "when", "where", "how", "all", "any", "both", "each", "few", "more",
                           "some", "such", "no", "nor", "too", "very", "can", "will", "just", "in", "on", "for", "so",
                           "not", "could"]

    # LEARNER CODE START HERE

    word_frequencies = {}

    for punctuation in punctuations:
        if punctuation in file_contents:
            file_contents = file_contents.replace(punctuation, "")  # To remove punctuations

    for word in file_contents.split():
        if word.lower() in uninteresting_words:  # To ignore uninteresting words
            continue
        else:
            if word in word_frequencies:
                word_frequencies[word] += 1
            else:
                word_frequencies[word] = 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_frequencies)
    return cloud.to_array()


# Display your wordcloud image
my_image = calculate_frequencies(text)
plt.imshow(my_image, interpolation='nearest')
plt.axis('off')
plt.savefig('WordCloud')  # To Save the figure
plt.show()
