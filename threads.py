import threading


class Usuario:
    def __init__(self, idade):
        self.idade = idade


u = Usuario(20)


def calculo_estatistico(num_thread, usuario):
    usuario.idade += 1
    print('thread', num_thread, 'idade:', usuario.idade)


def salva_dados(num_thread, usuario):
    usuario.idade += 2
    print('thread', num_thread, 'idade:', usuario.idade)


t1 = threading.Thread(
    target=calculo_estatistico, args=(1, u,))

t2 = threading.Thread(
    target=salva_dados, args=(2, u,))

print('Thread Principal')

t2.start()
t1.start()

t1.join()
t2.join()
print('Isso será a última coisa impressa devido ao join')
