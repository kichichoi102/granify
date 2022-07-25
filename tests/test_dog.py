import sys
import pytest
from io import StringIO
from src.models.Dog import Dog

class TestDog():

    @pytest.fixture(scope='module')
    def dog(self):
        self.dog = Dog('Felix')
        return self.dog

    def test_it_can_instantiate(self):
        dog = Dog()
        assert isinstance(dog, Dog)

    def test_name(self, dog):
        assert dog.name == 'Felix'

    def test_age(self, dog):
        assert 5 <= dog.age <= 10

    def test_prev_names(self, dog):
        assert dog.prevNames == ['Felix']
        dog.setName('Ben')
        assert dog.prevNames == ['Felix', 'Ben']

    def test_set_name(self, dog):
        dog.setName('Benny')
        assert dog.name == 'Benny'

    def test_set_age(self, dog):
        dog.setAge(10)
        assert dog.age == 10

    def test_set_favorite_food(self, dog):
        dog.setFavoriteFood('cake')
        assert dog.favoriteFood == 'cake'

    def test_get_name(self, dog):
        dog.setName('Felix')
        assert dog.getName() == 'Felix'
    
    def test_get_age(self, dog):
        age = dog.age
        assert dog.getAge() == age

    def test_get_favorite_food(self, dog):
        dog.setFavoriteFood(None)
        assert dog.getFavoriteFood() == None
        dog.setFavoriteFood('Jello')
        assert dog.getFavoriteFood() == 'Jello'

    def test_average_name_length(self, dog):
        res = 0
        for name in dog.prevNames:
            res += len(name)

        assert res/len(dog.prevNames) == dog.getAverageNameLength()

    def test_speak(self, dog):
        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        dog.speak()

        sys.stdout = old_stdout
        consoleLog = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        assert consoleLog == 'Woof\n'

        old_stdout = sys.stdout # Memorize the default stdout stream
        sys.stdout = buffer = StringIO()

        dog.speak('Hello World')

        consoleLog = buffer.getvalue() # Return a str containing the entire contents of the buffer.
        assert consoleLog == 'Hello World\n'

