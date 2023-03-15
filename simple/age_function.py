from typing import List, Dict
import random


def age_data_generator() -> List[Dict[str, int]]:
    """
    A function that generates a 10 dictionary-list where each dictionary holds an id key and random age between 1 and 100

    Here are some tests:
    >>> ages = age_data_generator()
    >>> len(ages)
    10
    >>> all(isinstance(data['id'], int) and 1 <= data['id'] <= 10 for data in ages)
    True
    >>> all(isinstance(data['age'], int) and 1 <= data['age'] <= 100 for data in ages)
    True
    """

    age_values: List[Dict[str, int]] = [
        {'id': i+1, 'age': random.randint(1, 100)} for i in range(10)]

    return age_values


def sorted_age_values(age_list: List[Dict[str, int]]) -> List[Dict[str, int]]:
    """ A function that sorts the list generated in age_data_generator by age in descending order and print the id of the youngest and oldest.
    Also, it returns the sorted list.

    Here are some tests:
    >>> age_list =  [{'id': 1, 'age': 67}, {'id': 2, 'age': 42}, {'id': 3, 'age': 19}, {'id': 4, 'age': 81}, \
                    {'id': 5, 'age': 33}, {'id': 6, 'age': 88}, {'id': 7, 'age': 56}, {'id': 8, 'age': 73}, \
                    {'id': 9, 'age': 91}, {'id': 10, 'age': 10}] 
    >>> sorted_age_list = sorted_age_values(age_list)
    Oldest person ID: 9 
    Youngest person ID: 10 
    >>> sorted_age_list[0]['id'] == 9
    True
    >>> sorted_age_list[-1]['id'] == 10
    True
    """

    sorted_list = sorted(age_list, key=lambda x: x['age'], reverse=True)
    oldest = sorted_list[0]['id']
    youngest = sorted_list[-1]['id']

    print(f"Oldest person ID: {oldest}")
    print(f"Youngest person ID: {youngest}")

    return sorted_list
