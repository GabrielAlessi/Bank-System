import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Criar dados fictícios para o modelo
X = np.random.rand(1000, 5)
y = np.random.randint(2, size=1000)

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Criar o modelo de rede neural
model = Sequential()
model.add(Dense(12, input_dim=5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compilar o modelo
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Treinar o modelo
model.fit(X_train, y_train, epochs=10, batch_size=10)

# Avaliar o modelo no conjunto de teste
loss, accuracy = model.evaluate(X_test, y_test)
print(f'Acurácia no conjunto de teste: {accuracy*100:.2f}%')

# Função para prever se uma transação é fraudulenta
def predizer_fraude(transacao):
    transacao = np.array(transacao)
    transacao = scaler.transform([transacao])
    predicao = model.predict(transacao)
    return bool(predicao > 0.5)

# Exemplo de uso:
transacao_exemplo = [5000.0, 100.0, 50.0, 1.0, 0.0]  # substitua pelos dados da transação
resultado = predizer_fraude(transacao_exemplo)
print(f'Fraude detectada: {resultado}')
