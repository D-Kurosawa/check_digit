"""Pickle object compress and decompress"""
import bz2
import pathlib
import pickle


def loads(compress_obj):
    try:
        decompress = bz2.decompress(compress_obj)
    except OSError:
        try:
            return pickle.loads(compress_obj)
        except Exception:
            raise IOError(f"object <{compress_obj}> is not pickle object")
    else:
        return pickle.loads(decompress)


def dumps(obj, compress_level=1, compress=True):
    pkl = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)

    if compress:
        return bz2.compress(pkl, compresslevel=compress_level)
    else:
        return pkl


def load(file_name):
    if not pathlib.Path(file_name).exists():
        raise FileNotFoundError(file_name)

    try:
        with bz2.BZ2File(file_name, 'rb') as f:
            pkl = f.read()
    except OSError:
        try:
            with open(file_name, 'rb') as f:
                return pickle.load(f)
        except Exception:
            raise IOError(f"file <{file_name}> can not read to pickle object")
    else:
        return pickle.loads(pkl)


def dump(obj, file_name, compress_level=1, compress=True):
    if compress:
        with bz2.BZ2File(file_name, 'wb', compresslevel=compress_level) as f:
            f.write(pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL))
    else:
        with open(file_name, 'wb') as f:
            pickle.dump(obj, f, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    def _main():
        a = dict(zip(range(1000000), range(1000000)))

        dump(a, 'a1.pkl.bz2')
        dump(a, 'a2.pkl', compress=False)

        print(a == load('a1.pkl.bz2'))
        print(a == load('a2.pkl'))

        b = dumps(a)
        c = dumps(a, compress=False)
        print(a == loads(b))
        print(a == loads(c))


    _main()
