'''
from Weather_App import Fetch_analysis
from Weather_App import analyze_weather


city_list = ["New York", "London", "Mumbai", "Paris"]
weather_data = {city: Fetch_analysis.get_current_weather(city) for city in city_list}

for city, data in weather_data.items():
    print(f"{city}: {data['temperature']}°C,{data['condition']}")
    average_temp = analyze_weather.calculate_average_temperature(weather_data)
    if average_temp is not None:
        print(f"\nAverage Temperature:{average_temp:.2f}°C")
    else:
        print("\nNo valid temperature data to calculate average.")
        city = "New York"
        city_weather_data = weather_data[city]
        trend_message = analyze_weather.check_weather_trend(city_weather_data)
        print(f"\nWeather trend for {city}: {trend_message}")
'''

