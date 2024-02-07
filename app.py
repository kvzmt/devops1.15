from flask import Flask, render_template
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route('/')
def index():
    # ustaw ręcznie strefę czasową
    time_zone = timezone(timedelta(hours=1))  # UTC+1
    
    # pobranie obecnej strefy czasowej
    now = datetime.now(time_zone)
    current_time = now.strftime("%H:%M:%S")
    
    return render_template('index.html', time=current_time, time_zone='UTC+1')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')