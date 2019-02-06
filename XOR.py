import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import SGD



x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])
sgd = SGD(lr=0.5)
model = Sequential()
model.add(Dense(20, activation='tanh', input_dim=2))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer=sgd, loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x, y, epochs=500)
print(model.predict(x))