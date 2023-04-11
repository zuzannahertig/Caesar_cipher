from encrypt import Encryptor, Decryptor, Cipher
from buffer import MemoryBuffer
from filehandler import FileHandler


class Executor:
    def execute(self, cypher_type, text, shift):
        rot_types = {1: 13, 2: 47}
        if shift in rot_types.keys():
            shift = rot_types[shift]

        def encrypt(text, shift):
            encryptor = Encryptor(shift)
            return 'encrypted', encryptor.cypher(text)

        def decrypt(text, shift):
            decryptor = Decryptor(shift)
            return 'decrypted', decryptor.cypher(text)

        options = {1: encrypt,
                   2: decrypt}

        status, text = options.get(cypher_type)(text, shift)
        data = {'id': Cipher.id, 'text': text, 'status': status, 'rot_type': f'ROT{shift}'}
        MemoryBuffer.history.append(data)

        print(MemoryBuffer.history)
        return MemoryBuffer.history


class Menu:
    def __init__(self):
        self.executor = Executor()
        self.running = True

    def show_menu(self):
        while self.running:
            text = input('Enter your text:\n')
            cypher_type = int(input('Choose:\n1 – to encrypt your text\n2 – to decrypt your text\n'))
            rot_type = int(input('Choose ROT type:\n1 – ROT13\n2 – ROT47\n3 – I want to enter my type of ROT (a '
                                 'number)\n'))
            if rot_type == 3:
                rot_type = int(input('Enter your type of ROT:\n'))

            self.executor.execute(cypher_type=cypher_type, text=text, shift=rot_type)

            answer = input('Do you want to enter another text? y/n\n')
            if answer == 'y':
                continue
            elif answer == 'n':
                save = input('Do you want to save your data? y/n\n')
                if save == 'y':
                    FileHandler.append_to_file('file', MemoryBuffer.history)
                self.running = False
            else:
                raise ValueError('Invalid answer.')


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == '__main__':
    main()
