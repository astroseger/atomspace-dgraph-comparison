import re

def get_all(file_name, pattern):
    with open(file_name) as f:
        return re.findall(pattern, f.read())
    
    
def compare_two(f1, f2, pattern):
    rez1 = sorted(get_all(f1, pattern))
    rez2 = sorted(get_all(f2, pattern))
    
    set_rez1 = set(rez1)
    set_rez2 = set(rez2)
    if (len(rez1) != len(set_rez1)):
        print("Duplicates in rez1")
    if (len(rez2) != len(set_rez2)):
        print("Duplicates in rez2")
    if (set_rez1 != set_rez2):
        print("!!!! ERROR !!!!")
        exit(0)
    
    
    
compare_two("atomspace_reqs_1_rez.txt", "dgrap_req_1_rez.txt", "reservation-\d+")
#compare_two("atomspace_reqs_2_rez.txt", "dgrap_req_2_rez.txt", "reservation-\d+")


        
