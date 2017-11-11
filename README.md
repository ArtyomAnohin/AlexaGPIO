# AlexaGPIO

Custom Amazon Alexa skills to manipulate LED's with GPIO module


### Setup

```python
pip install Flask flask-ask
```

GPIO pins
```python
locationDict = {
    'blue': 25,       // GPIO pin 25
    'green': 24,      // GPIO pin 24
    'red': 23,        // GPIO pin 23
    'white': 22       // GPIO pin 22
}
```

### Commands

#### Location Intent - possibility to ON/OFF separate led.

```
run {Invocation Name}
```
######     {Invocation Name} - Skill name in Amazon Developer console


```
to turn {location} {status}
to change the {location} to {status}
```
###### {location} - led color [BLUE, GREEN, RED, WHITE]
###### {status} - ON or OFF


#### PlayIntent - simple demo 
```
play demo
```
