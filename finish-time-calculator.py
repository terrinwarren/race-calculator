from datetime import timedelta

def finish_time_calculator():
    print("Enter the total distance:")
    distance_in = input("Distance: ").strip()
    print("Enter the pace per mile:")
    pace_in = input("pace (mm:ss): ").strip()

#helper function to convert pace input into a time data type 

    def split_pace(t):
        parts = t.split(":")
        m = float(parts[0])
        s = float(parts[1])
        return timedelta(minutes=m, seconds=s)
    
    #calculate the total time
    total_distance = float(distance_in)
    total_pace = split_pace(pace_in)
    finish_time = total_distance * total_pace 
   
    finish_time_seconds = int(finish_time.total_seconds())
    finish_hour = finish_time_seconds // 3600
    finish_min = (finish_time_seconds % 3600) // 60
    finish_sec = finish_time_seconds % 60

    print(f"Finish Time: {finish_hour} hours: {finish_min} minutes: {finish_sec:02d} seconds")


finish_time_calculator()