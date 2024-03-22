from MotorDriver import my_sleep
from kalman_filter import KalmanFilter
from maf import MovingAverageFilter

kf = KalmanFilter()
maf = MovingAverageFilter(10)

while True:
    raw_yaw = kf.get_yaw()
    maf.add(raw_yaw)
    yaw = maf.get_average()
    print(yaw)
    my_sleep(100)
    

    
    