import numpy as np
import keras as K
from keras.models import load_model
import tensorflow as tf

import argparse
from facebook.graphapi import api
import os
import json
import MySQLdb

def sentiment_analyzer(text):
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
    review = text
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
    # print("%0.4f" % prediction[0][0])
    return prediction[0][0]

def sentiment_analysis(text):
    sentiment = sentiment_analyzer(text)
    if sentiment < 0.3:
        return False
    return True


def delete_comment(apiObj, comment_id):
    delete_data = apiObj.delete("/" + str(comment_id))
    return delete_data["success"]


def fetch_comments(apiObj, post_data, page_id):
    try:
        # Loop through posts
        for post_datum in post_data["data"]:
            post_id = post_datum["id"]
            # print(post_datum)
            # Fetch comment of each posts
            comment_data = apiObj.get("/" + str(post_id) + "/comments")

            # Loop through comments
            for comment_datum in comment_data["data"]:
                comment_id = comment_datum["id"]
                comment_message = comment_datum["message"]
                # print(comment_id, comment_message)
                print(comment_datum)
                
                # Send for sentiment analysis
                sentiment = sentiment_analysis(comment_message)
                # If negative
                if not sentiment:            
                    # Deleting comment
                    delete_comment(apiObj, comment_id)
                
                    # Save comment to db
                    db = connect_to_db()
                    q = "INSERT INTO comment_log(page_id, date_time, comment) VALUE('" + str(page_id) + "', NOW(), '" + comment_message + "')"
                    print(q)
                    cur = db.cursor()
                    cur.execute(q)
                    db.commit()
                    db.close()

    except:
        pass
                

def fetch_posts(apiObj, page_id):
    # Fetch posts from page
    post_data = apiObj.get("/" + str(page_id) + "/posts")
    fetch_comments(apiObj, post_data, page_id)

def fetch_ads(apiObj, page_id):
    # Fetch ads from page
    post_data = apiObj.get("/" + str(page_id) + "/ads_posts")
    fetch_comments(apiObj, post_data, page_id)

def connect_to_db():
    # Fetch configuration
    config_file = os.path.join(BASE_DIR, 'config.json')
    
    with open(config_file) as json_file:
        config = json.load(json_file)
    
    db = MySQLdb.connect(host=config["host"],
                         user=config["user"],
                         passwd=config["pass"],
                         db=config["db"])
    return db

def ad_only(page_id):
    # Check in db
    db = connect_to_db()
    cur = db.cursor()
    cur.execute("select ad_only from page where page_id='" + str(page_id) + "'")

    for row in cur.fetchall():
        ad_only = int(row[0])
    
    db.close()
    
    if ad_only:
        return True
    return False

def main():
    apiObj = api()
    apiObj.set_access_token(access_token)
    apiObj.set_version("v3.3")
    
    # Check db if it is ad only
    if not ad_only(page_id):
        # Fetch post from page
        fetch_posts(apiObj, page_id)
    
    # Fetch ads from page
        fetch_ads(apiObj, page_id)

if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--access_token', help='Access Token')
    parser.add_argument('--page_id', help='Page Id')    
    args = parser.parse_args()
    
    access_token = args.access_token
    page_id = args.page_id

    # Main call
    main()
