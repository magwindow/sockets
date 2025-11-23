'''Доменная система имен'''
import socket

# возвращает IP-адрес доменного имени
# print(socket.gethostbyname('www.crappytaxidermy.com'))  # 66.6.44.4

# возвращает имя, список альтернативных имен и список адресов
# print(socket.gethostbyname_ex('www.crappytaxidermy.com'))  # ('crappytaxidermy.com', ['www.crappytaxidermy.com'], ['66.6.44.4'])

# ищет IP-адрес, но также возвращает достаточное количество информации для того,
# чтобы создать сокет, который с ним соединится
print(socket.getaddrinfo('www.crappytaxidermy.com', 80))  # [(<AddressFamily.AF_INET: 2>, 0, 0, '', ('66.6.44.4', 80))]