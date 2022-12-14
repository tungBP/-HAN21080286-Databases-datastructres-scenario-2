All_routes = []

def Path_calculate(Start_point, Cities_list, Path_list, Distance):
    Path_list.append(Start_point)

    if len(Path_list) > 1:
        Distance += Cities_list[Path_list[-2]][Start_point]

    if (len(Cities_list) == len(Path_list)) and (Path_list[0] in Cities_list[Path_list[-1]]):
        Path_list.append(Path_list[0])
        Distance += Cities_list[Path_list[-2]][Path_list[0]]
        All_routes.append([Distance, Path_list])
        return


    for city in Cities_list:
        if (city not in Path_list) and (Start_point in Cities_list[city]):
            Path_calculate(city, Cities_list, list(Path_list), Distance)
    
if __name__ == '__main__':
    Cities_list = {
        'A': {'A': 0, 'B': 10, 'C': 15, 'D': 20, 'E': 30},
        'B': {'A': 10, 'B': 0, 'C': 35, 'D': 25, 'E': 35},
        'C': {'A': 15, 'B': 35, 'C': 0, 'D':30, 'E':40},
        'D': {'A': 20, 'B': 25, 'C': 30, 'D': 0, 'E':45},
        'E': {'A': 30, 'B': 35, 'C': 40, 'D': 45, 'E':0},
    }
    Path_calculate('A', Cities_list, [], 0)
    All_routes.sort()
    print ("Optimal route: %s" % All_routes[0][1:])
    print ("Optimal route distance: %s" % All_routes[0][0])
    
   
