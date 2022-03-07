from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase, get_adjective, get_adverb
import random
import pytest


def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    plural_nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "men", "rabbits", "women"]
    for _ in range(4):

        word = get_noun(1)

        assert word in single_nouns
    for _ in range(4):

        quantity = random.randint(2, 11)

    
        word = get_noun(quantity)


        assert word in plural_nouns

def test_get_verb():


    past_verbs = [ "drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_single_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
  
    for _ in range(4):
        quantity = random.randint(1, 11)
   
        word = get_verb(quantity, "past") 

    
        assert word in past_verbs

    for _ in range(4):

        word = get_verb(1, "present")

        assert word in present_single_verbs

    for _ in range(4):
        quantity = random.randint(1, 11)
      
        word = get_verb(quantity, "future")

     
        assert word in future_verbs

    for _ in range(4):

   
        quantity = random.randint(2, 11)


        word = get_verb(quantity, "present")

       
        assert word in present_plural_verbs




def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below", "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]
    for _ in range(4):
    
        word = get_preposition()
        assert word in prepositions

def test_get_prepositional_phrase():
    for _ in range(4):
        phrase = get_prepositional_phrase(3)
        phrase_words = phrase.split()
        assert len(phrase_words) == 4

def test_get_adjective():
    adjectives = ["pretty", "sad", "fat", "fit", "sad", "alert", "smart", "dumb", "charming", "clever", "creepy", "crazy", "dirty", "clean" ]
    for _ in range(4):
    
        word = get_adjective()
        assert word in adjectives
def test_get_adverb():
    adverbs = ["boldly", "bravely","cheefully", "slowly","lazily", "poorly", "quietly"]
    for _ in range(4):
    
        word = get_adverb()
        assert word in adverbs
    

pytest.main(["-v", "--tb=line", "-rN", __file__])