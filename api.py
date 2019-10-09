import requests

APP_ID = 'AIzaSyChw-V04qU5R705zAeHGAP6wXkofZGpy80'
URL = 'https://maps.googleapis.com/maps/api/geocode/json'


class GeocodeAPi:

    def get_cords_by_location(self, location):
        response = requests.get(URL, {
            'key': APP_ID,
            'address': location
        })
        if response.json()['status'] == 'OK':
            results = response.json()['results'][0]
            coords = results['geometry']['location']
            print('location {}:'.format(location), coords)

    def get_location_by_coords(self, lat, lng):
        response = requests.get(URL, {
            'key': APP_ID,
            'latlng': ((str(lat)) + r',' + str(lng))
        })
        results = response.json()['results'][0]
        if response.json()['status'] == 'OK':
            address = results['formatted_address']
            print('coords: {}, {}\nlocation: {}'.format(lat, lng, address))


geocode_api = GeocodeAPi()
location = input('Input location: ')
geocode_api.get_cords_by_location(location)
print()
print('-----------------------------------------------------------')
print()
lat = 43.746362
lng = 7.430814900000001
geocode_api.get_location_by_coords(lat, lng)


