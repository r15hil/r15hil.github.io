[__Back to Projects__](projects.md)


# Temperature controlled fan

This is a project I made to turn on/off a fan based on the temperature.

## What I already had
- Wire Jumpers 
- Resistors
- Temperature sensor (DS18B20)
- Fan (salvaged from an old hair dryer)
- Arduino Uno
- Breadboard

## What I had to get
- A mosfet (I used an IRFZ44N)

## How it works

The arduino reads the temperature from the sensor and if it is above 30 degrees, it turns on the mosfet which in turn turns on the fan. If the temperature is below 30 degrees, the mosfet is turned off and the fan is turned off.

## Code

```
#include <OneWire.h>
#include <DallasTemperature.h>

#define ONE_WIRE_BUS 12

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

void setup() {
  
  pinMode(13, OUTPUT); # Pin 13 is the mosfet gate
  Serial.begin(9600);
  sensors.begin();
}

void loop() {

  sensors.requestTemperatures(); // Send the command to get temperatures
  Serial.print("Celsius temperature: ");
  Serial.print(sensors.getTempCByIndex(0)); 
  Serial.print("\n");

  if( sensors.getTempCByIndex(0) > 30){
    digitalWrite(13, HIGH); // Turn on the mosfet
  } else{ 
    digitalWrite(13, LOW); // Turn off the mosfet
  }

  delay(5000); // Wait for 5 seconds

}

```

![image](../../assets/pics/temp_fan_schematic.jpeg)
![image](../../assets/pics/temp_fan_circuit.jpeg)

<iframe width="560" height="315" src="https://www.youtube.com/embed/KIM-IGIcUgY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Resources used
- [Temperature sensor guide](https://randomnerdtutorials.com/guide-for-ds18b20-temperature-sensor-with-arduino/)
- [Mosfet](https://images.theengineeringprojects.com/image/webp/2017/09/Introduction-to-IRFZ44N_3.png.webp?ssl=1)