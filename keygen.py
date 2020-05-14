import string
from random import choice, randint
from subprocess import PIPE, run


def generate_key():
    possible_chars = string.ascii_letters + string.digits
    key = [choice(possible_chars) for i in range(7)]
    key.insert(randint(0, len(key)), '@')
    key.insert(4, '-')
    return ''.join(key)


def test_key_gen(program, test_count):
    for i in range(test_count):
        key = generate_key()
        print(f"test {i+1}: {key}")
        x = run([program, key], stdout=PIPE, stderr=PIPE, universal_newlines=True)
        assert(x.returncode == 0)
    print(f"completed {test_count} successful runs!")
    return True

test_key_gen('./crackmeMario', 50)

