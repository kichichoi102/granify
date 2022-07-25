import sys
import pytest
from io import StringIO
from src.models.Cat import Cat
from src.models.Dog import Dog
from collections import defaultdict
from src.dataAccessLayer.Data import Data

class TestData():

    @pytest.fixture(scope='module')
    def data(self):
        self.data = Data('Database')
        return self.data

    def test_begin_tran(self, data):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        data.beginTran()

        consoleLog = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        assert consoleLog == 'Beginning a transaction\n'

    def test_rollback(self, data):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        data.rollback()

        consoleLog = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        assert consoleLog == 'Rolling back transaction\n'

    def test_time_stamp(self, data):
        timestamp = data.getTimestamp()
        assert timestamp == data.timestamp

    def test_log(self, data):
        log = defaultdict(list)
        assert log == data.log

    def test_insert(self, data):
        cat = Cat("Felix")
        dog = Dog("Beeny")
        data.insert("cat", cat)
        data.insert("dog", dog)
        assert data.log == {"cat": [(1, "Felix")],"dog":[(2, "Beeny")]}

    def test_get_all_logs(self, data):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        data.getAllLogs()

        consoleLog = buffer.getvalue()
        assert consoleLog == 'Table: cat, Timestamp: 1, Name: Felix\nTable: dog, Timestamp: 2, Name: Beeny\n'
        
    def test_get_log_by_name(self, data):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        data.getLogByName("Beeny")

        consoleLog = buffer.getvalue()
        assert consoleLog == 'Table: dog, Timestamp: 2, Name: Beeny\n'

    def test_get_log_by_timestamp(self, data):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        # get first timestamp item
        data.getLogByTimestamp(1)

        consoleLog = buffer.getvalue()
        assert consoleLog == 'Table: cat, Timestamp: 1, Name: Felix\n'

        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        # get second timestamp item
        data.getLogByTimestamp(2)

        consoleLog = buffer.getvalue()
        assert consoleLog == 'Table: dog, Timestamp: 2, Name: Beeny\n'

        # raise exception when timestamp is out of bounds
        try:
            data.getLogByTimestamp(10)
            assert False
        except Exception:
            assert True



        