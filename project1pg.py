from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample PG data dictionary with "Girls PG" changed to "Boys PG"
PG_DATA = {
    'sathya': {
        'name': 'Shree Sathya Deva PG',
        'city': 'Bangalore',
        'location': 'Ecity',
        'tabs': {
            'pginfo': {
                'owner': 'Narayana',
                'type': 'Boys PG',  # Changed from "Girls PG"
                'location_link': 'https://goo.gl/maps/yourmaplink',
                'features': 'Fully furnished rooms, home-cooked food, WiFi, laundry, 24/7 security and more.'
            },
            'rooms': {
                'Single Sharing': '₹8,500/month with food & WiFi',
                'Double Sharing': '₹6,500/month per person',
            },
            'nearby': {
                'Infosys campus': '1.5 km',
                'TCs': '1.5 km',
                'Techm': '1.5 km',
                'Schneider': '1.0 km',
                'Ecity bus stop': '75 meters',
                'Metro station': '100 meters',
            },
            'foodmenu': {
                'Monday': 'Idli',
                'Tuesday': 'Chapathi',
                'Wednesday': 'Dosa',
                'Thursday': 'Utappa',
                'Friday': 'Lemon rice',
                'Saturday': 'Puri',
                'Sunday': 'Punugulu',
            },
            'contact': {
                'Phone': '9876543210',
                'Email': 'info@shreesathya.com'
            },
            'support': 'For any help, contact support@shreesathya.com',
        }
    },
    'krishna': {
        'name': 'Shree Krishna PG',
        'city': 'Bangalore',
        'location': 'Marathahalli',
        'tabs': {
            'pginfo': {
                'owner': 'Ramesh',
                'type': 'Boys PG',
                'location_link': 'https://goo.gl/maps/anotherlink',
                'features': 'Cozy rooms, mess facility, WiFi, laundry.',
            },
            'rooms': {
                'Single Sharing': '₹7,500/month',
                'Double Sharing': '₹6,000/month per person',
            },
            'nearby': {
                'Infosys campus': '2.0 km',
                'TCs': '2.5 km',
                'Techm': '2.0 km',
                'Schneider': '1.5 km',
                'Bus stop': '100 meters',
                'Metro station': '300 meters',
            },
            'foodmenu': {
                'Monday': 'Dosa',
                'Tuesday': 'Chapathi',
                'Wednesday': 'Idli',
                'Thursday': 'Lemon rice',
                'Friday': 'Puri',
                'Saturday': 'Upma',
                'Sunday': 'Vada',
            },
            'contact': {
                'Phone': '9123456780',
                'Email': 'info@shreekrishna.com'
            },
            'support': 'For any help, contact support@shreekrishna.com',
        }
    }
    # Add more PGs similarly...
}

@app.route('/', methods=['GET', 'POST'])
def index():
    cities = sorted(set(pg['city'] for pg in PG_DATA.values()))
    locations = sorted(set(pg['location'] for pg in PG_DATA.values()))
    pg_list = None

    if request.method == 'POST':
        city = request.form.get('city')
        location = request.form.get('location')
        pg_list = {pg_id: data for pg_id, data in PG_DATA.items()
                   if data['city'] == city and data['location'] == location}
        return render_template('index.html', cities=cities, locations=locations, pg_list=pg_list, selected_city=city, selected_location=location)
    
    return render_template('index.html', cities=cities, locations=locations, pg_list=pg_list)

@app.route('/pg/<pg_id>')
def pg_detail(pg_id):
    pg = PG_DATA.get(pg_id)
    if not pg:
        return "PG not found", 404
    return render_template('pg_detail.html', pg=pg)

if __name__ == '__main__':
    app.run(debug=True)
