# -*- coding: utf-8 -*-
"""
Программа для осуществлении воспроизведения звукоых файлов клиентам телефонной сети
"""
# ##############################################################################
#  Copyright (c) 2021. Projects from AndreyM                                   #
#  The best encoder in the world!                                              #
#  email: muraig@ya.ru                                                         #
# ##############################################################################

import os
from contextlib import suppress
import asyncio
import sys

async def async_function(typeauto):
    from app.autodial.autodial_apps import check_applications, ARIApp
    # more async stuff...
    # FILENAME = "/home/andrei/PycharmProjects/web_realtime_streaming/other/some_other_file.tsv"
    env_root = os.path.abspath(os.path.dirname(__file__)).rsplit('/', 1)[0] + '/app/'
    env = env_root + '.env'
    # print(f"env: {env}") ; import sys ; sys.exit()

    await ARIApp(env).connect(typeauto)

async def get_date(typeauto=None):
    # строка с кодом, которую будем выполнять,
    # ее можно заменить любой командой
    code = 'import datetime; print(datetime.datetime.now())'
    code = await async_function(typeauto)

    # Создаем подпроцесс и перенаправляем
    # стандартный вывод в канал `PIPE`.
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Читаем вывод запущенной команды.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Ждем когда субпроцесс завершиться.
    await proc.wait()
    # возвращаем прочитанную строку
    #return line
    return 200

async def main(typeauto=None):
    # date = asyncio.run(get_date(typeauto))
    date = await get_date(typeauto)
    # выводим результат работы
    print(f"Current date: {date}")
    return 200


if __name__ == '__main__':
    with suppress(KeyboardInterrupt):
        main(typeauto=None)


# Current date: 2021-01-19 09:57:24.047066

'''
import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('ls /zzz'))
'''

'''
command = 'time sleep 5' # Here I used the 'time' only to have some output

def x(command):
    cmd = shlex.split(command)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return p

# Start the subprocess and do something else...
p = x(command)
# ...for example count the seconds in the mean time..

try: # This take care of killing the subprocess if problems occur
    for j in range(100):
        stdout.write('\r{:}'.format(j))
        stdout.flush()
        time.sleep(1)
        if p.poll() != None:
            print(p.communicate())
            break
except:
    p.terminate() # or p.kill()

'''

'''
import os
import time
import asyncio
import aioprocessing
def func(queue, event, lock, items):
    """ Demo worker function.

    This worker function runs in its own process, and uses
    normal blocking calls to aioprocessing objects, exactly
    the way you would use oridinary multiprocessing objects.

    """
    with lock:
        event.set()
        for item in items:
            time.sleep(1)
            queue.put(item+5)
    queue.close()
async def example(queue, event, lock):
    l = [1,2,3,4,5]
    p = aioprocessing.AioProcess(target=func, args=(queue, event, lock, l))
    p.start()
    while True:
        result = await queue.coro_get()
        if result is None:
            break
        print("Got result {}".format(result))
    await p.coro_join()
async def example2(queue, event, lock):
    await event.coro_wait()
    async with lock:
        await queue.coro_put(78)
        await queue.coro_name(async_function)
        await queue.coro_put(None) # Shut down the worker


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    queue = aioprocessing.AioQueue()
    lock = aioprocessing.AioLock()
    event = aioprocessing.AioEvent()
    tasks = [
        asyncio.ensure_future(example(queue, event, lock)),
        asyncio.ensure_future(example2(queue, event, lock)),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
'''

