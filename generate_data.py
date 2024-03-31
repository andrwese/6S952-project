from math import cos, sin, pi
class Dynamics:
    '''
    Describes the state of a quadrotor drone, and calcualtes the state derivative/dynamic equations
    Model derived from: https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=5091&context=etd

    Member variables:
    -------------------
    position: 
        phi = roll angle between body frame and earth frame
        theta = pitch angle between body frame and earth frame
        psi = yaw angle between body frame and earth frame
        x = x position in earth frame
        y = y position in earth frame
        z = z position in earth frame

    velocity: 
        dphi
        dtheta
        dpsi
        dx
        dy
        dz
    parameters: 
        m = mass
        l = 
        g = gravitational acceleration
        c =
        Jx = inertia around x-axis
        Jy = inertia around y-axis
        Jz = inertia around z-axis
    '''
    
    def __init__(self, position=(0,0,0,0,0,0), velocity=(0,0,0,0,0,0), parameters=(0.8, 0.25,9.81,0.02,0.015,0.015,0.02)) -> None:
        if len(position) != 6:
            raise ValueError("Position array must have 6 elements")
        if len(velocity) != 6:
            raise ValueError("Velocity array must have 6 elements")
        if len(parameters) != 7:
            raise ValueError("Parameter array must have 7 elements")
        
        self.phi = position[0]
        self.theta = position[1]
        self.psi = position[2]
        self.x = position[3]
        self.y = position[4]
        self.z = position[5]

        self.dphi = velocity[0]
        self.dtheta = velocity[1]
        self.dpsi = velocity[2]
        self.dx = velocity[3]
        self.dy = velocity[4]
        self.dz = velocity[5]

        self.m = parameters[0]
        self.l = parameters[1]
        self.g = parameters[2]
        self.c = parameters[3]
        self.Jx = parameters[4]
        self.Jy = parameters[5]
        self.Jz = parameters[6]

    def update_position(self, new_position):
        if len(new_position) != 6:
            raise ValueError("New position array must have 6 elements")
        self.phi = new_position[0]
        self.theta = new_position[1]
        self.psi = new_position[2]
        self.x = new_position[3]
        self.y = new_position[4]
        self.z = new_position[5]

    def update_velocity(self, new_velocity):
        if len(new_velocity) != 6:
            raise ValueError("New velocity array must have 6 elements")
        self.dphi = new_velocity[0]
        self.dtheta = new_velocity[1]
        self.dpsi = new_velocity[2]
        self.dx = new_velocity[3]
        self.dy = new_velocity[4]
        self.dz = new_velocity[5]

    def get_acceleration(self, U):
        '''
        Uses the current position and velocity, together with the current control input, to calculate the state derivative at the current timestep
        U: current control input, i.e. uses the force inputted to each motor to describe how the systsem will translate/rotate

        Utz = F[1] + F[2] + F[3] + F[4]     # translation force along z-axis (body frame)
        Utx = F[4] - F[2]                   # translation force along x-axis
        Uty = F[1] - F[3]                   # translation force along y-axis
        Urz = F[1] + F[3] - F[2] - F[4]     # rotation force around z-axis (body frame)

        returns: (ddphi, ddtheta, ddpsi, ddx, ddy, ddz)
        '''
        if len(U) != 4:
            raise ValueError("force input array must have 4 elements")
    
        # Control input vector:
        Utz = U[0]     # translation force along z-axis (body frame)
        Utx = U[1]     # translation force along x-axis
        Uty = U[2]     # translation force along y-axis
        Urz = U[3]     # rotation force around z-axis (body frame)
        

        # Equation 3.13 - 3.15 from the paper:
        ddphi = self.l/self.Jx * Utx + self.Jy/self.Jx * self.dpsi * self.dtheta - self.Jz/self.Jx * self.dtheta * self.dpsi
        ddtheta = self.l/self.Jy * Uty + self.Jz/self.Jy * self.dpsi * self.dphi - self.Jx/self.Jy * self.dphi * self.dpsi
        ddpsi = self.l*self.c/self.Jz * Urz + self.Jx/self.Jz * self.dphi * self.dtheta - self.Jy/self.Jz * self.dtheta * self.dphi

        # Equations 3.18 - 3.20 from the paper:
        ddx = -Utz/self.m * (-cos(self.phi)*sin(self.theta)*cos(self.psi) + sin(self.phi)*sin(self.psi))
        ddy = -Utz/self.m * (cos(self.phi)*sin(self.theta)*cos(self.psi) + sin(self.phi)*cos(self.psi))
        ddz = -Utz/self.m * (-cos(self.phi)*cos(self.theta)) - self.g

        return (ddphi, ddtheta, ddpsi, ddx, ddy, ddz)
    
    def pid_controller(self, desired_state):
        '''
        calculates control input given error between current state and desired state
        Use Eq. 4.8, 4.11?
        '''


'''
TODO:
gjøre ferdig pid-controller. så de hadde noen gain-parametre i paperet
definere en desired trajectory
definere en loop som kan simulere state over tid, gitt et tidsintervall og en initial position/velocity (bruke forward euler?)

'''
