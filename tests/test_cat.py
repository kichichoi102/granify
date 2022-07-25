import sys
import pytest
from io import StringIO
from src.models.Cat import Cat

class TestCat():

    @pytest.fixture(scope='module')
    def cat(self):
        self.cat = Cat('Felix')
        return self.cat

    def test_it_can_instantiate(self):
        cat = Cat()
        assert isinstance(cat, Cat)

    def test_name(self, cat):
        assert cat.name == 'Felix'

    def test_age(self, cat):
        assert 5 <= cat.age <= 10

    def test_prev_names(self, cat):
        assert cat.prevNames == ['Felix']
        cat.setName('Ben')
        assert cat.prevNames == ['Felix', 'Ben']

    def test_set_name(self, cat):
        cat.setName('Benny')
        assert cat.name == 'Benny'

    def test_set_age(self, cat):
        cat.setAge(10)
        assert cat.age == 10

    def test_set_favorite_food(self, cat):
        cat.setFavoriteFood('cake')
        assert cat.favoriteFood == 'cake'

    def test_get_name(self, cat):
        cat.setName('Felix')
        assert cat.getName() == 'Felix'
    
    def test_get_age(self, cat):
        age = cat.age
        assert cat.getAge() == age

    def test_get_favorite_food(self, cat):
        cat.setFavoriteFood(None)
        assert cat.getFavoriteFood() == None
        cat.setFavoriteFood('Jello')
        assert cat.getFavoriteFood() == 'Jello'

    def test_average_name_length(self, cat):
        res = 0
        for name in cat.prevNames:
            res += len(name)

        assert res/len(cat.prevNames) == cat.getAverageNameLength()

    def test_speak(self, cat):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        cat.speak()

        sys.stdout = old_stdout
        whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        assert whatWasPrinted == 'Meow\n'

        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        cat.speak('Hello World')

        whatWasPrinted = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        assert whatWasPrinted == 'Hello World\n'