'''
import asyncio

class ProcServer:
    async def _transfer(self, src, dest):
        while True:
            data = await src.read(1024)
            if data == b'':
                break
            dest.write(data)

    async def _handle_client(self, r, w):
        loop = asyncio.get_event_loop()
        print(f'Connection from {w.get_extra_info("peername")}')
        child = await asyncio.create_subprocess_exec(
            *TARGET_PROGRAM, stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE)
        # sock_to_child = loop.create_task(self._transfer(r, child.stdin))
        sock_to_child = loop.create_task(self._sock_to_child(r, child))
        child_to_sock = loop.create_task(self._transfer(child.stdout, w))
        await child.wait()
        sock_to_child.cancel()
        child_to_sock.cancel()
        w.write(b'Process exited with status %d\n' % child.returncode)
        w.close()

    async def _sock_to_child(self, reader, child):
        try:
            await self._transfer(reader, child.stdin)
        except IOError as e:
            # IO errors are an expected part of the workflow,
            # we don't want to propagate them
            print('exception:', e)
        child.kill()

    async def start_serving(self):
        await asyncio.start_server(self._handle_client,
                                   '0.0.0.0', SERVER_PORT)

SERVER_PORT    = 6666
TARGET_PROGRAM = ['./test']

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    server = ProcServer()
    loop.run_until_complete(server.start_serving())
    #print('Serving on {}'.format(server.sockets[0].getsockname()))
    loop.run_forever()
'''

'''
import asyncio

class ServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.client_addr   = transport.get_extra_info('peername')
        self.transport     = transport
        self.child_process = None

        print('Connection with {} enstablished'.format(self.client_addr))

        asyncio.ensure_future(self._create_subprocess())

    def connection_lost(self, exception):
        print('Connection with {} closed.'.format(self.client_addr))

        if self.child_process.returncode is not None:
            self.child_process.terminate()

    def data_received(self, data):
        print('Data received: {!r}'.format(data))

        # Make sure the process has been spawned
        # Does this even make sense? Looks so awkward to me...
        while self.child_process is None:
            continue

        # Write any received data to child_process' stdin
        self.child_process.stdin.write(data)

    async def _create_subprocess(self):
        self.child_process = await asyncio.create_subprocess_exec(
            *TARGET_PROGRAM,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE
        )

        # Start reading child stdout
        asyncio.ensure_future(self._pipe_child_stdout())

        # Ideally I would register some callback here so that when
        # child_process exits I can write to the socket a goodbye
        # message and close the connection, but I don't know how
        # I could do that...

    async def _pipe_child_stdout(self):
        # This does not seem to work, this function returns b'', that is an
        # empty buffer, AFTER the process exits...
        data = await self.child_process.stdout.read(100) # Arbitrary buffer size

        print('Child process data: {!r}'.format(data))

        if data:
            # Send to socket
            self.transport.write(data)
            # Reschedule to read more data
            asyncio.ensure_future(self._pipe_child_stdout())


SERVER_PORT    = 6666
TARGET_PROGRAM = ['./test']

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ServerProtocol, '0.0.0.0', SERVER_PORT)
    server = loop.run_until_complete(coro)

    print('Serving on {}'.format(server.sockets[0].getsockname()))

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()
'''

'''
import asyncio
import os
import signal
import time

loop = asyncio.get_event_loop()

pid = os.fork()
if pid == 0:
    loop.close()
    signal.pause()
else:
    acknowledge_sigchild = asyncio.Future()


    def acknowledge(*args):
        print("ack sigchld", *args)
        acknowledge_sigchild.set_result(None)


    with asyncio.get_child_watcher() as watcher:
        watcher.add_child_handler(pid, acknowledge)

    time.sleep(1)
    print("sending sigterm")
    os.kill(pid, signal.SIGTERM)

    # Uncomment to fix the deadlock
    # loop.remove_reader(loop._ssock)
    # loop.add_reader(loop._ssock, loop._read_from_self)

    loop.run_until_complete(acknowledge_sigchild)  # deadlock
'''

'''
import os, asyncio, socket, multiprocessing


async def handler(loop, client):
    with client:
        while True:
            data = await loop.sock_recv(client, 64)
            if not data:
                break
            await loop.sock_sendall(client, data)


# create tcp server
def create_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('', 25000))
    sock.listen()
    sock.setblocking(False)
    return sock


# whenever accept a request ,create a handler task in eventloop
async def serving(loop, sock):
    while True:
        client, addr = await loop.sock_accept(sock)
        loop.create_task(handler(loop, client))


sock = create_server()

for num in range(multiprocessing.cpu_count() - 1):
    pid = os.fork()
    if pid <= 0:  # fork process as the same number as
        break  # my cpu cores

loop = asyncio.get_event_loop()
loop.create_task(serving(loop, sock))
loop.run_forever()
'''
