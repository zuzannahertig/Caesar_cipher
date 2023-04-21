from features.buffer import Text, MemoryBuffer


class TestBuffer:
    def setup_method(self):
        self.text = Text(text="def", status="encrypted", rot_type="ROT13")

    def test_class_text(self):
        assert (
            repr(self.text) == "Text(text='def', status='encrypted', rot_type='ROT13')"
        )

    def test_should_add_text_to_buffer(self):
        MemoryBuffer.add(self.text)
        assert MemoryBuffer.memory == [self.text]

    def test_should_return_buffer_as_dict(self):
        buffer = MemoryBuffer()
        memory_dict = buffer.return_buffer_as_dict()
        for entry in memory_dict:
            assert isinstance(entry, dict)
