class dispenser:

    roles = {'chairperson': 8, 'secretary': 4, 'scribe': 2, 'timekeeper': 1}
    
    def load_group(file):
        group_array = []
        for line in file:
            group_array.append({
                'name' : line.replace('\n', ''),
                'roles_nb' : 0,
                'roles_state' : 0
                })
        return group_array

    def sort_roles_nb(val): 
        return val['roles_nb']  

    def task_distribution(prosit_nb, group):
        result_array=[]
        for prosit in range(prosit_nb):
            prosit_roles = [prosit + 1]
            group_clone = group.copy()
            group_clone.sort(key=dispenser.sort_roles_nb)
            prosit_roles.append(dispenser.give_role(group, group_clone, 'chairperson'))
            prosit_roles.append(dispenser.give_role(group, group_clone, 'secretary'))
            prosit_roles.append(dispenser.give_role(group, group_clone, 'scribe'))
            prosit_roles.append(dispenser.give_role(group, group_clone, 'timekeeper'))
            result_array.append(prosit_roles)
        return result_array
        
    def check_role(member, role):
        return (member['roles_state'] // dispenser.roles[role])%2 == 0

    def give_role(group, group_sorted, role):
        for member in group_sorted:
            if (dispenser.check_role(member, role)):
                if (member['roles_state'] + dispenser.roles[role] == 15):
                    new_state = 0
                else:
                    new_state = member['roles_state'] + dispenser.roles[role]
                for people in group:
                    if (people['name'] == member['name']):
                        people['roles_state'] = new_state
                        people['roles_nb'] +=1
                        break
                group_sorted.remove(member)
                return member['name']
