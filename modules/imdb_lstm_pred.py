import numpy as np
import keras as K
from keras.models import load_model
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

def main():
    np.random.seed(1)
    tf.set_random_seed(1)

    max_words = 20000

    max_review_len = 80

    e_init = K.initializers.RandomUniform(-0.01, 0.01, seed=1)
    init = K.initializers.glorot_uniform(seed=1)
    simple_adam = K.optimizers.Adam()
    embed_vec_len = 32    # values per word -- 100-500 is typical

    model = K.models.Sequential()
    model.add(K.layers.embeddings.Embedding(input_dim=max_words,
        output_dim=embed_vec_len, embeddings_initializer=e_init,
        mask_zero=True))
    model.add(K.layers.LSTM(units=100, kernel_initializer=init,
        dropout=0.2, recurrent_dropout=0.2))    # 100 memory
    model.add(K.layers.Dense(units=1, kernel_initializer=init,
        activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=simple_adam,
        metrics=['acc'])


    mp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "Models", "imdb_model.h5")
    model = load_model(mp)


    d = K.datasets.imdb.get_word_index()
    review = "I loved the movie very much"
    words = review.split()
    review = []
    for word in words:
        if word not in d: 
            review.append(2)
        else:
            review.append(d[word]+3)
    review = K.preprocessing.sequence.pad_sequences([review],
        truncating='pre',    padding='pre', maxlen=max_review_len)

    prediction = model.predict(review)
    print("%0.4f" % prediction[0][0])


if __name__ == "__main__":
    main()
