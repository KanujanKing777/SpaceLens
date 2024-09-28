import json
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

# Step 1: Load JSON Data from multiple files
def load_json(file_paths):
    data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data.extend(json.load(file))
    return data

# Load transcription and OSD data
transcription_files = [
    './Structured Data/Outputa_OSD-379_transcription-profiling_rna-sequencing-(rna-seq)_Illumina NovaSeq.json',
    './Structured Data/Outputa_OSD-665_transcription-profiling_rna-sequencing-(rna-seq)_illumina.json'
]

osd_files = [
    './Structured Data/Outputs_OSD-379.json',
    './Structured Data/Outputs_OSD-665.json'
]

transcription_data = load_json(transcription_files)
osd_data = load_json(osd_files)

# Step 2: Preprocess Data
def preprocess_data(data):
    sentences = []
    for entry in data:
        if isinstance(entry, dict):
            for key, value in entry.items():
                sentences.append(f"{key}: {value}")
        else:
            sentences.append(str(entry))
    return sentences

transcription_sentences = preprocess_data(transcription_data)
osd_sentences = preprocess_data(osd_data)

# Tokenize the sentences
tokenizer = Tokenizer()
tokenizer.fit_on_texts(transcription_sentences + osd_sentences)

# Convert to sequences
transcription_sequences = tokenizer.texts_to_sequences(transcription_sentences)
osd_sequences = tokenizer.texts_to_sequences(osd_sentences)

# Pad sequences for uniform input shape
max_sequence_len = max(max([len(seq) for seq in transcription_sequences]),
                       max([len(seq) for seq in osd_sequences]))
transcription_sequences = pad_sequences(transcription_sequences, maxlen=max_sequence_len, padding='post')
osd_sequences = pad_sequences(osd_sequences, maxlen=max_sequence_len, padding='post')

# Step 3: Define the Model
vocab_size = len(tokenizer.word_index) + 1
embedding_dim = 100
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_sequence_len),
    LSTM(100, return_sequences=True),
    Dropout(0.2),
    LSTM(100),
    Dense(100, activation='relu'),
    Dense(vocab_size, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Step 4: Train the Model
def generate_training_data(sequences, vocab_size):
    X, y = [], []
    for seq in sequences:
        for i in range(1, len(seq)):
            X.append(seq[:i])
            y.append(seq[i])
    X = pad_sequences(X, maxlen=max_sequence_len, padding='post')
    y = tf.keras.utils.to_categorical(y, num_classes=vocab_size)
    return X, y

X_transcription, y_transcription = generate_training_data(transcription_sequences, vocab_size)
X_osd, y_osd = generate_training_data(osd_sequences, vocab_size)

# Combine both datasets for training
X_train = np.vstack((X_transcription, X_osd))
y_train = np.vstack((y_transcription, y_osd))

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=64)

# Step 5: Generate Sample Output
def generate_text(seed_text, next_words, max_sequence_len):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len, padding='post')
        predicted_probs = model.predict(token_list, verbose=0)
        predicted = np.argmax(predicted_probs, axis=-1)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text += " " + output_word
    return seed_text

# Generate new transcription and OSD data
sample_transcription = generate_text("Sample transcription seed", next_words=50, max_sequence_len=max_sequence_len)
sample_osd = generate_text("Sample OSD seed", next_words=50, max_sequence_len=max_sequence_len)

# Step 6: Save Generated Data as JSON
generated_data = {
    "generated_transcription": sample_transcription,
    "generated_osd": sample_osd
}

# Save the generated transcription and OSD data to separate JSON files
with open('generated_transcription_data.json', 'w') as transcription_file:
    json.dump({"transcription": sample_transcription}, transcription_file, indent=4)

with open('generated_osd_data.json', 'w') as osd_file:
    json.dump({"osd": sample_osd}, osd_file, indent=4)

print("Generated data has been saved to 'generated_transcription_data.json' and 'generated_osd_data.json'")
