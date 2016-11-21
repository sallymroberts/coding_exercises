def get_unique_id(delivery_id_confirmations):
    """ Get unique delivery id from list of delivery id's
        List has up to 100 id's, all of which have duplicates,
        except 1. Identify the unique id with no duplicate.
    """
    delivery_ids = set()

    for id in delivery_id_confirmations:
        if id in delivery_ids:
            delivery_ids.remove(id)
        else:
            delivery_ids.add(id)

    for id in delivery_ids:
        return id
    
    return None


# Tests
print("*" * 80)

# Multiple delivery ids, 1 unique id, returns unique id
delivery_id_confirmations = [10, 8, 3, 3, 7, 99, 8, 10, 99]
print("Multiple ids, 1 unique id, returns unique id", "\n", 
    "Expect: 7", "\n", 
    "Actual:", get_unique_id(delivery_id_confirmations))

delivery_id_confirmations = [10, 8, 3, 3, 99, 8, 10, 99]
print("Multiple ids, no unique id, returns None", "\n", 
    "Expect: None", "\n", 
    "Actual:", get_unique_id(delivery_id_confirmations))


delivery_id_confirmations = []
print("Delivery ids is empty, returns None", "\n", 
    "Expect: None", "\n", 
    "Actual:", get_unique_id(delivery_id_confirmations))

