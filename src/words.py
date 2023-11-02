import clickhouse_connect
import re

from collections import Counter


def most_common_words():
    client = clickhouse_connect.get_client(host='localhost', username='default')
    res = client.query("SELECT title,text,topic,tags FROM dataset")

    all_text = ' '.join([row[0] for row in res.result_rows])
    words = re.findall(r'\w+', all_text.lower())

    word_counts = Counter(words)
    return word_counts.most_common(100)