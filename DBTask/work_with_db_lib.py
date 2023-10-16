import inspect
import random
import sqlite3


def get_cursor():
    """Method for getting the cursor.

    :return: Cursor to access the original database
    """
    conn = sqlite3.connect('ships.db')
    return conn.cursor()


def get_table_columns_names(table):
    """Method for obtaining ordered column names of the transmitted table.

    :param table: Table name
    :return: Ordered list of columns of the passed table
    """
    select = f'''PRAGMA table_info("{table}")'''
    cur = get_cursor()
    cur.execute(select)
    column_names = [i[1] for i in cur.fetchall()]
    return column_names


def get_obj_attributes(obj):
    """
    Method for obtaining attributes of the passed class.

    :param obj: Class object
    :return: List of attributes of the passed class
    """
    parameters = [a for a in inspect.getmembers(obj, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
    return parameters


def get_obj_attributes_without_mane(obj):
    """Method for obtaining attributes of the passed class, without an attribute with the object name.
    Necessary to receive a random attribute, which will be changed and entered into a new table.

    :param obj: Class object
    :return: List of attributes of the passed class, without the attribute with the object name
    """
    parameters = [a for a in inspect.getmembers(obj, lambda a: not(inspect.isroutine(a))) if not(a[0].startswith('__') and a[0].endswith('__'))]
    for parameter in parameters:
        if parameter[0] == 'ship':
            parameters.remove(parameter)
    return parameters


def get_random_obj_attribute(obj):
    """
    Method for getting a random attribute of a class object (Not including the attribute with the class name).

    :param obj: Class object
    :return: Random attribute of the passed class (Not including the attribute with the class name)
    """
    return random.choice(get_obj_attributes_without_mane(obj))


def get_correct_sequence_of_attributes(table, obj):
    """Method for ordering the attributes of the passed class, in accordance with the order of the columns of the passed
    tables from the database.

    :param table: Table name
    :param obj: Class object
    :return: List of attributes of the passed class, ordered accordingly. with the order of the columns of the table being transferred from the database
    """
    correct_sequence = []
    sequence_of_columns = get_table_columns_names(table)
    obj_attributes = get_obj_attributes(obj)
    for column_name in sequence_of_columns:
        for obj_attribute in obj_attributes:
            if column_name == obj_attribute[0]:
                correct_sequence.append(obj_attribute[-1])
                break
    return correct_sequence


def create_selection_to_insert(table, obj):
    """Method for entering data consisting of attributes of the passed class into the passed table.

    :param table: Table name
    :param obj: Class object
    :return: A string query in the database, indicating the name of the table where the entry will be made, and the values,
    being ordered according to with the order of the columns in the transmitted table
    """
    data = get_correct_sequence_of_attributes(table, obj)
    select = f'''INSERT INTO "{table}" VALUES{tuple(data)};'''
    return select


def create_selection_to_get_random_parameter_from_table(table, parameter):
    """Method for obtaining a random column value from the specified table.

    :param table: Table name
    :param parameter: Column name
    :return: A string query in the database, indicating the name of the table from which one random value will be received,
    piz of the transmitted column
    """
    select = f'''SELECT {parameter} FROM {table} ORDER BY RANDOM() LIMIT 1;'''
    return select


def get_three_random_parameters(list1, list2, list3):
    """Method for obtaining a list consisting of three random values ​​obtained from three different lists.
    The method was written in order to reduce the number of calls to the database at the stage of filling out the table with ships,
    when generating the original database.

    :param list1: List with gun models
    :param list2: List with engine models
    :param list3: List with case models
    :return: List of three random models of orids, engines and hulls. Essentially this is a list of
    components of a particular ship.
    """
    result = [random.choice(list1), random.choice(list2), random.choice(list3)]
    return result


