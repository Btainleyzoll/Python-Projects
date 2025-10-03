import psutil

def get_cpu_usage(interval = 1):
    try:
        cpu_percent = psutil.cpu_percent(interval = interval)
        
    except psutil.Error:
        return None
  
    return cpu_percent if 0 <= cpu_percent <= 100 else None
   
def get_per_core_usage(interval = 1, percpu = True):
    core_usage = {}
    core_count = psutil.cpu_percent(interval=interval, percpu=percpu)
    for i, core in enumerate(core_count, start=1):
        core_usage[f"CPU {i}"] = core
    return core_usage
    
def get_cpu_times(interval = 1, percpu = False):
    try:
        
        info = psutil.cpu_times(percpu=percpu)
        print(type(info))
        #return infocheck
    except psutil.Error:
        return None
a = get_cpu_times()
print(a)