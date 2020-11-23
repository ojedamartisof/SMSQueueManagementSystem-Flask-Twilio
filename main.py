from twilio.rest import Client


class main:
    def __init__(self):
        self.mode = None
        self.account_sid = 'AC57aae2a7c8e3efbd4b37c2cb0e1543d4'
        self.auth_token = '2dfb6bdf682db61c81691bd79a978c6c'
        self.client = Client(self.account_sid, self.auth_token)
        self._queue = []
        self._mode = 'FIFO'

    def enqueue(self, item):
        #### añadir a la cola ####
        self._queue.append(item)
        message = self.client.messages.create(
            body='Code night!' + str(item['name']) + ',the people practice all night' + str(
                self.size()) + ', dont sleep and PRACTICE MORE ',
            from_='+56959679839',
            to=str(item['phone'])
        )
        return message.sid


    def dequeue(self):
        ####procesar la cola ####
        if self.size() > 0:
            if self.mode == 'FIFO':
                item = self._queue.pop()
                return item
            elif self._mode == 'LIFO':
                item = self._queue.pop(-1)
                return item
        else:
            msg = {
                "msg": "Fila sin elementos"
            }
            return msg


    def get_queue(self):
        ####Retornar Toda la Fila####
        return self._queue


    def size(self):
        return len(self._queue)


def Main():
    return None