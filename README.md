# RainCheck

<img src="image.jpg" alt="Rainy image">

## Project Description
<hr>

This project sends an SMS alert to the user in the event of bad weather, such as rain or snow for the following day.

## Packages
<hr>

To install the required packages from the command line,
execute the following command as it contains all the packages
that have been used in the [requirements.txt](./requirements.txt) file.

```pip install -r requirements.txt```
## APIs
Weather data through [OpenWeatherMap API](https://openweathermap.org/api).
<br>
SMS Texts sent using the [Twilio API](https://www.twilio.com/en-us).

## Usage
<hr>

<ol>
<li>Create a <a href="https://openweathermap.org/">OpenWeatherMap</a> account</li>
    <ol>
        <li>Create an API Key and save to your <code>.env.text</code> file.</li>
        <li>Use the <code>os</code> module to access your API key from the <code>.env.text</code> file.</li>
    </ol>
<li>Create a <a href="https://www.twilio.com/en-us">Twilio</a> account
    <ol>
        <li>Verify your account with your phone number.</li>
        <li>Create a twilio phone number from the console panel.</li>
        <li>From the console panel, copy and paste your account_sid and your authentication token to your <code>.env</code> 
        with variable names of <code>ACC_SID</code> and <code>AUTH_TOKEN</code> and retrieve the values using the <code>os</code> module
        in your <code>main.py</code>.</li>
    </ol>
</li>

<li>Use <a href="https://latlong.net"> latlong.net</a> to get your latitude and longitude of your city, 
then edit the <code>LAT, LONG</code>variables in <code>main.py</code> with your latitude and longitude data.</li>
</ol>

### Note
<hr>
You can bypass the use of environment variables in this project and assign your personal details as string values if you only intend to use the project on your local machine. However, it's important to be aware of the risks of publishing your personal details on the internet.


## Alternatively
<hr>

You can use [PythonAnyWhere](https://www.pythonanywhere.com/) to schedule a task that runs every day on specific hour.

# Finally
<hr>
I appreciate you taking the time to read and view this project. Please take care and stay safe.


