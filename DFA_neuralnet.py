import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense


# Load your data
data = pd.read_csv('test_DFA_data.csv')

# Extract features and labels
texts = data.iloc[:, 0].astype(str).tolist()
labels = data.iloc[:, 1].tolist()

# Convert texts to ASCII values and pad sequences
max_length = max(len(text) for text in texts)

def text_to_ascii(text, max_length):
    ascii_values = [ord(char) for char in text]
    return ascii_values + [0] * (max_length - len(ascii_values))

X = np.array([text_to_ascii(text, max_length) for text in texts])
y = np.array(labels)

# Split the data into training and testing sets manually
split_fraction = 0.8
split_index = int(len(X) * split_fraction)

X_train, X_test = X[:split_index], X[split_index:]
y_train, y_test = y[:split_index], y[split_index:]


# Parameters
vocab_size = 128  # ASCII values range from 0 to 127
embedding_dim = 50

# Build the model
model = Sequential([
    Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Summarize the model
model.summary()

# Train the model
history = model.fit(X_train, y_train, epochs=10, validation_split=0.2, batch_size=32)


# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy:.4f}')


# Function to predict if a string is in the language
def predict_language_membership(text):
    ascii_values = text_to_ascii(text, max_length)
    input_array = np.array([ascii_values])
    prediction = model.predict(input_array)
    return prediction[0][0] > 0.5



option = input("Would you like to test a word (Y or N): ")

while option == 'y' or option == 'Y':
    print(predict_language_membership(input("What string would you like to test: ")))
    option = input("Would you like to test another word (Y or N): ")
    
    


