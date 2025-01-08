# ---Imports---

import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Embedding


# ---Function to build the Seq2Seq model---

"""
This function builds a sequence-to-sequence (Seq2Seq) model using LSTM.
    
Parameters:
    - input_vocab_size: Number of unique words in the source language
    - output_vocab_size: Number of unique words in the target language
    - latent_dim: Dimensionality of the LSTM hidden layers (default 256)
    
Returns:
    - model: A compiled Seq2Seq model
"""

          
def build_model(input_vocab_size, output_vocab_size, latent_dim=256):
    
    # Encoder
    encoder_inputs = Input(shape=(None,))
    encoder_embedding = Embedding(input_vocab_size, latent_dim)(encoder_inputs)
    encoder_lstm = LSTM(latent_dim, return_state=True)
    encoder_outputs, state_h, state_c = encoder_lstm(encoder_embedding)
    encoder_states = [state_h, state_c]
    
    # Decoder
    decoder_inputs = Input(shape=(None,))
    decoder_embedding = Embedding(output_vocab_size, latent_dim)(decoder_inputs)
    decoder_lstm = LSTM(latent_dim, return_sequence=True, return_state=True)
    decoder_outputs, _, _ = decoder_lstm(decoder_embedding, initial_state=encoder_states)
    decoder_dense = Dense(output_vocab_size, activation='softmax')
    decoder_outputs = decoder_dense(decoder_outputs)
    
    # Model
    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
