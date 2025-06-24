def calculate_average(scores):
    return round(sum(scores)/len(scores),2)

def percentage_distribution(scores):
    levels = {"90-100": 0, "80-89": 0, "70-79": 0, "60-69": 0,"<60": 0}
    for score in scores:
        if score >= 90: 
            levels["90-100"] +=1
        elif score >= 80: 
            levels["80-89"] +=1
        elif score >= 70: 
            levels["70-79"] +=1
        elif score >= 60: 
            levels["60-69"] +=1
        else:
            levels["<60"] +=1
    return levels

