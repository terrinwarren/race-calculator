from datetime import timedelta

def pace_calculator():
    print("Enter the total distance:")
    distance_in = input("Distance: ").strip()
    print("Enter the total time:")
    time_in = input("Time (hh:mm:ss): ").strip()
    

#helper function to convert time input into a time data type 

    def split_time(t):
        parts = t.split(":")
        h = float(parts[0])
        m = float(parts[1])
        s = float(parts[2])
        return timedelta(hours=h, minutes=m, seconds=s)
    
    #calculate the pace in seconds
    total_distance = float(distance_in) 
    total_time = split_time(time_in) 
    pace = total_time / total_distance

#split pace into minutes and seconds
    total_pace_seconds = int(pace.total_seconds())
    pace_min = total_pace_seconds // 60
    pace_sec = total_pace_seconds % 60

    print(f"Pace: {pace_min}:{pace_sec:02d} per mile")

pace_calculator()