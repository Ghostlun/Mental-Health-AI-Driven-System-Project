counsel_df = pd.read_csv("counselchat-data.csv")

from collections import Counter

print("Orignal length" + str(len(counsel_df)))
counsel_df = counsel_df[['questionText', 'topics','answerText']]
all_words = ' '.join(counsel_df['topics'].astype(str)).replace(',', '').split()

# Count the frequency of each word
word_count = Counter(all_words)

# ['Panic Disorder' 'Depression' 'Anxiety' 'Burnout' 'Stress']

import nltk
from nltk.corpus import wordnet

# Ensure you've downloaded the WordNet corpus

# Display the word frequencies
print("\nWord frequencies in the 'topics' column:")
found_selected_count = 0
stress_count = 0
depression_count = 0
disorder_count = 0
anxiety_count = 0
burn_out_count = 0
for word, count in word_count.items():
    
    if word.__contains__("Stress"):
        stress_count +=count
    elif word.__contains__("Depression"):
        depression_count += count
    elif word.__contains__("Disorder"):
        disorder_count += count
    elif word.__contains__("Anxiety"):
        anxiety_count += count
    elif word.__contains__("Burnout"):
        burn_out_count += count
    else:
        print(f"{word} :  {count}")
found_selected_count = stress_count + depression_count + disorder_count + anxiety_count
print("total counts" + str(len(counsel_df)))
print("stress_count", stress_count)
print("depression_count", depression_count)
print("disorder_count", disorder_count)
print("anxiety_count", anxiety_count)
print("burn_out_count", burn_out_count)
print("Found selcted count", found_selected_count)

counsel_df[['topics']]