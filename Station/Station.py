# Importing the geodesic module from the library
from geopy.distance import geodesic
  

cuttack = (20.462521, 85.882988)
bhubaneswar = (20.296059, 85.824539)
  
# Print the distance calculated in km
print('the distance between cuttack and bhubaneswar is')
print(geodesic(cuttack, bhubaneswar).km)