from imu import MPU6050

class KalmanFilter:
    def __init__(self):
        # Kalman filter parameters
        self.Q = [[0.001, 0], [0, 0.003]]  # Process noise covariance
        #@todo tune all this freaking values. 
        self.R = [[0.03]]  # Measurement noise covariance
        self.P = [[1, 0], [0, 1]]  # Estimation error covariance
        self.K = [[0], [0]]  # Kalman gain
        self.state_estimate = [[0], [0]] 

        # State transition matrix
        self.A = [[1, -0.1], [0, 1]]
        # Control input matrix (not used if there's no control input)
        self.B = [[0], [0]]
        # Measurement matrix
        self.H = [[1, 0]]

        self.mpu = MPU6050('X')  # Initialize MPU6050

    def dot(self, M, N):
        return [[sum(a*b for a,b in zip(M_row,N_col)) for N_col in zip(*N)] for M_row in M]

    def inv(self, M):
        # Matrix inversion (for 1x1 matrix)
        return [[1/M[0][0]]]

    def predict(self):
        self.state_estimate = self.dot(self.A, self.state_estimate)
        # Predict the error covariance
        AP = self.dot(self.A, self.P)
        self.P = self.dot(AP, [[self.A[0][0], self.A[1][0]], [self.A[0][1], self.A[1][1]]])  # Transpose A
        for i in range(2):
            for j in range(2):
                self.P[i][j] += self.Q[i][j]

    def update(self, measurement):
        PHt = self.dot(self.P, [[self.H[0][0]], [self.H[0][1]]])  # Transpose H
        S = self.dot(self.H, PHt)
        S[0][0] += self.R[0][0]
        self.K = self.dot(PHt, self.inv(S))
        # Update the estimate via measurement
        y = [[measurement[0][0] - self.dot(self.H, self.state_estimate)[0][0]]]
        self.state_estimate = [[self.state_estimate[i][0] + self.K[i][0] * y[0][0]] for i in range(2)]
        # Update the error covariance
        KH = self.dot(self.K, self.H)
        for i in range(2):
            for j in range(2):
                self.P[i][j] -= KH[i][0] * self.P[0][j]

    def get_yaw(self):
        accel_data = self.mpu.accel.xyz
        gyro_data = self.mpu.gyro.xyz
        yaw_rate = gyro_data[2]
        self.predict()
        self.update([[yaw_rate]])
        # Return the estimated yaw
        return self.state_estimate[0][0]


        