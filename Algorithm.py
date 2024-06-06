""" The logic for deciding which traffic lights should be on at the same time """
import Simulated_ir_input
import Traffic_light_objects

# A list that will represent all the traffic lights that will be on at the same time
final_combination = list()


def smart_combination(t_dict):
    """ Calculates the lane with the most cars for the given Dictionary """
    most_traffic = ["", 0]
    for lane in t_dict:
        a = t_dict[lane]
        if t_dict[lane] > most_traffic[1] and lane not in final_combination:
            most_traffic[0] = lane
            most_traffic[1] = t_dict[lane]
    return most_traffic[0]


def edit_dictionary(possibilities):
    """ Returns an array with all the possible combinations for a given name """
    return {k: Simulated_ir_input.lane_dict[k] for k in possibilities}


def calculate_possibilities():
    """ Calculates a combination of lanes starting from the lane with the most cars. It will always pick the next lane
     with the most cars, which will avoid collision until there is no lane to pick from. This is always a combination
     of four lanes given that there are three lanes per direction """

    """ Step 1: take the lane with the most cars """
    final_combination.append(smart_combination(Simulated_ir_input.lane_dict))
    """ Step 2: Take the lane with the most cars which can combine with the initial lane """

    possibilities = Traffic_light_objects.traffic_dict[final_combination[0]]
    final_combination.append(smart_combination(edit_dictionary(possibilities)))

    """ Step 3: Take the lane with the most cars which can combine with the initial lane and the second lane. This can
     be done using list intersection which creates a list with the values that match both lists """
    possibilities1 = Traffic_light_objects.traffic_dict[final_combination[0]]
    possibilities2 = Traffic_light_objects.traffic_dict[final_combination[1]]
    possibilities = list(set(possibilities1).intersection(possibilities2))
    final_combination.append(smart_combination(edit_dictionary(possibilities)))

    """ Step 4: Take the lane with the most cars which can combine with the initial lane and the second lane. This can
         be done using list intersection which creates a list with the values that match both lists """
    possibilities1 = Traffic_light_objects.traffic_dict[final_combination[0]]
    possibilities2 = Traffic_light_objects.traffic_dict[final_combination[1]]
    possibilities3 = Traffic_light_objects.traffic_dict[final_combination[2]]
    possibilities = set.intersection(*map(set, [possibilities1, possibilities2, possibilities3]))
    final_combination.append(smart_combination(edit_dictionary(possibilities)))
    print(final_combination)


calculate_possibilities()
