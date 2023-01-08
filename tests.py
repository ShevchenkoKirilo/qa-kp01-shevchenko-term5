from binary import Binary
from buffer import Buffer
from folder import Folder
from log import Log
from types import NoneType


class Test:
    root = Folder("root", 16)

    def test_folder_create(self=None):
        folder1 = Folder("folder1", 16, Test.root)
        assert isinstance(folder1, Folder)
        assert folder1.name == "folder1"
        assert folder1.lim == 16
        assert folder1.parent == Test.root
        assert type(folder1.list()) is str

    def test_folder_move(self=None):
        folder2 = Folder("folder2", 16)
        assert type(folder2.parent) is NoneType
        folder2.move(Test.root)
        assert folder2.parent == Test.root

    def test_folder_list(self=None):
        folder3 = Folder("folder3", 16, Test.root)
        assert type(folder3.list()) is str

    def test_folder_delete(self=None):
        folder4 = Folder("folder4", 16, Test.root)
        del folder4

        assert "folder4" not in locals()

    def test_folder_delete_not_existing(self=None):
        folder5 = Folder("folder5", 16, Test.root)
        del folder5

        try:
            del folder5
        except NameError:
            assert True
        else:
            assert False

    def test_binary_create(self=None):
        binary1 = Binary("binary1", "content", Test.root)
        assert isinstance(binary1, Binary)
        assert binary1.name == "binary1"
        assert binary1.content == "content"
        assert binary1.parent == Test.root

    def test_binary_move(self=None):
        binary2 = Binary("binary2", "content")
        assert type(binary2.parent) is NoneType
        binary2.move(Test.root)
        assert binary2.parent == Test.root

    def test_binary_readfile(self=None):
        binary3 = Binary("binary3", "content", Test.root)
        assert binary3.readfile() == "content"

    def test_binary_delete(self=None):
        binary4 = Binary("binary4", "content", Test.root)
        del binary4

        assert "binary4" not in locals()

    def test_buffer_create(self=None):
        buffer1 = Buffer("buffer1", 16, Test.root)
        assert buffer1.name == "buffer1"
        assert buffer1.size == 16
        assert buffer1.parent == Test.root

    def test_buffer_move(self=None):
        buffer2 = Buffer("buffer2", 16)
        assert type(buffer2.parent) is NoneType
        buffer2.move(Test.root)
        assert buffer2.parent == Test.root

    def test_buffer_push(self=None):
        buffer3 = Buffer("buffer3", 16, Test.root)
        buffer3.push("content")
        assert buffer3.consume() == "content"

    def test_buffer_consume(self=None):
        buffer4 = Buffer("buffer4", 16, Test.root)
        buffer4.push("content")
        assert buffer4.consume() == "content"
        assert buffer4.consume() is None

    def test_buffer_delete(self=None):
        buffer5 = Buffer("buffer5", 16, Test.root)
        del buffer5

        assert "buffer" not in locals()

    def test_log_create(self=None):
        log1 = Log("log1", Test.root)
        assert log1.name == "log1"
        assert log1.parent == Test.root

    def test_log_move(self=None):
        log2 = Log("log2")
        assert type(log2.parent) is NoneType
        log2.move(Test.root)
        assert log2.parent == Test.root

    def test_log_append(self=None):
        log3 = Log("log3", Test.root)
        log3.append("content")

        assert log3.readfile() == "content" + "\n"

    def test_log_readfile(self=None):
        log4 = Log("log4", Test.root)
        log4.append("content")

        assert log4.readfile() == "content" + "\n"

    def test_log_delete(self=None):
        log5 = Log("log5", Test.root)
        del log5

        assert "log5" not in locals()
