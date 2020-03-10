class Flight:

    #define the flight information - might be a little excessive, but you get the idea
    def __init__(self, flightNumber, flightStartTime, flightEndTime, flightDate, startLocation, destination):
        self.flightNumber = flightNumber
        self.flightStartTime = flightStartTime
        self.flightEndTime = flightEndTime
        self.flightDate = flightDate
        self.startLocation = startLocation
        self.destination = destination
        self.pilot = []
        self.flightAttendants = []
        self.passengers = []

    #functions to add a pilot, flight attendent, and passenger to the flight
    def addPilot(self, pilot):
        self.pilot.append(pilot)

    def addFlightAttendant(self, flightAttendant):
        self.flightAttendants.append(flightAttendant)

    def addPassenger(self, passenger):
        self.passengers.append(passenger)

class Person:

    #superclass to define a person involved in flying
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.flights = []

    #function that lets a person add a flight
    def addFlight(self, flightNumber):
        self.flights.append(flightNumber)


class Passenger(Person):

    #class to define a person, inherits from Person class
    #adds passenger ID and seat number info, plus info from the Person constructor
    def __init__(self, firstName, lastName, passengerID, seatNumber):
        Person.__init__(self, firstName, lastName)
        self.passengerID = passengerID
        self.seatNumber = seatNumber


class Employee(Person):

    #defines a person who works at the airport, introduces variables for employee ID and hourly pay
    #inherits from Person class
    def __init__(self, firstName, lastName, employeeID, hourlyPay):
        Person.__init__(self, firstName, lastName)
        self.employeeID = employeeID
        self. hourlyPay = hourlyPay

    #calculates how much the employee gets paid during the flight
    def flightPay(self, flightDuration):
        return self.hourlyPay * flightDuration


class FlightAttendant(Employee):

    #inherits from Employee class
    def __init__(self, firstName, lastName, employeeID, hourlyPay):
        Employee.__init__(self, firstName, lastName, employeeID, hourlyPay)

    #overrides flightPay function for Employee class
    def flightPay(self, flightDuration):
        return self.hourlyPay * (flightDuration + 2) # add time to set up and clean plane


class Pilot(Employee):

    #inherits from Employee class, adds variable for pilot's license number
    def __init__(self, firstName, lastName, employeeID, hourlyPay, licenseNumber):
        Employee.__init__(self, firstName, lastName, employeeID, hourlyPay)
        self.licenseNumber = licenseNumber

#initialize 2 flights and 2 pilots, assign themselves to each other
flight1 = Flight(1042, 800, 1300, "04/23/2020", "New York", "London")
flight2 = Flight(543, 1500, 1800, "04/26/2020", "London", "Stockholm")

pilot1 = Pilot("John", "Mathews", 654321, 40, 464535)
pilot2 = Pilot("Ann", "Johnson", 363454, 35, 453444)

pilot1.addFlight(flight1.flightNumber)
flight1.addPilot(pilot1)
pilot2.addFlight(flight2.flightNumber)
flight2.addPilot(pilot2)

#print the flight pay of pilot 1
print(pilot1.flightPay((flight1.flightEndTime - flight1.flightStartTime) / 100))

#add a flight attendent to flight 2, calculate their pay
flightAttendant = FlightAttendant("Jack", "Black", 345354, 25)
flightAttendant.addFlight(flight2.flightNumber)
flight2.addFlightAttendant(flightAttendant)
print(flightAttendant.flightPay((flight2.flightEndTime - flight2.flightStartTime) / 100))

#add passengers to flight 2
pass1 = Passenger("Mary", "Sue", 234342, "D13")
pass2 = Passenger("Henry", "Ford", 466829, "C13")
pass1.addFlight(flight2.flightNumber)
flight2.addPassenger(pass1)
flight2.addPassenger(pass2)
pass2.addFlight(flight2.flightNumber)

#print the pilot, flight attendents, and passengers of flight 2
print(flight2.pilot)
print(flight2.flightAttendants)
for passenger in flight2.passengers:
    print(passenger.firstName + " " + passenger.lastName)


