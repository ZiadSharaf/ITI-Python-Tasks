class Person:
    def __init__(self,name,money,mood,health_rate):
        self.name=name
        self.money=money
        self.mood=mood
        self.health_rate=health_rate

    def sleep(self,hours):
        if hours==7:
            self.mood="Happy"
        elif hours<7:
            self.mood="Tired"
        else:
            self.mood="Lazy"

    def eat(self,meals):
        if meals==3:
            self.health_rate=100
        elif meals==2:
            self.health_rate=75
        elif meals==1:
            self.health_rate=50

    def buy(self,items):
        self.money-=items*10


class Car:
    def __init__(self,name,fuel_rate,velocity):
        self.name=name
        self._fuel_rate=max(0,min(fuel_rate,100))
        self._velocity=max(0,min(velocity,200))

    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self,value):
        self._fuel_rate=max(0,min(value,100))

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self,value):
        self._velocity=max(0,min(value,200))

    def run(self,velocity,distance):
        self.velocity=velocity
        while distance>0 and self.fuel_rate>0:
            distance-=10
            self.fuel_rate-=1
        self.stop(distance)

    def stop(self, remain_distance):
        self.velocity=0
        if remain_distance<=0:
            print("You arrived at your destination.")
        else:
            print(f"Stopped with {remain_distance:.2f} km left due to finishing of the fuel.")


class Employee(Person):
    def __init__(self,name,money,id,car,email,salary,distance_to_work,mood="",health_rate=0):
        super().__init__(name,money,mood,health_rate)
        self.id=id
        self.car=car
        self.email=email
        self.salary=salary
        self.distance_to_work=distance_to_work

    def work(self,hours):
        if hours==8:
            self.mood="Happy"
        elif hours>8:
            self.mood="Tired"
        else:
            self.mood="Lazy"

    def drive(self,velocity,distance):
        self.car.run(velocity,distance)

    def refuel(self,gasAmount=100):
        self.car.fuel_rate+=gasAmount
        if self.car.fuel_rate>100:
            self.car.fuel_rate=100

    def send_mail(self,to,subject,body):
        print(f"Sending email to {to}\nSubject: {subject}\n{body}\nBest regards,\n{self.name}\n")


class Office:
    employees_num=0

    def __init__(self,name):
        self.name=name
        self.employees=[]

    def get_all_employees(self):
        return self.employees

    def get_employee(self,employee_id):
        return next((employee for employee in self.employees if employee.id==employee_id),None)

    def hire(self,employee):
        self.employees.append(employee)
        Office.employees_num+=1

    def fire(self,employee_id):
        self.employees=[employee for employee in self.employees if employee.id != employee_id]
        Office.employees_num-=1

    def deduct(self,employee_id,deduction):
        employee=self.get_employee(employee_id)
        if employee:
            employee.salary-=deduction

    def reward(self,employee_id,reward):
        employee=self.get_employee(employee_id)
        if employee:
            employee.salary+=reward

    def check_lateness(self,employee_id,move_hour):
        employee=self.get_employee(employee_id)
        if employee:
            velocity=60
            is_late=self.calculate_lateness("09:00",move_hour,employee.distance_to_work,velocity)
            if is_late:
                self.deduct(employee_id,10)
                print(f"{employee.name} is late. Salary deducted.")
            else:
                self.reward(employee_id,10)
                print(f"{employee.name} is on time. Salary increased.")

    @staticmethod
    def calculate_lateness(target_hour,move_hour,distance,velocity):
        def time_to_minutes(t):
            hours,minutes=map(int,t.split(":"))
            return hours*60+minutes

        target_minutes=time_to_minutes(target_hour)
        move_minutes=time_to_minutes(move_hour)
        travel_minutes=distance/velocity*60

        arrival_minutes=move_minutes+travel_minutes
        return arrival_minutes>target_minutes


    @classmethod
    def change_emps_num(cls,num):
        cls.employees_num=num



car=Car("Fiat 128",fuel_rate=100,velocity=60)
samy=Employee("Samy",500,1,car,"samy@iti.org",5000,20)
iti=Office("ITI Smart Village")

iti.hire(samy)

samy.sleep(7)
print(f"Mood after sleep: {samy.mood}")

samy.eat(2)
print(f"Health rate after eating 2 meals: {samy.health_rate}")

samy.buy(3)
print(f"Money after buying 3 items: {samy.money}")

samy.drive(60,20) 

samy.work(8)
print(f"Mood after working 8 hours: {samy.mood}")

samy.refuel()
print(f"Fuel rate after refueling: {car.fuel_rate}\n")

samy.send_mail("ahmed123@gmail.com","Football match","Will you watch the match tiday.")

iti.check_lateness(1,"08:40") 

print(f"Samy's salary: {samy.salary}")
print("All Employees:",[emp.name for emp in iti.get_all_employees()])
print(f"Number of employees: {iti.employees_num}")


print("\n--- Firing Employee ---")
iti.fire(1)
print("Number Remaining Employees after firing:",[emp.name for emp in iti.get_all_employees()])


Office.change_emps_num(0)
print(f"Updated employees number: {Office.employees_num}")
