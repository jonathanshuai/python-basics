import numpy as np

class NaiveBayesText():
    def __init__(self):
        pass

    def fit(self, X, y):

        # make sure the number of data points matches labels
        assert len(X) == len(y)

        y = np.array(y)

        # Assume that y is from 0..n_labels - 1
        self.n_labels = y.max() + 1

        self.vocabulary = set()
        for line in X:
            for word in line:
                self.vocabulary.add(word)

        self.vocab_size = len(self.vocabulary)

        # Make a mapping from word to the index of that word
        self.word_to_index = dict(zip(self.vocabulary, range(self.vocab_size)))

        # Probabilities will hold counts first and then we'll divide later to get the real probabilities
        self.probabilities = np.ones((self.vocab_size, self.n_labels))


        for i in range(len(X)):
            label = y[i]
            for word in X[i]:
                index = self.word_to_index[word]
                self.probabilities[index, label] += 1

        self.probabilities = self.probabilities / self.probabilities.sum(axis=0) 

    def predict(self, X):
        y = np.zeros(len(X))

        for i in range(len(X)):
            current_probs = np.ones(self.n_labels)

            for word in X[i]:
                if word in self.word_to_index:
                    index = self.word_to_index[word]
                    current_probs *= self.probabilities[index]

            print(current_probs)
            y[i] = current_probs.argmax()
        return y




text_data = [
    'Chinese beijing chinese',
    'Chinese chinese shanghai',
    'Chinese Macao',
    'Tokyo Japan Chinese'
]

labels = [1, 1, 1, 0]

clean_text_data = [text.lower().split() for text in text_data]


test = 'Chinese Chinese Chinese Tokyo Japan'
clean_test = test.lower().split()



nbt = NaiveBayesText()
nbt.fit(clean_text_data, labels)
nbt.predict([clean_test])
